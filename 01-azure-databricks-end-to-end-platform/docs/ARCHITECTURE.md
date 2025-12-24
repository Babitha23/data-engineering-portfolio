# 🔧 Technology Choices & Rationale
## Why Azure Databricks

Azure Databricks is used as the primary data transformation and processing engine because it provides:
- Scalable distributed processing using Apache Spark, suitable for handling large historical energy datasets.
- Separation of compute and storage, allowing flexible scaling without locking data into proprietary formats.
- Native integration with Azure Data Lake Storage (ADLS Gen2), enabling secure and high-throughput access to raw and curated data.
- Support for multiple languages (PySpark, SQL), which aligns with real-world enterprise data engineering practices.
- Optimized performance for batch analytics, making it ideal for building Bronze → Silver → Gold data pipelines.

Databricks is widely adopted in enterprise data platforms and reflects industry-standard tooling expected of senior data engineers.

## Why Delta Lake

Delta Lake is used as the storage layer format within the data lake to provide reliability and governance capabilities that traditional data lakes lack.

Key reasons include:
- ACID transactions, ensuring data consistency and reliability during concurrent reads and writes.
- Schema enforcement and schema evolution, preventing bad data from corrupting downstream analytics.
- Time travel capabilities, enabling rollback, auditing, and reproducibility of historical datasets.
- Improved performance through data skipping and metadata indexing.
- Unified batch and analytics workloads, supporting both transformation pipelines and analytical queries.

Using Delta Lake enables the data lake to behave like a modern data warehouse while maintaining cloud-scale flexibility.

## Why Azure Synapse Serverless SQL (Cost-Efficient Analytics Layer)

Azure Synapse Serverless SQL is used as the analytics query layer to expose curated (Gold) datasets for reporting and analysis.

It is chosen specifically because:
- No infrastructure provisioning or management is required.
- Pay-per-query model, where costs are incurred only for the amount of data scanned.
- Ideal for low-to-medium data volumes, which suits analytical exploration and dashboarding.
- Native querying of data directly from ADLS and Delta tables, avoiding data duplication.
- Tight integration with Power BI, enabling fast visualisation without additional ETL steps.

By avoiding dedicated SQL pools, the solution remains highly cost-effective while still providing enterprise-grade analytics access.

## Design Principle Summary

This architecture follows three core principles:

- Cost efficiency: avoid always-on compute resources.
- Scalability: handle growing datasets without redesign.
- Enterprise realism: mirror patterns used in production environments.