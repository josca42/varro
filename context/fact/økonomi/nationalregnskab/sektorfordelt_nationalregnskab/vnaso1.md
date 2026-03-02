table: fact.vnaso1
description: Versionstabel NASO1 - Produktion, BVT og indkomstdannelse (oversigtstabel) efter version, transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- version: values [V2024_JUN=Juniversion 2021-2024, V2024_MAR=Martsversion 2024, V2023_JUN=Juniversion 1966-2023 (Hovedrevision 2024), V2023_MAR=Martsversion 2023, V2022_JUN=Juniversion 2020-2022 ... V2014_NOV=Novemberversion 2012-2014, V2014_JUN=Juniversion 2014, V2014_MAR=Martsversion 2014, V2013_NOV=Novemberversion 2011-2013, V2013_SEP=Septemberversion 1966-2013 (Hovedrevision 2014)]
- transakt: values [P1K=P.1 Produktion, P11A12A131K=P.11+P.12+P.131 Markedsmæssig produktion, produktion til eget brug samt betaling for ikke-markedsmæssig produktion, P7K=P.7 Import af varer og tjenester, P71K=P.71 Import af varer, P72K=P.72 Import af tjenester ... P51CD=P.51c Forbrug af fast realkapital, B2A3ND=B.2n+B.3n Nettooverskud af produktion og blandet indkomst, B2ND=B.2n Nettooverskud af produktion, B3ND=B.3n Blandet nettoindkomst, B1ND=B.1n Nettoværditilvækst]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- Version table of naso1. Same structure but adds a version dimension. Always filter WHERE version = 'V2024_JUN' (or the latest available) unless explicitly comparing revisions across publication releases.
- sektor: same dot-dropped ESA codes as naso1. Join dim.esa with REPLACE(d.kode, '.', ''). 9 sectors including S14, S15 individually. Use ColumnValues("vnaso1", "sektor") for labels.
- Covers the same transakt codes as naso1 (chapter 1-2.1.1). For current data use naso1 instead — vnaso1 is for revision analysis only.