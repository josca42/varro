table: fact.laby06
description: Gennemsnitlig disponibel indkomst efter kommunegruppe, alder og tid
measure: indhold (unit Kr.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- alder: values [00=I alt, 15-19=15-19 år, 20-29=20-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70-79=70-79 år, 80-00=80 år og derover]
- tid: date range 2004-01-01 to 2023-01-01
dim docs: /dim/kommunegrupper.md
notes:
- komgrp joins dim.kommunegrupper at BOTH niveau=1 (5 kommunegruppe-types) and niveau=2 (individual kommuner). Filter to one niveau to avoid mixing levels: WHERE d.niveau = 1 for groups, d.niveau = 2 for individual kommuner.
- alder includes 00='I alt' (total) plus 8 age bands (15-19 through 80-00). Code '00' is the total. Do not mix 00 with individual bands. Note: children under 15 are excluded; this is income for persons 15+.
- indhold is average disposable income in Kr. — not equivalised (no household equivalence adjustment). See ifor32 for equivalised income by decil.
- Covers 2004–2023. See ifor32/ifor35 for data back to 1987 (different breakdown: decil by kommune, no kommunegruppe).
