table: fact.pgkonv1
description: Konventionelt landbrug - Dækningsbidrag og jordrente efter produktionsgrene, regnskabsposter for afgrøder og tid
measure: indhold (unit -)
columns:
- prodgren1: values [1030=Korn i alt, 1031=Korn i alt, 1-50 hektar, 1050=Korn i alt, 50-100 hektar, 1055=Korn i alt, 100-250 hektar, 1060=Korn i alt, 250 hektar og derover ... 1135=Majs (grovfoder), 1140=Helsæd (grovfoder), 1145=Roer (grovfoder), 1150=Græs i omdrift (grovfoder), 1155=Vedvarende græs (grovfoder)]
- regnp: values [0=Population, antal bedrifter, 5=Stikprøve, antal bedrifter, 10=Areal, ha, 20=Høstudbytte, hkg/FE pr. ha, 25=Produktpris, kr. pr. hkg/FE ... 250=OMKOSTNINGER I ALT, 255=NETTOOVERSKLUD, 246=Jordomkostning, 265=Lønningsevne, 270=LØNNINGSEVNE, KR. PR. TIME]
- tid: date range 2021-01-01 to 2023-01-01
notes:
- regnp mixes many different metrics per crop branch: antal bedrifter, areal (ha), høstudbytte (hkg/FE pr. ha), produktpris (kr. pr. hkg/FE), and various cost items (kr. pr. ha). Units vary by code — always filter to a specific regnp and check the label for the unit.
- prodgren1 has size-bracketed sub-categories (e.g., 1031=Korn 1–50 ha, 1050=Korn 50–100 ha, 1055=Korn 100–250 ha, 1060=Korn 250+ ha) alongside totals (1030=Korn i alt). Never sum totals and sub-categories together.
- Covers konventionelt landbrug afgrøder (crops) only. For husdyr (livestock) use pgkonv2. For same structure in organic farming use pgoeko1.
- Only 3 years of data (2021–2023).
