-- Purpose: Analytics query for UK electricity generation trends
-- Business Question: What are the dominant fuel sources today?
-- Dataset: fact_electricity_by_fuel (Gold)
-- Engine: Synapse Serverless SQL
-- Author: Babitha Dharmaraj

WITH latest_year AS (
    SELECT MAX(year) AS max_year
    FROM vw_electricity_by_fuel
    WHERE period_type = 'annual'
)
SELECT
    fuel,
    round(SUM(metric_value),2) AS generation_gwh
FROM vw_electricity_by_fuel
WHERE year = (SELECT max_year FROM latest_year)
  AND metric_type = 'electricity_generated'
  AND fuel not like '%Total%'
GROUP BY fuel
ORDER BY generation_gwh DESC;