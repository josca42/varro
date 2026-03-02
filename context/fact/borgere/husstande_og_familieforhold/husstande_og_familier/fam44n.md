table: fact.fam44n
description: Familier 1. januar efter område, familietype, familiestørrelse, antal børn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- famtyp: values [M=Enlige mænd, K=Enlige kvinder, PARF=Ægtepar med forskelligt køn, PARS=Ægtepar med samme køn, RP=Registreret partnerskab, SL=Samlevende par, SB=Samboende par, IHB=Ikke hjemmeboende børn under 18 år]
- famstor: values [1=1 person, 2=2 personer, 3=3 personer, 4=4 personer, 5=5 personer, 6-=6 personer og derover]
- antborn: values [0=0 børn, 1=1 barn, 2=2 børn, 3=3 børn, 4=4 børn, 5-=5 børn og derover]
- tid: date range 1986-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and 3 (99 kommuner). omrade='0' is the national total — not in dim.nuts. Same omrade structure as fam55n.
- famtyp has 8 values with NO total. Note it distinguishes same-sex marriages (PARS), registered partnerships (RP), and cohabiting pairs (SL=Samlevende, SB=Samboende) — more detailed than fam55n which only has PAR and PA. IHB is present (children not living at home, a small category).
- famstor and antborn have NO total codes. To get total family count, SUM across all famtyp × famstor × antborn combinations.
- Use ColumnValues("nuts", "titel", for_table="fam44n") to see the 104 region/kommune codes.
- Key difference from fam55n: fam44n counts families (familier), fam55n counts households (husstande). A family is a smaller unit (e.g., couple + children); a household can contain multiple families.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.