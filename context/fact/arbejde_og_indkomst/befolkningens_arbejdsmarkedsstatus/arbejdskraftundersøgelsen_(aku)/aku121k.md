table: fact.aku121k
description: Arbejdsmarkedstilknytning (procent) efter beskæftigelsesstatus, område og tid
measure: indhold (unit Pct.)
columns:
- beskstatus: values [BFK=Beskæftigelsesfrekvens, LPCT=AKU-ledighedsprocent, EFK=Erhvervsfrekvens]
- omrade: join dim.nuts on omrade=kode; levels [1]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 1 only (5 regioner, kode 81-85). Code 0 = national total, not in dim. Filter omrade != '0' for region-level analysis.
- BFK=Beskæftigelsesfrekvens, LPCT=AKU-ledighedsprocent, EFK=Erhvervsfrekvens are three different rates — never sum across beskstatus. Select the one rate you need.
- Quarterly data (same time coverage as aku120k). For the counts in thousands, use aku120k instead.
- Map: /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade='0'.