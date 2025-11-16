| Dataset                 | Used For                                         | Type                                    | Frequency |
| ----------------------- | ------------------------------------------------ | --------------------------------------- | --------- |
| Historical Electricity  | Trend & baseline consumption                     | Batch                                   | Static    |
| Energy Trends (Monthly) | Incremental ETL, aggregation, forecasting        | Incremental batch / simulated streaming | Monthly   |
| ECUK                    | Dimensional model population (sector, fuel type) | Batch                                   | Annual    |
| NEED                    | Spark scaling, joins, optimization               | Batch                                   | Static    |
