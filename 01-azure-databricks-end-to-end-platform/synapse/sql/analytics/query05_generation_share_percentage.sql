-- Purpose: Analytics query for UK electricity generation trends
-- Business Question: What percentage of total generation does each fuel contribute?
-- Dataset: fact_electricity_by_fuel (Gold)
-- Engine: Synapse Serverless SQL
-- Author: Babitha Dharmaraj

WITH annual_totals AS (
    SELECT
        year,
        SUM(metric_value) AS total_generation
    FROM vw_electricity_by_fuel
    WHERE metric_type = 'electricity_generated'
      AND period_type = 'annual'
    GROUP BY year
)
SELECT
    f.year,
    f.fuel,
    round(SUM(f.metric_value),2) AS generation_gwh,
    ROUND(
        SUM(f.metric_value) / t.total_generation * 100, 2
    ) AS generation_percentage
FROM vw_electricity_by_fuel f
JOIN annual_totals t
    ON f.year = t.year
WHERE f.metric_type = 'electricity_generated'
  AND f.period_type = 'annual'
  AND f.fuel not like '%Total%'
GROUP BY f.year, f.fuel, t.total_generation
ORDER BY f.year, generation_percentage DESC;
