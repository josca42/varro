table: fact.handbu01
description: Handicapindsatser til børn og unge mellem 0-17 år efter kommune, indsats, køn og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [3]
- indsatser: values [100=Handicapindsatser i alt, 110=Børn og unge der modtager handicapindsatser i alt]
- kon: values [0=I alt, D=Drenge, P=Piger, 9=Uoplyst køn]
- tid: date range 2022-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- kommunedk joins dim.nuts at niveau=3 (95 kommuner). kommunedk=0 is a national total row not in dim.nuts — use it for Denmark-wide figures rather than summing all kommuner.
- indsatser has exactly 2 values: 100=Handicapindsatser i alt (total number of interventions) and 110=Børn og unge der modtager handicapindsatser i alt (unique children). 100 > 110 because one child can receive multiple interventions. Never sum 100+110 — pick one. Use 110 when you want "how many children".
- kon=0 is "I alt" — do not sum all kon values (0+D+P+9) as that would double-count. Filter to kon=0 for totals, or SUM over D+P+9 separately.
- Map: context/geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.
