-- Purpose: Analytics query for UK electricity generation trends
-- Business Question: What are the short-term trends in electricity generation?
-- Dataset: fact_electricity_by_fuel (Gold)
-- Engine: Synapse Serverless SQL
-- Author: Babitha Dharmaraj

SELECT
    year,
    quarter,
    fuel,
    round(SUM(metric_value),2) AS quarterly_generation_gwh
FROM vw_electricity_by_fuel
WHERE metric_type = 'electricity_generated'
  AND period_type = 'quarterly'
  AND year >= YEAR(GETDATE()) - 5
  AND fuel not like '%Total%'
GROUP BY year, quarter, fuel
ORDER BY year, quarter;