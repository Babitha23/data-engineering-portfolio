-- Purpose: Analytics query for UK electricity supply and demand
-- Business Question: Is electricity demand increasing or decreasing over time?
-- Dataset: fact_electricity_supply_demand (Gold)
-- Engine: Synapse Serverless SQL
-- Author: Babitha Dharmaraj

SELECT
    year,
    SUM(metric_value) AS total_demand_gwh
FROM vw_electricity_supply_demand
WHERE period_type = 'annual'
  AND supply_demand_components = 'Total demand'
GROUP BY year
ORDER BY year;

