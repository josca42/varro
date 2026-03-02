table: fact.best18
description: Bestyrelsesmedlemmer efter bestyrelsesmedlem, firmastatus, køn, virksomhedsstørrelse, branche (DB07 19-grp) og tid
measure: indhold (unit Antal)
columns:
- bestmedl: values [1=Nyt bestyrelsesmedlem, 2=Fortsættende bestyrelsesmedlem]
- firmastat: values [1=Ny i firmabestanden, 2=Fortsættende i firmabestanden]
- kon: values [100=Køn i alt, 200=Mænd, 300=Kvinder, 400=Uoplyst køn]
- virkstr: values [3001=I alt, 3005=Ingen ansatte, 3010=Under 10 årsværk, 3020=10-49 årsværk, 3030=50-249 årsværk, 3040=250 årsværk og derover]
- branchedb0721: join dim.db on branchedb0721=kode::text [approx]
- tid: date range 2023-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- Only covers 2023. This is an entry-flow table: bestmedl=1 (Nyt bestyrelsesmedlem) and bestmedl=2 (Fortsættende), firmastat=1 (Ny i firmabestanden) and firmastat=2 (Fortsættende).
- No total rows for bestmedl or firmastat — sum across both columns to get totals. All 4 combinations (1×1, 1×2, 2×1, 2×2) are present.
- branchedb0721 uses DB07 letter codes — dim.db join does not work. Use ColumnValues("best18", "branchedb0721").
- Filter kon='100' and virkstr='3001' for overall counts.