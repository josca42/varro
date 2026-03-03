table: fact.kfred2
description: Fredede fortidsminder efter område, anlægskategori og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- ankat: values [30=Erhverv og produktion, 31=Begravelse, 32=Tro og tradition, 33=Mærkesten, 34=Transport, 35=Forsvar, 36=Bebyggelse, 37=Social og samfund]
- tid: date range 2010-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau=1 only (5 regioner: 81–85). Code 0 = landstal (national total) — not in dim.
- ankat has 7 categories (Erhverv, Begravelse, Tro, Mærkesten, Transport, Forsvar, Bebyggelse, Social) — there is no "all categories" total row. Sum across all ankat values to get total fortidsminder per region.
- Sample: fortidsminder by category nationally in 2024: SELECT f.ankat, f.indhold FROM fact.kfred2 f WHERE f.omrade='0' AND f.tid='2024-01-01' ORDER BY f.indhold DESC
- Map: /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.