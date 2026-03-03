table: fact.fly33
description: Flytninger inden for kommuner efter område, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 95=95 år, 96=96 år, 97=97 år, 98=98 år, 99-=99 år og derover]
- kon: values [M=Mænd, K=Kvinder]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 3 (99 kommuner). Perfect 99/99 match. Use `JOIN dim.nuts d ON f.omrade = d.kode AND d.niveau = 3`.
- No total rows: alder is 0–99 only, kon is M/K only. Summing all rows for a kommune gives the true intra-municipal move count.
- This table covers only moves *within* a municipality (flytning der ikke krydser kommunegrænse). For inter-municipal moves use fly66; for all moves nationally use fly.
- ColumnValues("nuts", "titel", for_table="fly33") returns the 99 kommuner present in this table.
- Map: /geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.