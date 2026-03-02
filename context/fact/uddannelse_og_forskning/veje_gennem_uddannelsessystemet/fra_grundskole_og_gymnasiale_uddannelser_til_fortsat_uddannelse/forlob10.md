table: fact.forlob10
description: Fra grundskole til fortsat uddannelse efter afgangsårgang, afgangseksamen, afgangsinstitutionsregion, uddannelsesstatus, statustidspunkt efter afgang, uddannelse, køn, herkomst og tid
measure: indhold (unit Antal)
columns:
- afgaarg: values [2003=2003, 2004=2004, 2005=2005, 2006=2006, 2007=2007 ... 2020=2020, 2021=2021, 2022=2022, 2023=2023, 2024=2024]
- afgklas: values [TOT=I alt, H1020=H1020 Grundskole 7.-9. klasse, H1030=H1030 Grundskole 10. klasse]
- afgreg: join dim.nuts on afgreg=kode; levels [1]
- uddstat: values [1=I gang med en uddannelse, 2=Har fuldført en uddannelse, 3=Har afbrudt en uddannelse, 4=Ej påbegyndt]
- statustid: values [3=3 måneder, 15=1 år, 27=2 år, 39=3 år, 51=4 år, 63=5 år, 75=6 år, 87=7 år, 99=8 år, 111=9 år, 123=10 år, 135=11 år, 147=12 år, 159=13 år, 171=14 år, 183=15 år, 195=16 år, 207=17 år, 219=18 år, 231=19 år]
- uddannelse: values [TOT=I alt, H15=H15 Forberedende uddannelser, H20=H20 Gymnasiale uddannelser, H29=H29 Erhvervsfaglige grundforløb, H30=H30 Erhvervsfaglige uddannelser, H35=H35 Adgangsgivende uddannelsesforløb, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H90=H90 Uoplyst mv.]
- koen: values [10=Køn i alt, M=Mænd, K=Kvinder]
- herkomst: values [0=I alt, 10=Personer med dansk oprindelse, 20=Indvandrere, 30=Efterkommere, 40=Uoplyst]
- tid: date range 2022-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- tid is the publication snapshot year (2022, 2023, 2024), NOT the analysis year. The same cohort (afgaarg) appears in multiple tid snapshots with near-identical values. Always filter to tid = '2024-01-01' to avoid triple-counting. The cohort year is afgaarg.
- statustid is NOT additive. Values represent the same graduation cohort measured at different elapsed times (3=3 months, 15=1 year, 27=2 years, ..., 231=19 years after graduation). Pick a single statustid for analysis. Summing across statustid is meaningless.
- uddstat values 1-4 are mutually exclusive and sum to the full cohort at each statustid. There is no total row — to get the cohort size, sum all four: SUM(indhold) WHERE uddannelse='TOT'.
- uddannelse is only meaningful when uddstat='1' (i gang) or uddstat='2' (fuldført). When filtering to uddstat='1', uddannelse='TOT' gives total in education; sub-values (H15–H90) are mutually exclusive and sum to TOT.
- afgreg=0 is the national total and does NOT join to dim.nuts. For national queries use afgreg='0' directly. Regional breakdown uses kode 81–85 (niveau=1, 5 regions). No finer geography available.
- To get a simple cohort count: filter afgklas='TOT', uddannelse='TOT', koen='10', herkomst='0', afgreg='0', and pick one statustid and one tid.
- herkomst sub-values 10+20+30+40 sum exactly to herkomst='0' (I alt). 40=Uoplyst is very small (~13 persons per cohort). koen M+K sum to koen='10'.
- afgklas sub-values H1020 (7.–9. klasse) + H1030 (10. klasse) sum to TOT.
- Map: context/geo/regioner.parquet — merge on afgreg=dim_kode. Exclude afgreg=0.