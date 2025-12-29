# Databricks notebook source
#Below step is only for portfolio project. In real prod, need to use service principal to link storage account to Databricks
spark.sparkContext._jsc.hadoopConfiguration().set(
    "fs.azure.account.key.stenergyplatformadls.dfs.core.windows.net",
    "<Access_Key>"
)

# COMMAND ----------

#Validating access to storage account from Databricks
dbutils.fs.ls("abfss://bronze@stenergyplatformadls.dfs.core.windows.net/energy_trends/prices")

# COMMAND ----------

# MAGIC %md
# MAGIC Import libraries and functions

# COMMAND ----------

from pyspark.sql.functions import col, when, coalesce, last, monotonically_increasing_id, lit, to_date, year, month,  regexp_extract, expr, round
from pyspark.sql.window import Window
from pyspark.sql.types import FloatType, DoubleType

# COMMAND ----------

# MAGIC %md
# MAGIC Define functions

# COMMAND ----------

def forward_fill_tablename(df_bronze):
    #Adding a column to hold table name
    df_with_table = df_bronze.withColumn(
        "table_name",
        when(col("generator_type").rlike("(?i)table"), col("generator_type"))
    )
    #Repartitioning to 1 partition to have sequential row ids
    df_with_table = df_with_table.repartition(1)

    #Forward filling generator type and table names
    df = df_with_table.withColumn("row_id", monotonically_increasing_id())
    df = df.withColumn('generator_type', coalesce(col('generator_type'), last('generator_type', True).over(Window.orderBy('row_id')), lit('0')))
    df_filled = df.withColumn('table_name', coalesce(col('table_name'), last('table_name', True).over(Window.orderBy('row_id')), lit('0')))

    df_data = df_filled.filter( ~col("generator_type").rlike("(?i)table"))
    df_data = df_data.drop('row_id')

    return df_data

# COMMAND ----------

def transform_col_name(original_name, header_value):
    """
    Applies all logic: header extraction, lowercase, character removal, 
    'fuel' mapping, and 'provisional' removal.
    """
    # Use the value from the header row
    name = str(header_value)
    
    # Apply your specific string replacements & lowercase
    name = (name.lower()
            .replace(" ", "_")
            .replace("(", "")
            .replace(")", "")
            .replace("[", "")
            .replace("]", "")
            .replace("\n", "_"))
    
    # Logic: if 'fuel' is in the name, rename the whole thing to 'fuel'
    if "fuel" in name:
        return "fuel"
    
    # Logic: remove '_provisional'
    name = name.replace("_provisional", "")
    
    return name

# COMMAND ----------

def column_mapping(df_bronze):
    # 1. First, extract the header values from the specific row
    header_row = df_bronze.filter('_c0 like "Generator type"').limit(1).collect()[0]
    current_cols = df_bronze.columns

    # 2. Build the selection list using the zipped original column names and header row values
    new_columns = [
        col(old_name).alias(transform_col_name(old_name, header_row[i]))
        for i, old_name in enumerate(current_cols)]
    
    # 3. Apply all changes in one single transformation
    df_column_mapped = df_bronze.select(*new_columns)

    return df_column_mapped

# COMMAND ----------

def round_float_columns(df):
    # Identify columns that are Float or Double types
    float_cols = [f.name for f in df.schema.fields 
                if isinstance(f.dataType, (FloatType, DoubleType))]

    # Apply rounding to 2 decimal places for those specific columns
    for column in float_cols:
        df_cleaned = df.withColumn(column, round(col(column), 2))
    return df_cleaned


# COMMAND ----------

def clean_et51_tables(bronze_path, table):
    """
    Reads the excel file from bronze_path and returns a cleaned dataframe
    """
    if table == 'main':
        excel_data_address = "'Main Table'!A6"
    elif table == 'annual':
        excel_data_address = "'Annual'!A5"
    elif table == 'quarter':
        excel_data_address = "'Quarter'!A5"
    #Reading the excel file from bronze container
    df_bronze_main = (
        spark.read
        .format("com.crealytics.spark.excel")
        .option("header", "false")
        .option("inferSchema", "true")
        .option("dataAddress", excel_data_address)  # sheet name
        .load(bronze_path)
        )
    df_correct_columns = column_mapping(df_bronze_main)
    df_with_tablename = forward_fill_tablename(df_correct_columns)

    #Remove the header row from the data now that it's in the schema
    df_cleaned = df_with_tablename.filter('generator_type not like "Generator type"')

    #Rounding the float columns
    # df_cleaned = round_float_columns(df_cleaned)
    
    #Cleaning up the values in 'fuel' column                    
    df_final = df_cleaned.withColumn("fuel", regexp_extract(col("fuel"), r"^([A-Za-z ]+)", 1))

    return df_final

# COMMAND ----------

# MAGIC %md
# MAGIC Implementation

# COMMAND ----------

#Reading ET5.1 file from bronze container
bronze_path = "abfss://bronze@stenergyplatformadls.dfs.core.windows.net/energy_trends/prices/ET_5.1_SEP_25.xlsx"

for table in ('main', 'annual', 'quarter'):
  silver_path = f"abfss://silver@stenergyplatformadls.dfs.core.windows.net/energy_trends_generation/{table}/"
  df = clean_et51_tables(bronze_path, table)
  #Write cleaned data to appropriate silver path
  df.write.format("delta") \
        .mode("overwrite") \
        .save(silver_path)


# COMMAND ----------

dbutils.notebook.exit("Success")