table: fact.fam133n
description: Børn 1. januar efter område, husstandstype, antal personer i husstand , antal børn i husstand, køn, alder og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- hustyp: values [M=Enlige mænd, K=Enlige kvinder, PAR=Ægtepar, PA=Et par i øvrigt, IHB=Ikke hjemmeboende børn under 18 år, AH=Andre husstande bestående af flere familier]
- antpersh: values [1=1 person, 2=2 personer, 3=3 personer, 4=4 personer, 5=5 personer, 6-=6 personer og derover]
- antbornh: values [0=0 børn, 1=1 barn, 2=2 børn, 3=3 børn, 4=4 børn, 5-=5 børn og derover]
- kon: values [D=Drenge, P=Piger]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år]
- tid: date range 1986-01-01 to 2025-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 3 only (99 kommuner). No national total row — to get a national count, SUM across all omrade values.
- No total rows for any dimension. Must sum across all hustyp/antpersh/antbornh/kon/alder values you want.
- hustyp=IHB ("Ikke hjemmeboende børn under 18 år") covers children not living in a household (institutions, foster care). Exclude IHB when counting children in ordinary households.
- hustyp=AH ("Andre husstande bestående af flere familier") covers complex multi-family households.
- This table uses husstandstype (household type) rather than familietype (family type) as in fam111n. A household can span multiple families. alder covers 0–24, kon is D/P only.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. No national total row exists in this table.
