Date: 28/12/2025 <br>
Time Spent: ~4-5 hours <br>
Day 3 - Silver Layer Transformation (Energy Trends – ET 5.1) <br>

# 🎯 Objective

Transform ET 5.1 Household Electricity Trends Excel dataset from Bronze to Silver layer, handling complex Excel structures and multiple reporting granularities.

# 🛠 Tools & Technologies Used

- Azure Databricks
- Apache Spark (PySpark)
- Delta Lake
- ADLS Gen2 (ABFSS access)
- spark-excel library
- Window functions & Spark SQL expressions

# 🔄 Tasks Completed
- Read ET 5.1 Excel file from ADLS Bronze container using com.crealytics.spark.excel
- Processed all three reporting structures:
	- Main Table
	- Annual data
	- Quarterly data
- Handled complex Excel layout:
	- Forward-filled hierarchical table names
	- Extracted embedded header rows
	- Cleaned and standardised column names
- Normalised schemas across tables for analytical readiness
- Rounded numeric columns for consistency
- Implemented reusable transformation functions for maintainability
- Wrote cleaned datasets to Silver layer in Delta format

# 🧠 Key Learnings

- Real-world Excel energy datasets often contain multiple logical tables per sheet
- Forward-filling hierarchical metadata is essential for downstream analytics
- Modular transformation functions significantly improve maintainability
- Databricks + ADLS Gen2 works seamlessly without DBFS mounts

# ✅ Outcome
- Silver Delta tables for ET 5.1:
	- energy_prices_main
	- energy_prices_annual
	- energy_prices_quarterly

# Status: 
✅ Completed successfully
