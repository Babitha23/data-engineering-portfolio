-- Purpose: Analytics query for UK electricity supply and demand
-- Business Question: How do total electricity supply and demand compare year by year?
-- Dataset: fact_electricity_supply_demand (Gold)
-- Engine: Synapse Serverless SQL
-- Author: Babitha Dharmaraj

SELECT
    year,
    supply_demand_components,
    SUM(metric_value) AS total_gwh
FROM vw_electricity_supply_demand
WHERE period_type = 'annual' and supply_demand_components not like '%Total%'
GROUP BY year, supply_demand_components
ORDER BY year, supply_demand_components;
