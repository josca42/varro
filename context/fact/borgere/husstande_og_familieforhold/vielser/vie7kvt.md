table: fact.vie7kvt
description: Vielser efter type og tid
measure: indhold (unit Antal)
columns:
- type: values [VIRP=Vielser i alt, VMK=Vielser mellem en mand og en kvinde, V2M=Vielser mellem to mænd, V2K=Vielser mellem to kvinder]
- tid: date range 2020-01-01 to 2025-06-01

notes:
- Quarterly version of vie7. Same type column and same filtering rules: `type='VIRP'` is the aggregate total; VMK/V2M/V2K are the three subtypes. Never sum all 4 types.
- `tid` is quarterly (e.g. 2024-01-01 = Q1 2024). The most recent data here (up to 2025Q2) is more current than vie7's annual data.