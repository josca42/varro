table: fact.musik3
description: Indtægter ved salg af musik efter rettighedsejertype, område og tid
measure: indhold (unit Kr.)
columns:
- rettighed: values [10=Uoplyst, 6=Autor, 7=Forlag, 8=Søsterselskab, 9=Arving]
- omrade: join dim.nuts on omrade=kode [approx]; levels [1]
- tid: date range 2012-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau=1 (5 regioner: 81–85). omrade=99 is not in dim.nuts — it represents income not attributable to any Danish region (foreign/centrally-held rights).
- omrade=99 is NOT the national total. Regions + omrade=99 are additive: to get total revenue by rettighed, SUM all omrade values.
- rettighed 8 (Søsterselskab), 9 (Arving), and 10 (Uoplyst) only appear under omrade=99 — they have NO regional breakdown. A regional filter (omrade BETWEEN 81 AND 85) will exclude these types entirely.
- rettighed 6 (Autor) and 7 (Forlag) have both regional and omrade=99 data.
- For total income by rettighed: SUM across all omrade. For regional breakdown: filter omrade IN (81,82,83,84,85) knowing rettighed 8/9/10 will be absent.
- Map: /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Filter omrade IN (81,82,83,84,85); note rettighed 8/9/10 will be absent from the map.