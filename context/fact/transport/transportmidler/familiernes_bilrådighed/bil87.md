table: fact.bil87
description: Familiernes bilrådighed (andele og fordelinger) efter enhed, indkomst, rådighedsmønster og tid
measure: indhold (unit Pct.)
columns:
- maengde4: values [50=Procentfordelingen, 70=Andel af den totale bilrådighed]
- indkom: values [01=I husholdningerne, 02=Under 50.000 kr, 3=50.000 - 74.999 kr., 4=75.000 - 99.999 kr., 5=100.000 - 124.999 kr. ... 10DC=10. decil, 1KV=1. kvartil, 2KV=2. kvartil, 3KV=3. kvartil, 4KV=4. kvartil]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10220=Familier med 1 bil i alt, 10230=Familier med personbil, 10240=Familier med firmabil, 10250=Familier med varebil, 10260=Familier med 2 biler i alt, 10270=Familier med 2 personbiler, 10280=Familier med 2 firmabiler, 10290=Familier med 2 varebiler, 10300=Familier med 1 personbil og 1 firmabil, 10310=Familier med 1 personbil og en varebil, 10320=Familier med 1 firmabil og 1 varebil, 10330=Familier med 3 biler i alt, 10340=Familier med flere end 3 biler]
- tid: date range 2000-01-01 to 2024-01-01
notes:
- maengde4 doubles all rows — always filter to one value: 50=Procentfordelingen, 70=Andel af den totale bilrådighed. Values are Pct.; do not SUM.
- indkom mixes three overlapping schemes (bands, decils, quartiles). See bil86 notes. Use 01 for total.
- raadmoens is hierarchical — pick one level.
