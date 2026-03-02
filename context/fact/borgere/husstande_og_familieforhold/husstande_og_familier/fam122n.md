table: fact.fam122n
description: Voksne 1. januar efter område, husstandstype, antal personer i husstand , antal børn i husstand, køn, alder og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- hustyp: values [M=Enlige mænd, K=Enlige kvinder, PAR=Ægtepar, PA=Et par i øvrigt, AH=Andre husstande bestående af flere familier]
- antpersh: values [1=1 person, 2=2 personer, 3=3 personer, 4=4 personer, 5=5 personer, 6-=6 personer og derover]
- antbornh: values [0=0 børn, 1=1 barn, 2=2 børn, 3=3 børn, 4=4 børn, 5-=5 børn og derover]
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [9915=Under 15 år, 15=15 år, 16=16 år, 17=17 år, 18=18 år ... 96=96 år, 97=97 år, 98=98 år, 99=99 år, 100-=100 år og derover]
- tid: date range 1986-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 3 only (99 kommuner). No regional or national aggregates — to get national totals, SUM across all kommuner. Use ColumnValues("nuts", "titel", for_table="fam122n") to see available kommuner.
- NO total codes in any dimension: hustyp, antpersh, antbornh, kon, and alder are all fully specific. Every non-target dimension must be either filtered to a specific value or explicitly aggregated (SUM or GROUP BY).
- alder: individual ages 15–100+. Special code 9915 = "Under 15 år" covers ages below 15. No age-group buckets — use CASE expressions in SQL to aggregate into age groups.
- This table is extremely dense (7 dimensions × 99 kommuner × 40 years). Always filter tid, omrade, and at least a few other dimensions to avoid pulling millions of rows. A typical query: one kommune, one year, one hustyp, then GROUP BY alder.
- hustyp IHB is absent here (unlike fam55n) — this table covers adults in households, not the IHB children category.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.