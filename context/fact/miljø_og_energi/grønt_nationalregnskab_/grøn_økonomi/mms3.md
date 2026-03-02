table: fact.mms3
description: Miljøstøtte efter branche, miljøkategori og tid
measure: indhold (unit Mio. kr.)
columns:
- branche: values [MTOT=I alt, MHUSHOLD=Husholdninger, MANDANV=Andre endelige anvendelser, MV=Brancher i alt, VA=A Landbrug, skovbrug og fiskeri ... V96000=96000 Frisører, vaskerier og andre serviceydelser, V960000=960000 Frisører, vaskerier og andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, V97000=97000 Private husholdninger med ansat medhjælp, V970000=970000 Private husholdninger med ansat medhjælp]
- miljokat: values [SUB05=Miljømotiverede subsidier i alt (1+2+3+4+5), SUB10=1. Forurening i alt, SUB25=2. Energi i alt, SUB45=3. Transport i alt, SUB55=4. Naturforvaltning i alt, SUB75=5. Bistand i alt]
- tid: date range 1995-01-01 to 2024-01-01
notes:
- branche is an inline coded column (no dim join). Aggregate codes: MTOT=I alt, MV=Brancher i alt, MHUSHOLD=Husholdninger, MANDANV=Andre endelige anvendelser. MTOT = MV + MHUSHOLD + MANDANV. Then V-prefixed industry codes (VA=Landbrug, VB=Råstofindvinding, ..., V01000, V010000...) at multiple levels of detail. Use MTOT for the national total. Use ColumnValues("mms3", "branche") to browse all sector codes and avoid double-counting across hierarchy levels.
- miljokat only has 6 values (5 top-level categories + total): SUB05=total, SUB10=Forurening, SUB25=Energi, SUB45=Transport, SUB55=Naturforvaltning, SUB75=Bistand. No sub-category detail unlike mms1.
- This is the only miljøstøtte table with industry breakdown. For finer environmental purpose breakdown without branche: use mms1 or mms2.
