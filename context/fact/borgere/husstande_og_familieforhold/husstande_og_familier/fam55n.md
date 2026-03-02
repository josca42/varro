table: fact.fam55n
description: Husstande 1. januar efter område, husstandstype, husstandsstørrelse, antal børn i husstand og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- hustyp: values [M=Enlige mænd, K=Enlige kvinder, PAR=Ægtepar, PA=Et par i øvrigt, IHB=Ikke hjemmeboende børn under 18 år, AH=Andre husstande bestående af flere familier]
- husstor: values [1=1 person, 2=2 personer, 3=3 personer, 4=4 personer, 5=5 personer, 6=6 personer, 7=7 personer, 8+=8 og derover]
- antbornh: values [0=0 børn, 1=1 barn, 2=2 børn, 3=3 børn, 4=4 børn, 5-=5 børn og derover]
- tid: date range 1986-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and 3 (99 kommuner). omrade='0' is the national total (hele landet) — not in dim.nuts, filter directly as WHERE omrade='0'. Use ColumnValues("nuts", "titel", for_table="fam55n") to see all 104 region/kommune codes.
- hustyp, husstor, and antbornh have NO total/aggregate codes. Every row is a specific combination. To get total household count for an area, SUM across all hustyp × husstor × antbornh values — they are non-overlapping categories. Never filter to a single value without intent.
- IHB (Ikke hjemmeboende børn under 18 år) is a tiny category (~1,300 nationally in 2025). It represents children under 18 who head their own household, not living with parents. Often appropriate to exclude when counting family households.
- Example: total households in a region — JOIN dim.nuts d ON omrade=d.kode WHERE d.niveau=1, then GROUP BY d.titel and SUM(indhold) across all hustyp/husstor/antbornh.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.