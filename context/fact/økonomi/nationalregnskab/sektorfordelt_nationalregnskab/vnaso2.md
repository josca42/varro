table: fact.vnaso2
description: Versionstabel NASO2 - 2.1.2-3.1 Indkomst, forbrug, opsparing og investering (oversigtstabel) efter version, transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- version: values [V2024_JUN=Juniversion 2021-2024, V2024_MAR=Martsversion 2024, V2023_JUN=Juniversion 1966-2023 (Hovedrevision 2024), V2023_MAR=Martsversion 2023, V2022_SEP=Septemberversion 2021-2022 ... V2014_NOV=Novemberversion 2012-2014, V2014_JUN=Juniversion 2014, V2014_MAR=Martsversion 2014, V2013_NOV=Novemberversion 2011-2013, V2013_SEP=Septemberversion 1966-2013 (Hovedrevision 2014)]
- transakt: values [B2A3GK=B.2g+B.3g Bruttooverskud af produktionen og blandet indkomst, D1K=D.1 Modtaget aflønning af ansatte, D2K=D.2 Modtaget produktions- og importskatter, D3K=D.3 Betalt subsidier, D4K=D.4 Modtaget formueindkomst ... P51C5D=P.51c Forbrug af fast realkapital, P52D=P.52 Lagerforøgelser, P53D=P.53 Anskaffelser minus afhændelser af værdigenstande, NPD=NP Anskaffelser af ikke-finansielle ikke-producerede aktiver, netto, B9D=B.9 Fordringserhvervelse, netto]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- Version table of naso2. Same structure but adds a version dimension. Always filter WHERE version = 'V2024_JUN' (or the latest) unless comparing revisions. For current data use naso2.
- sektor: same dot-dropped ESA codes as naso2. Join dim.esa with REPLACE(d.kode, '.', ''). 9 sectors. Use ColumnValues("vnaso2", "sektor") for labels.
- Covers income, consumption, savings and investment (chapter 2.1.2–3.1) across multiple publication versions.