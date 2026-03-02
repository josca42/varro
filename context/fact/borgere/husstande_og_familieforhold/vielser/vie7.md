table: fact.vie7
description: Vielser efter type og tid
measure: indhold (unit Antal)
columns:
- type: values [VIRP=Vielser i alt, VMK=Vielser mellem en mand og en kvinde, V2M=Vielser mellem to mænd, V2K=Vielser mellem to kvinder]
- tid: date range 1989-01-01 to 2024-01-01

notes:
- `type='VIRP'` is the aggregate total (vielser i alt). The 4 type codes are not mutually exclusive with VIRP — filtering VIRP gives the overall count while VMK/V2M/V2K are subsets. Never sum all 4 types together.
- For annual total marriages, use `type='VIRP'`. For breakdown by marriage type, use `type IN ('VMK','V2M','V2K')`.
- Annual data from 1989. For quarterly data use vie7kvt (from 2020).