table: fact.fam100n
description: Voksne 1. januar efter område, familietype, antal personer i familien, antal børn i familien, køn, alder og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- famtyp: values [M=Enlige mænd, K=Enlige kvinder, PARF=Ægtepar med forskelligt køn, PARS=Ægtepar med samme køn, RP=Registreret partnerskab, SL=Samlevende par, SB=Samboende par]
- antpf: values [1=1 person, 2=2 personer, 3=3 personer, 4=4 personer, 5=5 personer, 6-=6 personer og derover]
- antbrnf: values [0=0 børn, 1=1 barn, 2=2 børn, 3=3 børn, 4=4 børn, 5-=5 børn og derover]
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [9915=Under 15 år, 15=15 år, 16=16 år, 17=17 år, 18=18 år ... 96=96 år, 97=97 år, 98=98 år, 99=99 år, 100-=100 år og derover]
- tid: date range 1986-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 3 only (99 kommuner). No regional or national aggregates — SUM across kommuner for broader geography. Same omrade structure as fam122n.
- NO total codes in any dimension: famtyp, antpf, antbrnf, kon, and alder are all fully specific. 7 dimensions, all requiring explicit filter or GROUP BY.
- alder: individual ages 15–100+. Special code 9915 = "Under 15 år". No age-group buckets — build with CASE. Same pattern as fam122n.
- famtyp here is family-based (PARF, PARS, RP, SL, SB, M, K) — same 7 types as fam44n minus IHB. Note IHB is absent (this table counts adults in families).
- This is the family equivalent of fam122n. Use fam100n when you need adult demographics (age/sex) within family types; use fam44n when you just need family counts by size/type without demographic breakdown.
- Very large table — always filter tid and omrade first. A typical useful query: one kommune, one year, one famtyp, GROUP BY alder or kon.
- Map: /geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.