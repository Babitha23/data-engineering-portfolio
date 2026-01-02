-- Purpose: Analytics query for UK electricity supply and demand
-- Business Question: Does the UK produce more electricity than it consumes?
-- Dataset: fact_electricity_supply_demand (Gold)
-- Engine: Synapse Serverless SQL
-- Author: Babitha Dharmaraj

WITH supply AS (
    SELECT year, SUM(metric_value) AS supply_gwh
    FROM vw_electricity_supply_demand
    WHERE period_type = 'annual'
      AND supply_demand_components = 'Total supply'
    GROUP BY year
),
demand AS (
    SELECT year, SUM(metric_value) AS demand_gwh
    FROM vw_electricity_supply_demand
    WHERE period_type = 'annual'
      AND supply_demand_components = 'Total demand'
    GROUP BY year
)
SELECT
    s.year,
    s.supply_gwh,
    d.demand_gwh,
    round(s.supply_gwh - d.demand_gwh, 2) AS net_balance_gwh
FROM supply s
JOIN demand d
    ON s.year = d.year
ORDER BY s.year;