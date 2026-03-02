table: fact.dnudpriv
description: Udlånsundersøgelse, kreditvilkår for private (Nettotal) efter institutgruppe, spørgsmål, periode og tid
measure: indhold (unit -)
columns:
- instituttype: values [M=I alt, P=Pengeinstitutter, K=Realkreditinstitutter]
- sporg: values [10=1: Ændring i kreditstandarder, 2A=2a: kreditstandarder - finansieringsomkostninger, 2B=2b: kreditstandarder - konkurrence, 2C=2c: kreditstandarder - risikoopfattelse, 2D=2d: kreditstandarder - risikovillighed, 3A=3a: Betingelser - pris, 3B=3b: Betingelser - krav til sikkerhedsstillelse, 3C=3c: Betingelser - andre betingelser og vilkår, 4E=4e: Efterspørgsel efter lån - eksisterende kunder, 4N=4n: Efterspørgsel efter lån - nye kunder, 50=5: Andel af nedskrivninger/tab]
- tiden: values [I=Dette kvartal, K=Kommende kvartal, A=Seneste år]
- tid: date range 2008-10-01 to 2025-07-01

notes:
- indhold is a "Nettotal" (net balance statistic): share of institutions reporting tightening minus share reporting loosening/easing. Range roughly -80 to +80 in practice. Positive = net tightening; negative = net easing. Not a percentage of loans or borrowers.
- sporg contains questions from different survey sections: questions 1-3 about credit supply/conditions; questions 4 (4E, 4N) about demand; question 5 about write-downs. Never sum or average across sporg values.
- tiden selects the reporting horizon: I=dette kvartal (current, the primary use), K=kommende kvartal (forward-looking expectation), A=seneste år (past year). Always filter to one value.
- instituttype: M=i alt (total), P=pengeinstitutter, K=realkreditinstitutter. For a combined view use M.
- For current credit conditions for private borrowers: sporg='10' (ændring i kreditstandarder), instituttype='M', tiden='I'.