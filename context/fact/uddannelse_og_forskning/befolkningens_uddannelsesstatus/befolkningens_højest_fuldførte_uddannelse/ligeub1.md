table: fact.ligeub1
description: Befolkningens højeste fuldførte uddannelse (15-69 år) efter bopælsområde, herkomst, højest fuldførte uddannelse, alder, køn og tid
measure: indhold (unit Antal)
columns:
- bopomr: join dim.nuts on bopomr=kode; levels [1, 3]
- herkomst: join dim.herkomst on herkomst=kode [approx]
- hfudd: join dim.ddu_udd on hfudd=kode [approx: H prefix needs stripping]
- alder: values [TOT=Alder i alt, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2005-01-01 to 2024-01-01
dim docs: /dim/ddu_udd.md, /dim/herkomst.md, /dim/nuts.md

notes:
- bopomr joins dim.nuts (both smallint). 0=national total (not in dim), niveau 1=5 regioner (81-85), niveau 3=99 kommuner (101-860, including Christiansø=411). Filter d.niveau to pick granularity.
- herkomst does NOT join dim.herkomst — completely different coding. Inline values: 0=I alt, 10=Dansk oprindelse, 21=Indvandrere i alt, 24=Indvandrere vestlige, 25=Indvandrere ikke-vestlige, 31=Efterkommere i alt, 34=Efterkommere vestlige, 35=Efterkommere ikke-vestlige. Hierarchical: 0=10+21+31, 21=24+25, 31=34+35. Filter to one level to avoid double-counting.
- hfudd does NOT join dim.ddu_udd — inline H10-H90 + TOT (11 codes, no subcodes). Use directly.
- This table goes back to 2005, the longest count-based series in this subject. Use for herkomst breakdowns not available in other tables.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.