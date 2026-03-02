table: fact.brn9
description: Børn efter område, alder, familietype, mor status, far status og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år, 5=5 år, 6=6 år, 7=7 år, 8=8 år, 9=9 år, 10=10 år, 11=11 år, 12=12 år, 13=13 år, 14=14 år, 15=15 år, 16=16 år, 17=17 år]
- famtyp: values [0=Udeboende, 1=Begge forældre, 2=Enlig mor, 3=Mor og partner, 4=Enlig far, 5=Far og partner]
- morstat: values [HM=Har mor, MD=Mor død, UK=Uoplyst mor]
- farstat: values [HF=Har far, FD=Far død, UM=Uoplyst far]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/nuts.md
notes:
- omrade has three groups: '0' (national total, not in dim.nuts — use omrade='0' directly), niveau 1 (5 regioner), niveau 3 (99 kommuner). Filter to one niveau when joining dim.nuts.
- morstat and farstat are independent dimensions, not mutually exclusive. Filter both to target a specific parental status (e.g. morstat='HM' AND farstat='HF' for children with both parents alive).
- No total rows for any dimension. No alder aggregate — alder covers 0–17 only.
- Compare with brn10 for finer death-timing detail (DIA=died this year vs DT=died earlier) and extended age range (0–29).
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
