# 🚀 Data Engineering Portfolio — Babitha Dharmaraj

Welcome to my Data Engineering portfolio.  
This repository showcases end-to-end modern data engineering solutions using:

- Azure Data Factory (ADF)
- Azure Data Lake Storage Gen2 (ADLS)
- Azure Databricks (PySpark + Delta Lake)
- Azure Synapse Analytics / Databricks SQL
- dbt for transformation and modeling
- Python automation with CI/CD using GitHub Actions
- Streaming (Kafka / Event Hub) *(optional project)*

---

## 📁 Projects Overview

| Project | Status | Tech Stack | Description |
|--------|--------|------------|-------------|
| **01 — Azure + Databricks End-to-End Data Platform** | 🛠 In Progress | ADF, ADLS, Databricks, Synapse, Delta Lake | A real-world cloud data pipeline using Medallion Architecture (Bronze → Silver → Gold). |
| **02 — Spark Optimization & Performance Engineering** | 🔜 | Databricks, PySpark | Demonstrating optimizer strategies, caching, AQE, partitioning & runtime improvements. |
| **03 — SQL + dbt Data Modeling** | 🔜 | dbt, Synapse / Databricks SQL | Data warehouse modeling with tests, lineage, macro automation & SCD Type 2. |
| **04 — Python + CI/CD Automation** | 🔜 | Python, GitHub Actions, pytest | Automated ETL workflows with testing, linting, and deployment pipeline. |
| **05 — Streaming Data Pipeline (Optional)** | 🔜 | Kafka/Event Hub, Databricks Structured Streaming | Real-time ingestion and processing architecture delivering incremental results. |

---

## 🏗 Architecture (High-Level)

This portfolio follows the Medallion Architecture:
(Source) → ADF → Raw (Bronze) → Databricks Transform (Silver) → Business Layer (Gold) → Synapse SQL / BI Layer

A visual diagram will be added once Project 1 reaches completion.

---

## 📦 Tech Skills Demonstrated

- Cloud Data Engineering (Azure)
- Data Lake design, partitioning & Delta Lake
- CI/CD for data pipelines
- Software engineering best practices (testing, linting, modular design)
- Data warehousing & modeling (Kimball + dbt)
- Real-time + batch pipelines
- Spark performance tuning at scale

---

## 🧪 Testing & Code Quality

This repo includes:

- `pytest` unit tests
- `flake8`, `black`, `isort` formatting
- Automated CI/CD checks via GitHub Actions

---

## 📊 Sample Dataset(s)

Sources used across projects include public real-world datasets such as:

- NYC Taxi Trips
- OpenWeather API
- UK Gov Open Data
- E-commerce transactions dataset

Dataset details will be documented per project folder.

---

## 🗂 Repository Structure

data-engineering-portfolio/
│
├─ 01-azure-databricks-end-to-end-platform/
├─ 02-databricks-spark-optimization/
├─ 03-dbt-sql-modeling/
├─ 04-python-ci-cd-automation/
├─ 05-streaming-pipeline-databricks-kafka/
└─ README.md

---

## 📅 Timeline

This portfolio is being built over **6–7 weeks** with structured milestones and continuous improvements.

---

## 📬 Contact

If you’d like to discuss opportunities or give feedback:

- **LinkedIn:** linkedin.com/in/babitha-dharmaraj  
- **Email:** *(optional — add if you want recruiters to contact you)*

---

> ⭐ This portfolio is actively being developed. Commit history shows progress, iteration, and real-world problem solving.
