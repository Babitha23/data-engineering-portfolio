-- Purpose: Analytics query for UK electricity generation trends
-- Business Question: How has electricity generation by fuel changed over time?
-- Dataset: fact_electricity_by_fuel (Gold)
-- Engine: Synapse Serverless SQL
-- Author: Babitha Dharmaraj

SELECT
    year,
    fuel,
    round(SUM(metric_value),2) AS total_generation_gwh
FROM vw_electricity_by_fuel
WHERE metric_type = 'electricity_generated'
  AND period_type = 'annual'
  AND fuel not like '%Total%'
GROUP BY year, fuel
ORDER BY year DESC, total_generation_gwh DESC;
