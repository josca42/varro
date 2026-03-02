table: fact.bil89
description: Familiernes bilrådighed (andele og fordelinger) efter enhed, boligforhold, rådighedsmønster og tid
measure: indhold (unit Pct.)
columns:
- maengde4: values [50=Procentfordelingen, 70=Andel af den totale bilrådighed]
- bol: values [100=I husholdningerne, 110=Stuehuse til landbrugsejendomme, 120=Parcelhuse, 130=Række-, kæde- og dobbelthuse, 140=Etageboliger, 150=Kollegier, 610=Andre typer af boliger, 620=Ejerbolig, 630=Lejerbolig, 640=Uoplyst boligform]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10220=Familier med 1 bil i alt, 10230=Familier med personbil, 10240=Familier med firmabil, 10250=Familier med varebil, 10260=Familier med 2 biler i alt, 10270=Familier med 2 personbiler, 10280=Familier med 2 firmabiler, 10290=Familier med 2 varebiler, 10300=Familier med 1 personbil og 1 firmabil, 10310=Familier med 1 personbil og en varebil, 10320=Familier med 1 firmabil og 1 varebil, 10330=Familier med 3 biler i alt, 10340=Familier med flere end 3 biler]
- tid: date range 2000-01-01 to 2024-01-01
notes:
- maengde4 doubles all rows — always filter to one value: 50=Procentfordelingen, 70=Andel af den totale bilrådighed. Values are Pct.; do not SUM.
- bol has two overlapping classification schemes (boligtype vs. ejerforhold). See bil88 notes. bol=100 is the total.
- raadmoens is hierarchical — pick one level.
