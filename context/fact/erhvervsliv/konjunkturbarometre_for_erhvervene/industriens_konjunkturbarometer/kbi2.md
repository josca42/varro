table: fact.kbi2
description: Vurderinger i industrien efter branche (DB07), indikator, bedømmelse og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- indikator: values [FÆR=Færdigvarelagre, SAM=Samlet ordrebeholdning, EKS=Eksportordrebeholdning]
- bedommelse: values [MN2=For små eller ikke tilstrækkelig, NOR2=Passende eller tilstrækkelig, SNO2=For store eller mere end tilstrækkelig, NET=Nettotal]
- tid: date range 2005-01-01 to 2025-10-01
dim docs: /dim/db.md

notes:
- branche07 does NOT join dim.db — uses DB07 letter codes (B, BC, C, CA–CM, S1–S4), not dim.db's numeric codes. Use ColumnValues("kbi2", "branche07") for labels. Same hierarchy as kbi1: BC=aggregate, C=total manufacturing, CA–CM=sub-industries, S1–S4=MIG groups.
- bedommelse=NET = SNO2 − MN2. For orders (SAM, EKS): negative NET signals insufficient order backlog (weak demand). For inventory (FÆR): positive NET signals excess stock. Do not sum across bedommelse values.
- indikator is a measurement selector — each branche07×tid combination appears 3 times (FÆR, SAM, EKS). Always filter indikator to avoid triple-counting.
- Sample: SELECT tid, indhold FROM fact.kbi2 WHERE branche07='C' AND indikator='EKS' AND bedommelse='NET' ORDER BY tid;