table: fact.ski6
description: Skilsmisser efter type og tid
measure: indhold (unit Antal)
columns:
- type: values [SKIOP=Skilsmisser i alt, SMK=Skilsmisser mellem en mand og en kvinde, S2M=Skilsmisser mellem to mænd, S2K=Skilsmisser mellem to kvinder]
- tid: date range 1999-01-01 to 2024-01-01

notes:
- type=SKIOP is the national total — it equals SMK + S2M + S2K exactly. Never sum all four type values; use WHERE type='SKIOP' for total divorces, or filter to a specific type.
- Annual data (1999–2024). For monthly breakdown use ski6kvt.