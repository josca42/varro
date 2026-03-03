table: fact.fam111n
description: Børn 1. januar efter område, familietype, antal personer i familien, antal børn i familien, køn, alder og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- famtyp: values [M=Enlige mænd, K=Enlige kvinder, PARF=Ægtepar med forskelligt køn, PARS=Ægtepar med samme køn, RP=Registreret partnerskab, SL=Samlevende par, SB=Samboende par, IHB=Ikke hjemmeboende børn under 18 år]
- antpf: values [1=1 person, 2=2 personer, 3=3 personer, 4=4 personer, 5=5 personer, 6-=6 personer og derover]
- antbrnf: values [0=0 børn, 1=1 barn, 2=2 børn, 3=3 børn, 4=4 børn, 5-=5 børn og derover]
- kon: values [D=Drenge, P=Piger]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år]
- tid: date range 1986-01-01 to 2025-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 3 only (99 kommuner). No national total row — to get a national count, SUM across all omrade values.
- No total rows exist for any dimension (no IALT/TOT). There is no shortcut to get all children in a region; you must either group by or sum across all alder/kon/famtyp/antpf/antbrnf values.
- famtyp=IHB ("Ikke hjemmeboende børn under 18 år") covers children in institutions, foster care, etc. Not included in any other famtyp category. Exclude IHB when counting children living in family homes.
- alder covers 0–24 (older than most other børn tables which stop at 17). kon is D/P only — no gender total.
- Map: /geo/kommuner.parquet — merge on omrade=dim_kode. No national total row exists in this table.
