{{
  config({    
    "materialized": "ephemeral",
    "database": "dfinch",
    "schema": "mmo_simplified"
  })
}}

WITH `1k_aka_gpdip_edlud_289` AS (

  SELECT * 
  
  FROM {{ source('main_rishabh', '1k_aka_gpdip_edlud_289') }}

),

inactive_flag AS (

  {#Flags records where the user is marked as inactive.#}
  SELECT CASE
           WHEN is_active = 'N'
             THEN 1
           ELSE 0
         END AS is_not_active
  
  FROM `1k_aka_gpdip_edlud_289` AS in0

)

SELECT *

FROM inactive_flag
