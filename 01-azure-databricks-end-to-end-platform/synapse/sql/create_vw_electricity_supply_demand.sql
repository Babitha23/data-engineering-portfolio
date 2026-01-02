-- Purpose: Analytics view over Gold Delta table fact_electricity_supply_demand
-- Engine: Synapse Serverless SQL
-- Author: Babitha Dharmaraj

CREATE OR ALTER VIEW vw_electricity_supply_demand
AS
SELECT
    [supply_demand_components],
	[unit],
	[period_type],
	[year],
	[quarter],
	TRY_CAST(value AS FLOAT) AS metric_value,
	[ingestion_date]
FROM
    OPENROWSET(
        BULK 'energy_trends/fact_electricity_supply_demand/',
        DATA_SOURCE = 'EnergyGoldDataLake',
        FORMAT = 'DELTA'
    ) AS [result]
