table: fact.ski6kvt
description: Skilsmisser efter type og tid
measure: indhold (unit Antal)
columns:
- type: values [SKIOP=Skilsmisser i alt, SMK=Skilsmisser mellem en mand og en kvinde, S2M=Skilsmisser mellem to mænd, S2K=Skilsmisser mellem to kvinder]
- tid: date range 2020-01-01 to 2025-06-01

notes:
- Despite the "kvt" suffix (normally kvartal/quarterly), this table is MONTHLY — all 12 months are present and tid steps month by month.
- Same type breakdown as ski6: SKIOP is the aggregate total of SMK + S2M + S2K. Filter to a single type or use SKIOP for total.
- Use this table for monthly seasonality or recent monthly trends (from 2020). For annual series back to 1999, use ski6.