table: fact.laby03
description: Befolkningen i procent af alle i samme alder efter kommunegruppe, alder og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- alder: values [IALT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/kommunegrupper.md

notes:
- indhold = % of all Danes of this age who live in this kommunegruppe (i.e., the geographic distribution of each age cohort). Values sum to 100 across komgrp for each alder. Do NOT sum across alder.
- Different semantics from laby02: laby02 asks "what is the age profile of each group?"; laby03 asks "where do each age group live?"
- komgrp=0 (national total) present but not in dim. niveau=1 codes (1–5) only.
- Example use: find which kommunegruppe has the highest share of 30-year-olds vs 65-year-olds.