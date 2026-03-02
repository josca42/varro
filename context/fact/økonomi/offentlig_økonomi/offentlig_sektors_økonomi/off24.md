table: fact.off24
description: Offentlig forvaltning og service, forbrugsudgift efter funktion samt individuel og kollektiv andel efter funktion, forbrugsgruppe og tid
measure: indhold (unit Mio. kr.)
columns:
- funktion: join dim.cofog on funktion=kode::text [approx]; levels [1]
- konsumgrp: values [200=Individuelt offentligt forbrug, 300=Kollektivt offentligt forbrug, 400=Offentligt forbrug i alt]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/cofog.md

notes:
- funktion joins dim.cofog directly for codes 1–10 (niveau=1 COFOG categories). TOT is an aggregate not in dim — use funktion='TOT' for the grand total across all functions, or exclude it and sum the 10 COFOG groups yourself. Use ColumnValues("cofog", "titel", for_table="off24") to see the 10 available categories.
- konsumgrp is a measurement selector — every funktion×tid row appears 3 times: 200=Individuelt forbrug, 300=Kollektivt forbrug, 400=Offentligt forbrug i alt. Always filter to exactly one konsumgrp value. Forgetting this triples all sums. For totals, use 400; for the individual/collective split, use 200 and 300 separately.