-- Purpose: Analytics view over Gold Delta table fact_electricity_by_fuel
-- Engine: Synapse Serverless SQL
-- Author: Babitha Dharmaraj

-- CREATE EXTERNAL DATA SOURCE EnergyGoldDataLake
-- WITH (
--     LOCATION = 'abfss://gold@stenergyplatformadls.dfs.core.windows.net'
-- );

CREATE OR ALTER VIEW vw_electricity_by_fuel
AS
SELECT
    [fuel],
	[generator_type],
	[metric_type],
	[unit],
	[ingestion_date],
	[period_type],
	TRY_CAST(value AS FLOAT) AS metric_value,
	[year],
	[quarter]
FROM
    OPENROWSET(
        BULK 'energy_trends/fact_electricity_by_fuel',
        DATA_SOURCE = 'EnergyGoldDataLake',
        FORMAT = 'DELTA'
    ) AS [result]