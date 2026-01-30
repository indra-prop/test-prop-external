{{
  config({    
    "materialized": "ephemeral",
    "database": "dfinch",
    "schema": "mmo_simplified"
  })
}}

WITH OrchestrationSource_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('asd', 'OrchestrationSource_1') }}

),

Aggregate_0 AS (

  SELECT * 
  
  FROM OrchestrationSource_1 AS in0

)

SELECT *

FROM Aggregate_0
