-- Purpose: Analytics query for UK electricity supply and demand
-- Business Question: How reliant is the UK on electricity imports?
-- Dataset: fact_electricity_supply_demand (Gold)
-- Engine: Synapse Serverless SQL
-- Author: Babitha Dharmaraj

SELECT
    year,
    supply_demand_components,
    SUM(metric_value) AS total_gwh
FROM vw_electricity_supply_demand
WHERE period_type = 'annual'
  AND supply_demand_components IN ('Imports', 'Exports')
GROUP BY year, supply_demand_components
ORDER BY year;
