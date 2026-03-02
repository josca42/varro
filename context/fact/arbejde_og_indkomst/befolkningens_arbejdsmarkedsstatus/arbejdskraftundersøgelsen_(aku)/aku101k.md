table: fact.aku101k
description: Sæsonkorrigeret arbejdsmarkedstilknytning (procent) efter beskæftigelsesstatus og tid
measure: indhold (unit Pct.)
columns:
- beskstatus: values [BFK=Beskæftigelsesfrekvens, LPCT=AKU-ledighedsprocent, EFK=Erhvervsfrekvens]
- tid: date range 2008-01-01 to 2025-04-01

notes:
- BFK, LPCT, and EFK are three independent rates — never sum or average across beskstatus. Filter to the rate you need: BFK for employment rate, LPCT for unemployment rate, EFK for labour force participation rate.
- Seasonally adjusted quarterly series. Compare to aku111m for monthly resolution or aku111k for unadjusted quarterly with age/gender breakdown.