table: fact.bil86
description: Familiernes bilrådighed (faktiske tal) efter bestand, indkomst, rådighedsmønster og tid
measure: indhold (unit Antal)
columns:
- bestand: values [53=Bestand (E-familier 2007 - ), 73=Bestand (C-familier 2000 - 2006)]
- indkom: values [01=I husholdningerne, 02=Under 50.000 kr, 3=50.000 - 74.999 kr., 4=75.000 - 99.999 kr., 5=100.000 - 124.999 kr. ... 10DC=10. decil, 1KV=1. kvartil, 2KV=2. kvartil, 3KV=3. kvartil, 4KV=4. kvartil]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10220=Familier med 1 bil i alt, 10230=Familier med personbil, 10240=Familier med firmabil, 10250=Familier med varebil, 10260=Familier med 2 biler i alt, 10270=Familier med 2 personbiler, 10280=Familier med 2 firmabiler, 10290=Familier med 2 varebiler, 10300=Familier med 1 personbil og 1 firmabil, 10310=Familier med 1 personbil og en varebil, 10320=Familier med 1 firmabil og 1 varebil, 10330=Familier med 3 biler i alt, 10340=Familier med flere end 3 biler]
- tid: date range 2000-01-01 to 2024-01-01
notes:
- bestand is a methodology selector: 53=E-familier (2007+), 73=C-familier (2000-2006). Filter to one value.
- indkom mixes three overlapping income grouping schemes — pick exactly one: (1) income bands: 01=total, 02=under 50k, 3-24=individual bands, 99=uoplyst; (2) decils: 1DC-10DC; (3) quartiles: 1KV-4KV. Decils and quartiles each sum to the same total as the bands. Never mix schemes in one query.
- raadmoens is hierarchical — pick one level.
