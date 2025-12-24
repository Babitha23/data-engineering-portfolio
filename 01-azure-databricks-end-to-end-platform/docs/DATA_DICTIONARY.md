# Data Dictionary

This document captures metadata and definitions for the datasets used in the UK Energy Intelligence Lakehouse project.

---

## 1. Dataset Catalog

| Dataset Name | Source | Format | Update Frequency | Primary Use Case | Notes |
|-------------|--------|--------|------------------|------------------|-------|
| Historical Electricity Data | GOV.UK | CSV | Annual | Long-term trend analysis | Suitable for baseline metrics and historical comparisons |
| UK Energy Consumption (ECUK) | GOV.UK | XLS | Annual | Sector-level consumption analysis | Energy usage by domestic, industrial, transport, and services sectors |
| ET 5.1 – Household Electricity Prices | GOV.UK | XLS | Monthly | Price trend analytics | Time-series dataset used in pricing fact tables |
| ET 5.2 – Household Gas Prices | GOV.UK | XLS | Monthly | Comparative price analytics | Complements ET 5.1 for multi-fuel analysis |
| ET 1.1 – Indigenous Energy Production by Source | GOV.UK | XLS | Monthly | Energy production analysis | Multi-column dataset suitable for aggregation and joins |
| ET 3.1 – Final Energy Consumption by Sector | GOV.UK | XLS | Monthly | Fact table generation | Ideal for Bronze → Silver → Gold transformation layers |
| ET 4.1 – Electricity Supply, Demand, and Trade | GOV.UK | XLS | Monthly | Supply-demand analytics | Complex structure suitable for Spark normalization |
| NEED Dataset (Energy Efficiency) | GOV.UK | CSV / ODS | Occasional | Performance & optimization showcase | Large dataset used to demonstrate Spark optimization, joins, and partitioning |

---

## 2. Standard Data Columns Used Across Tables

| Column Name | Definition | Type | Example | Datasets |
|-------------|------------|------|---------|----------|
| `date` | Reporting date (month/year or year) | Date | `2025-07-01` | All |
| `region` | UK area / region (if applicable) | String | `North West` | Historical Electricity, ET 5.1/5.2, ET 3.1 |
| `energy_type` | Fuel or energy category | String | `Electricity`, `Gas`, `Coal` | ET 1.1, ET 3.1, Historical Electricity |
| `consumption_amount` | Volume of energy consumed | Decimal | `10322.5` | ECUK, ET 3.1, Historical Electricity |
| `unit` | Measurement unit (kWh, MWh, toe, etc.) | String | `kWh`, `£/MWh` | All |
| `price_value` | Cost per unit of energy | Decimal | `28.4` | ET 5.1, ET 5.2, ET 6.x (if available) |
| `production_amount` | Energy produced by source | Decimal | `1250.0` | ET 1.1, Historical Electricity |
| `sector` | Economic or consumption sector | String | `Domestic`, `Industrial` | ECUK, ET 3.1 |
| `source` | Energy source or fuel type | String | `Natural Gas`, `Coal`, `Solar` | ET 1.1, Historical Electricity |
| `reporting_period` | Month/Year covered by the record | String | `July 2025` | Monthly Energy Trends tables |
| `notes` | Any data-specific notes | String | `Estimated` | All |

---

## 3. Business Rules Applied in Transformations

| Rule | Layer Applied | Description |
|------|--------------|-------------|
| Standard date format | Silver | All date fields converted to `YYYY-MM-DD` to unify monthly and annual data across datasets |
| Normalized units | Silver | All consumption/production/price metrics standardized (e.g., kWh, MWh, toe, £/MWh) |
| Surrogate keys added | Gold | Used to support star schema dimensional modelling (dim_energy_type, dim_sector, dim_region, dim_time) |
| Null checks & validation | Silver | Records failing data quality rules stored in quarantine folder |
| Sector mapping | Silver | For datasets missing sector info (e.g., Historical Electricity), assign `Unknown` or aggregate level |
| Currency / price alignment | Silver | Prices standardized to £/MWh or £/kWh depending on dataset |
| Aggregation rules | Gold | Monthly Energy Trends tables aggregated by region / energy_type / sector when required |
| Joining datasets | Gold | Combine Historical Electricity, ECUK, and Energy Trends where dimensions match (time, sector, energy_type) |

---

## 4. Data Quality Checks

| Check Type | Rule |
|-----------|------|
| Completeness | No empty price, consumption, or production fields for reporting period |
| Schema consistency | Each new ingestion checked for column drift and unexpected changes |
| Range validation | Values must fall within realistic boundaries (e.g., consumption > 0, price > 0) |
| Duplicate removal | Remove duplicate rows after merging datasets (Bronze → Silver) |
| Missing sector / region | Flag records missing key dimension fields and store separately for review |
| File validation | Check filenames, sheet names, and formats before ingestion |
| Incremental validation | Ensure newly ingested rows do not duplicate previous months’ data |

---

## 5. Dimensions and Fact Tables (Target Star Schema)

### **Dimensions**

| Dimension Table | Key Columns | Notes |
|-----------------|------------|-------|
| `dim_time` | `time_id` (PK), `date`, `month`, `year`, `quarter` | Covers both monthly and annual datasets |
| `dim_region` | `region_id` (PK), `region_name` | Maps UK regions; optional for datasets without region info |
| `dim_energy_type` | `energy_type_id` (PK), `energy_type` | Electricity, Gas, Coal, Solar, Wind, etc. |
| `dim_sector` | `sector_id` (PK), `sector_name` | Domestic, Industrial, Transport, Services, Unknown |

### **Fact Tables**

| Fact Table | Measures / Columns | Linked Dimensions | Notes |
|------------|-----------------|-----------------|-------|
| `fact_energy_consumption` | `consumption_amount`, `unit` | `dim_time`, `dim_sector`, `dim_energy_type`, `dim_region` | From ECUK & ET 3.1 |
| `fact_energy_prices` | `price_value`, `unit` | `dim_time`, `dim_sector`, `dim_energy_type`, `dim_region` | From ET 5.1, ET 5.2 |
| `fact_energy_production` | `production_amount`, `unit` | `dim_time`, `dim_energy_type`, `dim_region` | From Historical Electricity & ET 1.1 |
| `fact_energy_supply_trade` | `supply_amount`, `trade_amount`, `unit` | `dim_time`, `dim_energy_type`, `dim_region` | From ET 4.1, normalized for Gold layer |

### Grain Definition

All fact tables are designed at a monthly grain unless otherwise stated.
Annual datasets are aligned to year-level granularity and mapped to the corresponding time dimension attributes.

---

## 6. Data Lineage (High-Level)

Source datasets are ingested into the Bronze layer in raw form.
All cleansing, validation, and normalization occur in the Silver layer.
Only conformed, analytics-ready tables are exposed in the Gold layer
for downstream consumption via Synapse Serverless and Power BI.

---
