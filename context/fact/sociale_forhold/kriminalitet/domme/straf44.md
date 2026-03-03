table: fact.straf44
description: Strafferetlige afgørelser efter område, overtrædelsens art, afgørelsestype, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- overtraed: values [TOT=Overtrædelsens art i alt, 1=Straffelov i alt, 1000=Uoplyst straffelov, 11=Seksualforbrydelser i alt, 1110=Blodskam mv. ... 3845=Love vedrørende forsvaret o.l., 3850=Love vedrørende offentlige forsyninger, 3855=Love vedrørende spil, bevilling, næring, 3865=Særlovgivning i øvrigt, 3870=Uoplyst særlovgivning]
- afgorelse: values [000=Afgørelsestype i alt, 1=1 Dom til frihedsstraf, 11=11 Ubetinget frihedsstraf, 111=111 Ubetinget dom alene, 112=112 Delvis betinget dom ... 514=514 Frifindelse, 515=515 Straf bortfaldet, 516=516 Militær straf, 517=517 Ingen tillægsstraf (§89), 518=518 Anden afgørelse i øvrigt]
- alder: values [TOT=Alder i alt, UA=Uoplyst alder, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70-79=70-79 år, 80-=80 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder, VIRKSOMHEDER=Virksomheder]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts but only at niveaux 1 (5 regioner, koder 81-85) and 3 (99 kommuner). No niveau 2 (landsdele). omrade='0' = I alt (whole country, not in nuts), omrade='998' = Uoplyst. Always filter omrade != '0' and omrade != '998' when joining, or handle them as inline aggregates.
- Use ColumnValues("nuts", "titel", for_table="straf44") to browse the 104 joinable regions/kommuner.
- overtraed and afgorelse are both inline hierarchical (same as straf40) — filter to one level in each to avoid double-counting.
- kon includes VIRKSOMHEDER; filter kon='TOT' for total persons+companies or kon IN ('M','K') for persons only.
- Most complete sentence table with regional breakdown. Only from 2007 (straf40 goes to 1980 without region).
- To get sentences by region: JOIN dim.nuts d ON f.omrade = d.kode AND d.niveau = 1, AND WHERE overtraed='TOT' AND afgorelse='000' AND alder='TOT' AND kon='TOT'.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade IN ('0', '998'). Kommune data can also be aggregated to 12 politikredse via dim.politikredse (niveau 2 koder match dim.nuts niveau 3; parent_kode → politikredsgrænser in /geo/politikredse.parquet).