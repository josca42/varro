table: fact.dnuderhv
description: Udlånsundersøgelse, kreditvilkår for erhvervsvirksomheder (Nettotal) efter institutgruppe, branche, spørgsmål, periode og tid
measure: indhold (unit -)
columns:
- instituttype: values [M=I alt, P=Pengeinstitutter, K=Realkreditinstitutter]
- erhverv: values [100=Alle / Ikke-specificeret, SMV=Små og mellemstorevirksomheder (Kun spg. 1, 4e, 4n og 5)]
- sporg: values [10=1: Ændring i kreditstandarder, 2A=2a: kreditstandarder - finansieringsomkostninger, 2B=2b: kreditstandarder - konkurrence, 2C=2c: kreditstandarder - risikoopfattelse, 2D=2d: kreditstandarder - risikovillighed, 3A=3a: Betingelser - pris, 3B=3b: Betingelser - krav til sikkerhedsstillelse, 3C=3c: Betingelser - andre betingelser og vilkår, 4E=4e: Efterspørgsel efter lån - eksisterende kunder, 4N=4n: Efterspørgsel efter lån - nye kunder, 50=5: Andel af nedskrivninger/tab]
- tiden: values [I=Dette kvartal, K=Kommende kvartal, A=Seneste år]
- tid: date range 2008-10-01 to 2025-07-01

notes:
- Same structure and interpretation as dnudpriv but for erhvervsvirksomheder (corporate borrowers).
- indhold is a Nettotal (net share tightening minus easing). Not an amount, not additive.
- erhverv: 100=alle/ikke-specificeret, SMV=small and medium enterprises. SMV is only available for spørgsmål 1, 4E, 4N, and 5. For other questions only erhverv='100' exists.
- sporg, tiden, instituttype: same coding as dnudpriv — see that table's notes.
- For current credit conditions for all business borrowers: sporg='10', erhverv='100', instituttype='M', tiden='I'.