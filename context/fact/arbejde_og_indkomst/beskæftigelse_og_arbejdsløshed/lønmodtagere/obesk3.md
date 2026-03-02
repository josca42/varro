table: fact.obesk3
description: Offentligt fuldtidsbeskæftigede lønmodtagere (sæsonkorrigeret) efter sektor og tid
measure: indhold (unit Antal)
columns:
- sektor: join dim.esr_sekt on sektor::text=kode
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/esr_sekt.md
notes:
- Sæsonkorrigeret version of obesk2. Same structure — see obesk2 notes. dim.esr_sekt join is broken; treat sektor as inline.
- SCOPE: Only public sector full-time equivalent employees. No tal column.
