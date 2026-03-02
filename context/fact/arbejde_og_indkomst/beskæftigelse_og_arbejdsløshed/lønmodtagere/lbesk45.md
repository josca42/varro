table: fact.lbesk45
description: Lønmodtagere efter enhed, bopælslandsdel, køn, herkomst og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- boplandk: join dim.nuts on boplandk=kode [approx]; levels [1, 2]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder, UDK=Uoplyst køn, uden bopæl i Danmark]
- herkomst: join dim.herkomst on herkomst=kode::text [approx]; levels [1]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/herkomst.md, /dim/nuts.md
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- boplandk joins dim.nuts correctly (89% match). Unmatched: 0=Hele landet, 950=Uden for Danmark. Contains both regioner (81–85) and landsdele (1–11) — filter d.niveau to pick one level.
- WARNING: dim.herkomst join is mostly broken. herkomst uses: 1=Dansk oprindelse, 24=Indvandrere vestlige, 25=Indvandrere ikke-vestlige, 34=Efterkommere vestlige, 35=Efterkommere ikke-vestlige, TOT=I alt, UDK=Uoplyst. Treat as inline — see lbesk43 notes.
- To get breakdown by region AND herkomst: filter tal, then cross boplandk with herkomst (exclude TOT and UDK in both unless summarising).
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on boplandk=dim_kode. Exclude boplandk IN (0, 950).
