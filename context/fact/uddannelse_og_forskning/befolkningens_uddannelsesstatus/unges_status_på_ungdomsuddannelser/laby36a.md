table: fact.laby36a
description: 20-åriges ungdomsuddannelser (andel i procent) efter kommunegruppe, uddannelsesstatus og tid
measure: indhold (unit Andel i pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md

notes:
- Values are percentages (Andel i pct.), not counts. Each uddstat value is a share of 20-year-olds in that kommunegruppe. Do NOT sum across uddstat values — they already partition to ~100% (AA_TOTAL=100, FULDFOERT+IGANG+AFBRUDT+INGENREG ≈ 100).
- Limited to 20-year-olds only (unlike laby36 which covers ages 18–25). Use this table to compare "what share of 20-year-olds have completed upper secondary" by kommunegruppe.
- komgrp=0 (national total) is not in dim.kommunegrupper but is present in the fact table — useful as a baseline. A plain JOIN would drop it; query it separately with WHERE komgrp=0 for the national rate.
- Only 2 dimension columns (komgrp, uddstat) — the simplest table in this subject. To read a result directly: WHERE komgrp=1 AND uddstat='FULDFOERT' AND tid='2024-01-01' gives the completion share for Hovedstadskommuner in 2024.