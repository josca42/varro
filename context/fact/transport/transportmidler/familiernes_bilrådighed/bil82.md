table: fact.bil82
description: Familiernes bilrådighed (faktiske tal) efter bestand, familietype, rådighedsmønster og tid
measure: indhold (unit Antal)
columns:
- bestand: values [52=Bestand (E-familier 2008 - ), 72=Bestand (C-familier 2000 -2007)]
- famtyp: values [FAIA=Familier i alt, FAUB=Familier uden børn, FAMB=Familier med børn, PAUB=Par uden børn, PAMB=Par med børn, PAFA=Parfamilier i alt, IHJB=Ikke-hjemmeboende børn, ENIA=Enlige i alt, ENUB=Enlige uden børn, ENMB=Enlige med børn]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10220=Familier med 1 bil i alt, 10230=Familier med personbil, 10240=Familier med firmabil, 10250=Familier med varebil, 10260=Familier med 2 biler i alt, 10270=Familier med 2 personbiler, 10280=Familier med 2 firmabiler, 10290=Familier med 2 varebiler, 10300=Familier med 1 personbil og 1 firmabil, 10310=Familier med 1 personbil og en varebil, 10320=Familier med 1 firmabil og 1 varebil, 10330=Familier med 3 biler i alt, 10340=Familier med flere end 3 biler]
- tid: date range 2000-01-01 to 2025-01-01
notes:
- bestand is a methodology selector, not an additive dimension. 52=E-familier (2008+), 72=C-familier (2000-2007). The two values cover non-overlapping time periods using different family register definitions. Filter to one bestand: use 52 for 2008+ data, 72 for 2000-2007. Never SUM or GROUP across both.
- famtyp has overlapping aggregates: FAIA=all families, PAFA=all couples (subset), ENIA=all singles (subset). PAUB+PAMB+IHJB ≈ PAFA; ENUB+ENMB ≈ ENIA; FAUB+FAMB ≈ FAIA. Pick one granularity level.
- raadmoens is hierarchical — pick one level. 10000=total, 10200=ingen bil, 10210=med bil; never SUM all raadmoens together.
