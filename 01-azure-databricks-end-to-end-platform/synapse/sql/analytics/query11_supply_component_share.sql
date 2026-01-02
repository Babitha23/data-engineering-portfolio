-- Purpose: Analytics query for UK electricity supply and demand
-- Business Question: Which components contribute most to electricity supply?
-- Dataset: fact_electricity_supply_demand (Gold)
-- Engine: Synapse Serverless SQL
-- Author: Babitha Dharmaraj

WITH annual_supply_total AS (
    SELECT
        year,
        SUM(metric_value) AS total_supply
    FROM vw_electricity_supply_demand
    WHERE period_type = 'annual'
      AND supply_demand_components not like '%Total%'
    GROUP BY year
)
SELECT
    f.year,
    f.supply_demand_components,
    SUM(f.metric_value) AS component_gwh,
    ROUND(
        SUM(f.metric_value) / t.total_supply * 100, 2
    ) AS supply_percentage
FROM vw_electricity_supply_demand f
JOIN annual_supply_total t
    ON f.year = t.year
WHERE f.period_type = 'annual'
  AND f.supply_demand_components not like '%Total%'
GROUP BY f.year, f.supply_demand_components, t.total_supply
ORDER BY f.year, supply_percentage DESC;