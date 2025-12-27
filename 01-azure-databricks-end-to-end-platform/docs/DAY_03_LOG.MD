Date: 27/12/2025
Time Spent: ~3-4 hours
Day 3 - Silver Layer Transformation (UK Energy Intelligence Lakehouse)

# 🎯 Objective

Transform raw Energy Trends Excel datasets from the Bronze layer into analytics-ready Delta tables in the Silver layer by handling hierarchical, multi-table Excel structures and enforcing data quality rules.

# 🛠 Tools & Technologies Used

- Azure Databricks
- Apache Spark (PySpark)
- Delta Lake
- ADLS Gen2 (ABFSS access)
- spark-excel library
- Window functions & Spark SQL expressions

# 📂 Datasets Processed

- Energy Trends – Fuel Used in Electricity Generation (multiple tables within a single Excel sheet)
- Source format: XLSX
- Structure: Hierarchical, multi-table, presentation-style Excel

# 🔄 Key Tasks Completed
## 1. Secure Access to ADLS Gen2 (Non-DBFS)
- Configured Hadoop-level access to ADLS Gen2 using ABFSS paths
- Resolved spark-excel authentication issue by explicitly setting Hadoop configuration
- Validated access using dbutils.fs.ls
✔ Enabled secure, mount-less data access aligned with modern Databricks best practices

## 2. Excel Ingestion Using spark-excel
- Installed and configured com.crealytics:spark-excel
- Read full Excel sheet without predefined ranges
- Avoided hardcoded table positions to support future structural changes
✔ Successfully ingested complex XLSX data directly from Bronze layer

## 3. Multi-Table Detection & Classification
- Identified table title rows dynamically using regex patterns
- Forward-filled table_name using window functions
- Assigned every row to its correct logical table
✔ Enabled scalable processing of multiple stacked tables within a single sheet

## 4. Hierarchical Data Normalisation
- Forward-filled hierarchical fields (e.g. generator_type)
- Cleaned fuel names using regex to remove notes and units
- Removed title rows, header rows, and empty rows
- Filtered null and invalid values
✔ Converted presentation-style data into structured analytical format

## 5. Silver Layer Delta Write
- Stored normalised datasets as Delta tables in the Silver container
- Preserved table-level lineage via table_name
- Ensured data is reusable for Gold star schema modelling

Silver path:
abfss://silver@stenergyplatformadls.dfs.core.windows.net/energy_trends_generation/

# 🧠 Key Learnings

- Government energy data is often published in human-readable Excel formats, not analytics-ready schemas
- Window functions are essential for handling hierarchical Excel structures
- Avoiding hardcoded ranges makes pipelines robust and future-proof
- spark-excel requires Hadoop-level configuration for ADLS access

# ✅ Outcome
- Successfully transformed complex, multi-table Excel datasets into clean Delta tables
- Silver layer now supports:
	- Fact table modelling
	- Aggregations
	- BI and SQL analytics
- Ready to design Gold star schema and analytical views