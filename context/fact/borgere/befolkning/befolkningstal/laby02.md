table: fact.laby02
description: Befolkningen i procent af alle i samme kommunegruppe efter kommunegruppe, alder og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- alder: values [IALT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/kommunegrupper.md

notes:
- indhold = % of people in this age group within the same kommunegruppe (i.e., the age distribution within each group). Values are age-distribution percentages — they sum to 100 across alder for each komgrp. Do NOT sum across komgrp.
- komgrp=0 (national total) is present but not in dim.kommunegrupper. Only niveau=1 codes (1–5) plus 0.
- alder has individual ages 0–125 plus IALT. Filter alder='IALT' to get the overall group share (always 100%).
- Compare komgrp across the same alder value to see how age profiles differ between city types (e.g., are Storbykommuner younger than Landkommuner?).