Date: 26/12/2025
Time Spent: 3 hours
Day 2 - Bronze layer Implementation

# ✅ Key Tasks Completed

## Azure Data Factory Pipelines
- Created ADF pipelines to ingest raw datasets from GOV.UK
- Used Copy Activity (no data flows)
- Preserved:
	- Original schema
	- Column names
	- Raw values
- Configured sink to Bronze container in ADLS Gen2

## Bronze Layer Design Decisions
- Bronze layer treated as immutable raw data
- No schema enforcement or data cleansing applied
- Folder-based organization instead of table-based
- Enables reprocessing and replay if needed


## Spark Validation in Databricks
- Validated raw ingestion using Spark:

df_bronze = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(bronze_path)
)
display(df_bronze)


## ✔ Confirmed:
- Files are accessible from Databricks
- Headers and schema inferred correctly
- Raw data is intact

# 🛠 Tools & Services Used
- Azure Data Factory (ADF)
- Azure Data Lake Storage Gen2 (ADLS)
- Azure Databricks
- Apache Spark
- CSV / Excel datasets from GOV.UK

# 📂 Datasets Ingested (Bronze – Raw)
- Energy Trends – Household Electricity & Gas Prices (ET 5.1, ET 5.2)
- Stored as raw CSV files with no transformations
- Folder structure aligned to domain and dataset type