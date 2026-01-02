-- Purpose: Analytics query for UK electricity generation trends
-- Business Question: How much of the UK’s electricity comes from renewables?
-- Dataset: fact_electricity_by_fuel (Gold)
-- Engine: Synapse Serverless SQL
-- Author: Babitha Dharmaraj

WITH CategorizedEnergy AS (
    SELECT 
        year,
        metric_value,
        CASE
            WHEN fuel IN ('Wind', 'Solar', 'Hydro (natural flow)', 'Bioenergy', 'Shoreline wave / tidal') THEN 'Renewable'
            ELSE 'Non-Renewable'
        END AS energy_category
    FROM vw_electricity_by_fuel
    WHERE metric_type = 'electricity_generated'
      AND period_type = 'annual'
      AND fuel NOT LIKE '%Total%'
)
SELECT 
    year,
    energy_category,
    ROUND(SUM(metric_value), 2) AS total_generation_gwh
FROM CategorizedEnergy
GROUP BY year, energy_category
ORDER BY year;