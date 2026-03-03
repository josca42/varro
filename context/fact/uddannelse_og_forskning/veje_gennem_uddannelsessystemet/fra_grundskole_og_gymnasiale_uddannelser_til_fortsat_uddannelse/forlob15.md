table: fact.forlob15
description: Fra gymnasiale uddannelser til fortsat uddannelse efter afgangsårgang, afgangseksamen, afgangsinstitutionsregion, uddannelsesstatus, statustidspunkt efter afgang, uddannelse, køn, herkomst og tid
measure: indhold (unit Antal)
columns:
- afgaarg: values [2008=2008, 2009=2009, 2010=2010, 2011=2011, 2012=2012, 2013=2013, 2014=2014, 2015=2015, 2016=2016, 2017=2017, 2018=2018, 2019=2019, 2020=2020, 2021=2021, 2022=2022, 2023=2023, 2024=2024]
- afgklas: values [TOT=I alt, H2010=H2010 Alment gymnasiale uddannelser, H2020=H2020 Erhvervsrettede gymnasiale uddannelser, H2030=H2030 Internationale gymnasiale uddannelser]
- afgreg: join dim.nuts on afgreg=kode; levels [1]
- uddstat: values [1=I gang med en uddannelse, 2=Har fuldført en uddannelse, 3=Har afbrudt en uddannelse, 4=Ej påbegyndt]
- statustid: values [3=3 måneder, 15=1 år, 27=2 år, 39=3 år, 51=4 år, 63=5 år, 75=6 år, 87=7 år, 99=8 år, 111=9 år, 123=10 år, 135=11 år, 147=12 år, 159=13 år, 171=14 år, 183=15 år, 195=16 år, 207=17 år, 219=18 år, 231=19 år]
- uddannelse: values [TOT=I alt, H15=H15 Forberedende uddannelser, H20=H20 Gymnasiale uddannelser, H29=H29 Erhvervsfaglige grundforløb, H30=H30 Erhvervsfaglige uddannelser, H35=H35 Adgangsgivende uddannelsesforløb, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H90=H90 Uoplyst mv.]
- koen: values [10=Køn i alt, M=Mænd, K=Kvinder]
- herkomst: values [0=I alt, 10=Personer med dansk oprindelse, 20=Indvandrere, 30=Efterkommere, 40=Uoplyst]
- tid: date range 2022-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Same structure as forlob10 but starting population is gymnasium graduates (afgklas: H2010=alment gymnasiale, H2020=erhvervsrettede, H2030=internationale). Cohorts run from 2008 (vs 2003 for forlob10).
- tid is the publication snapshot year (2022, 2023, 2024). Filter to tid = '2024-01-01' to avoid triple-counting the same cohort across snapshots.
- statustid is NOT additive. Values are repeated measurements of the same cohort at different elapsed times. Pick one statustid per query.
- uddstat values 1-4 are mutually exclusive, no total row. Sum all four (with uddannelse='TOT') to get full cohort size.
- afgreg=0 is national total, not in dim.nuts. Regions 81–85 join to dim.nuts at niveau=1. No sub-regional geography available.
- To get a simple cohort count: filter afgklas='TOT', uddannelse='TOT', koen='10', herkomst='0', afgreg='0', pick one statustid and tid='2024-01-01'.
- herkomst 10+20+30+40 sum to herkomst='0'. koen M+K sum to koen='10'. afgklas H2010+H2020+H2030 sum to TOT.
- Map: /geo/regioner.parquet — merge on afgreg=dim_kode. Exclude afgreg=0.