table: fact.naio3
description: Input-output tabel. Primære input fordelt efter anvendelse og prisenhed efter tilgangstype, anvendelse, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- tilgang1: values [D214X31=Produktskatter, netto ekskl. told og moms, D211=Moms, D29X39=Andre produktionsskatter, netto, D1=Aflønning af ansatte, B2A3G=Bruttooverskud af produktion og blandet indkomst, PRIMINP=Primære input, i alt]
- anvendelse: join dim.nr_branche on anvendelse=kode [approx]
- prisenhed: values [V=Løbende priser, Y=Foregående års priser]
- tid: date range 1966-01-01 to 2022-01-01
dim docs: /dim/nr_branche.md

notes:
- Primary inputs (wages, taxes, gross surplus) distributed across industries. Use this to answer "how much does industry X pay in wages / taxes / gross surplus?".
- **prisenhed must be filtered** (V=løbende, Y=foregående års priser).
- **tilgang1 must be filtered**: PRIMINP=Primære input i alt (total), D1=Aflønning af ansatte (wages), B2A3G=Bruttooverskud af produktion og blandet indkomst, D211=Moms, D214X31=Produktskatter netto ekskl. told og moms, D29X39=Andre produktionsskatter netto. Filter to PRIMINP for total primary input per industry; filter to D1 for wage cost.
- `anvendelse` = which industry is being measured (the "applying" industry). A-prefixed. Join via `SUBSTRING(f.anvendelse, 2) = d.kode`. Use `d.niveau` to control aggregation level.