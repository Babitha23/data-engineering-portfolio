# Databricks notebook source
#Below step is only for portfolio project. In real prod, need to use service principal to link storage account to Databricks
spark.sparkContext._jsc.hadoopConfiguration().set(
    "fs.azure.account.key.stenergyplatformadls.dfs.core.windows.net",
    "<Access_Key>"
)

# COMMAND ----------

# MAGIC %md
# MAGIC Import libraries and functions

# COMMAND ----------

from pyspark.sql.functions import col, when, coalesce, last, monotonically_increasing_id, lit, to_date, year, month,  regexp_extract, expr, round
from pyspark.sql.window import Window
from pyspark.sql.types import FloatType, DoubleType

# COMMAND ----------

# MAGIC %md
# MAGIC Functions

# COMMAND ----------

def cleanup_colum_names(df):
    for c in df.columns:
        df = df.withColumnRenamed(
            c,
            c.lower()
             .replace(" ", "")
             .replace("(", "")
             .replace(")", "")
             .replace("\n", "")
        )
    return df

# COMMAND ----------

def clean_quarter_columns(df):
    # Mapping for the messy middle part
    mapping = {
        " 1st quarter": "_q1",
        " 2nd quarter": "_q2",
        " 3rd quarter": "_q3",
        " 4th quarter": "_q4",
        "\n1st quarter": "_q1",
        "\n2nd quarter": "_q2",
        "\n3rd quarter": "_q3",
        "\n4th quarter": "_q4",
        "1st\nquarter": "_q1",
        "2nd\nquarter": "_q2",
        "3rd\nquarter": "_q3",
        "4th\nquarter": "_q4"
    }
    # Generate new names by checking if the suffix exists in our mapping
    new_cols = []
    for col in df.columns:
        new_name = col
        for messy, clean in mapping.items():
            if messy in col:
                new_name = col.replace(messy, clean)
        new_cols.append(new_name)
    df = df.toDF(*new_cols)
    return df

# COMMAND ----------

def clean_et52_tables(bronze_path, table):
    if table == 'main':
        excel_data_address = "'Main Table'!A5"
    elif table == 'annual':
        excel_data_address = "'Annual'!A4"
    elif table == 'quarter':
        excel_data_address = "'Quarter'!A5"

    df_bronze = (
            spark.read
            .format("com.crealytics.spark.excel")
            .option("header", "true")
            .option("inferSchema", "true")
            .option("dataAddress", excel_data_address)  # sheet name
            .load(bronze_path)
            )
    if table == 'main':
        df_bronze = df_bronze.drop('_c14')
        #Renaming columns
        new_columns = ['supply_demand_components', '2023', '2024', 'annual_percent_change', 'q2_2023', 'q3_2023', 'q4_2023', 'q1_2024', 'q2_2024', 'q3_2024', 'q4_2024', 'q1_2025', 'q2_2025', 'percent_change']
        df_bronze = df_bronze.toDF(*new_columns)
    elif table == 'quarter':
        df_bronze = df_bronze.withColumnRenamed("Components of supply and demand", "supply_demand_components")
        df_bronze = clean_quarter_columns(df_bronze)
        for c in df_bronze.columns:
                df_bronze = df_bronze.withColumnRenamed(
                    c,
                    c.lower()
                    .replace("[provisional]", "")
                    .replace(" ", "")
                    .replace("\n", "")
                )
    elif table == 'annual':
        header_row = df_bronze.first()
        new_column_names = [str(header_row[i]) for i in range(len(header_row))]
        df_bronze = df_bronze.toDF(*new_column_names).filter(col(new_column_names[0]) != header_row[0])
        df_bronze = df_bronze.withColumnRenamed("Components of supply and demand", "supply_demand_components")
        df_bronze = cleanup_colum_names(df_bronze)

    cols_to_fix = [c for c in df_bronze.columns if c != "supply_demand_components"]

    # Apply transformations: cast to float, fill nulls with 0, and round to 2 decimals
    df_cleaned = df_bronze.select(
        "supply_demand_components",
        *[round(coalesce(col(c).cast("double"), lit(0)), 2).alias(c) for c in cols_to_fix]
    )

    #Filtering out the rows with null values
    df_cleaned = df_bronze.filter(col('supply_demand_components').isNotNull())

    return df_cleaned

# COMMAND ----------

# MAGIC %md
# MAGIC Implementation

# COMMAND ----------

#Reading ET5.1 file from bronze container
bronze_path = "abfss://bronze@stenergyplatformadls.dfs.core.windows.net/energy_trends/prices/ET_5.2_SEP_25.xlsx"

for table in ('main','annual', 'quarter'):
  silver_path = f"abfss://silver@stenergyplatformadls.dfs.core.windows.net/energy_trends_supply_demand/{table}/"
  df = clean_et52_tables(bronze_path, table)
  #Write cleaned data to appropriate silver path
  df.write.format("delta") \
        .mode("overwrite") \
        .save(silver_path)

# COMMAND ----------

dbutils.notebook.exit("Success")