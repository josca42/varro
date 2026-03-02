table: fact.bebrit02
description: Seneste anvendelse af internet - procent af befolkningen (16-74 år) efter type, seneste anvendelse og tid
measure: indhold (unit Pct.)
columns:
- type: values [10=I alt, 40=Alder: 16-19 år, 50=Alder: 20-39 år, 60=Alder: 40-59 år, 70=Alder: 60-74 år ... 210=Indkomst: 0-49.999 kr., 220=Indkomst: 50.000-99.999 kr., 230=Indkomst: 100.000-199.999 kr., 240=Indkomst: 200.000-299.999 kr., 250=Indkomst: 300.000 og derover]
- senanv: values [10=Inden for de sidste 3 måneder., 20=Indenfor det sidste år (men ikke de sidste 3 måneder)., 30=For mere end et år siden., 40=Aldrig brugt internettet]
- tid: date range 2008-01-01 to 2025-01-01

notes:
- type is a demographic selector: type='10' = national total (alle 16-74 år). Other values are sub-groups (alder, køn, beskæftigelse, uddannelse, indkomst). Never sum across type values — they are mutually exclusive demographic segments. Always filter to one type or use '10' for the overall figure.
- senanv categories are mutually exclusive recency buckets. No "I alt" row for senanv. To get "has used internet in the past year", filter senanv IN ('10','20') (within 3 months + 3-12 months ago). senanv='40' means never used internet.
- All values are percentages of the 16-74 year old population in that demographic group.