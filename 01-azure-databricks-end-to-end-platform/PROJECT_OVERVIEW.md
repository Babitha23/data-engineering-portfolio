# UK Energy Intelligence Lakehouse

## 🔍 Overview

This project demonstrates an end-to-end modern data engineering workflow using real UK Government open data related to energy production, pricing, and consumption trends.

The solution simulates how an enterprise energy analytics platform would ingest, process, store, and serve data using a scalable Lakehouse architecture.

The project includes batch ingestion, incremental update handling, data modelling, pipeline orchestration, CI/CD automation, and analytical consumption layers.

---

## 🎯 Objectives

- Build a reproducible cloud-based data engineering platform using:
  - Azure Data Lake Storage (ADLS)
  - Azure Data Factory
  - Azure Databricks (PySpark + Delta Lake)
  - Azure Synapse Analytics
  - dbt for transformation + documentation + testing
  - GitHub Actions for CI/CD pipeline automation

- Transform raw public datasets into trusted, structured datasets for analytics and reporting.

- Apply best practices in:
  - Data lake zone design (Bronze → Silver → Gold)
  - Incremental ETL processing
  - Dimensional modelling (star schema)
  - Data quality enforcement and validation
  - Code version control and automated deployment

---

## 📦 Data Sources

All datasets are sourced from the UK Government’s open data platform:

- Energy Trends & Prices (Monthly releases)
- UK Energy Consumption by Sector
- Electricity Production and Supply Trends
- Household Energy Pricing Trends

(See `DATA_DICTIONARY.md` for full metadata.)

---

## 🏛️ Architecture

Source Files (Gov.UK) -> Azure Data Factory (Ingestion Scheduling) -> Bronze Layer (Raw Data - ADLS) -> Databricks / PySpark (Cleaning, Standardization) -> Silver Layer (Validated & Structured Data) -> dbt + Delta Lake (Dimensional Modelling & Business Rules) -> Gold Layer (Analytics-Ready Data / Star Schema) -> Power BI / Synapse SQL / Notebooks

---

## 🔧 Technologies Used

| Category | Tools |
|---------|-------|
| Cloud | Microsoft Azure |
| Compute | Azure Databricks (Spark, Delta Lake) |
| Storage | ADLS Gen2 |
| Orchestration | Azure Data Factory |
| Modelling | dbt |
| Programming | Python, SQL |
| DevOps | GitHub Actions |
| Consumption | Synapse SQL, Power BI, Databricks Notebooks |

---

## 📈 Expected Outputs

- Automated data pipeline with scheduling and monitoring
- Enriched energy insights dataset with trend, forecasting, and comparison capabilities
- Fully documented and validated data model suitable for enterprise use
- Portfolio-quality artefacts demonstrating end-to-end data engineering capability

---

## 📜 Status

| Stage | Progress |
|-------|----------|
| Dataset selection | ✅ Completed |
| Initial ingestion planning | ⏳ In progress |
| Pipelines | 🔜 Next |
| Modelling | 🔜 Later |
| CI/CD | 🔜 Final |

---

## 🔗 Future Enhancements

- Streaming simulation for monthly updated datasets  
- ML forecasting for pricing trends  
- Power BI dashboard integration  

---
