table: fact.aku111m
description: Arbejdsmarkedstilknytning efter sæsonkorrigering, beskæftigelsesstatus og tid
measure: indhold (unit Pct.)
columns:
- saeson: values [10=Sæsonkorrigeret, 11=Ikke sæsonkorrigeret]
- beskstatus: values [BFK=Beskæftigelsesfrekvens, LPCT=AKU-ledighedsprocent, EFK=Erhvervsfrekvens]
- tid: date range 2008-01-01 to 2025-09-01

notes:
- saeson MUST be filtered to one value: 10=Sæsonkorrigeret or 11=Ikke sæsonkorrigeret. Both exist for every beskstatus/tid combination — mixing them doubles every value.
- This is the only monthly AKU table (tid steps monthly). Quarterly equivalents are aku100k/aku101k/aku111k. Use this table when monthly granularity or seasonal adjustment comparison is needed.
- beskstatus values are rates (Pct.), not counts. BFK, LPCT, and EFK are three independent rates — never sum.