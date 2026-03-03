table: fact.paaroe01
description: Gennemsnitsafstand (km) til 0-24-åriges bedsteforældre 1. januar efter relationstype, hovedpersonens bopæl, hovedpersonens alder og tid
measure: indhold (unit Km)
columns:
- relationtyp: values [TAET=Afstand til den relation, der bor tættest på hovedpersonen, LANG=Afstand til den relation, der bor længst fra hovedpersonen]
- hovedbopael: join dim.nuts on hovedbopael=kode; levels [1, 3]
- hoald: values [9924=0-24 år i alt, 9817=0-17 år i alt, 0=0 år, 1=1 år, 2=2 år ... 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år]
- tid: date range 2024-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- relationtyp is a measurement selector: TAET = distance to the nearest grandparent, LANG = distance to the farthest. Rows are exactly doubled. Always filter to one value.
- hoald has 0–24 individual ages plus two aggregates: 9924 (0–24 i alt) and 9817 (0–17 i alt). Don't mix individual ages with aggregates.
- hoofdbopael joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (99 kommuner). Code 0 is the national total and does not join. Filter WHERE d.niveau = 1 or d.niveau = 3 to pick granularity; mixing both double-counts.
- Only one year of data (2024). No time-series analysis is possible.
- Sample query — average distance to nearest grandparent by region (kommuner): SELECT d.titel, AVG(f.indhold) FROM fact.paaroe01 f JOIN dim.nuts d ON f.hoofdbopael = d.kode WHERE f.relationtyp = 'TAET' AND d.niveau = 3 AND f.hoald = 9924 GROUP BY d.titel;
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on hoofdbopael=dim_kode. Exclude hoofdbopael=0.