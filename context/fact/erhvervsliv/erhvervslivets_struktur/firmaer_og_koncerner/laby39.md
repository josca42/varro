table: fact.laby39
description: Erhvervsdemografi efter kommunegruppe, årsværk og tid
measure: indhold (unit Antal)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode [approx]; levels [1]
- fui11: values [0=Overlevede virksomheder i alt, 1=Ingen ændring eller negativ vækst, 3=Voksede med mindre end 3 årsværk, 4=Voksede med 3-6 årsværk, 2=Voksede med mindst 6 årsværk]
- tid: date range 2010 to 2024
dim docs: /dim/kommunegrupper.md

notes:
- komgrp same as laby38b: joins dim.kommunegrupper niveau 1. Unmatched: 0 = "Hele landet", 995 = "Uoplyst kommunegruppe".
- fui11 is a growth-category column: 0=Overlevede virksomheder i alt, 1=Ingen ændring/negativ vækst, 2=Voksede med mindst 6 årsværk, 3=Voksede med mindre end 3 årsværk, 4=Voksede med 3–6 årsværk. Values 1–4 are sub-categories of value 0 (they sum to it), so never sum across all fui11 values. Use fui11=0 for the total count of surviving firms.
- Longest time range in this subject: 2010–2024. Use for trend questions about firm survival and growth over time.