table: fact.forsk5c
description: Bestand og brug af elektroniske ressourcer på forskningsbiblioteker med særlige forpligtelser efter bibliotek, opgørelse, elektronisk materialetype, placering og tid
measure: indhold (unit Antal)
columns:
- bib2: values [82010=Alle forskningsbiblioteker med særlige forpligtelser, 82130=Arbejdermuseet og Arbejderbevægelsens Bibliotek og Arkiv, 82090=AU Library, Fuglesangs Alle  (fusioneret i 2017 med Det Kgl. Bibliotek), 82140=Biblioteket Arkitektskolen Aarhus, 82150=CBS Bibliotek ... 82390=Aalborg Universitetsbibliotek, 82400=AU Library, Navitas  (fusioneret i 2017 med Det Kgl. Bibliotek), 82120=Aarhus Universitet Handels- og IngeniørHøjskolens Bibliotek, Herning, 84270=Aarhus University Library, 82205=DIIS Biblioteket]
- opgoer1: values [177=Bestand (titler), 178=Brug (download)]
- matypelek: values [183=E-tidsskrifter og andre e-serier, 184=E-bøger og lydbøger, 185=Andre e-materialer og manuskripter, 186=E-multimedieoptagelser, 187=Databaser, 188=Databaser, bibliografisk, 189=Databaser, andre, 190=Databaser, fuldtekst]
- placering: values [31=Egen server, 32=Ekstern server]
- tid: date range 2014-01-01 to 2024-01-01 (starts later than other forsk tables — 2014 not 2009)

notes:
- Has 4 dimension columns (bib2, opgoer1, matypelek, placering). Filter all non-target columns to avoid overcounting.
- opgoer1 must be filtered: 177=Bestand (titler/stock) and 178=Brug (downloads/usage) are completely different metrics — never sum them together.
- placering: 31=Egen server, 32=Ekstern server. Sum across both to get totals regardless of hosting, or filter to compare hosting types.
- matypelek 187/188/189/190 are database subtypes (187=Databaser, 188=bibliografisk, 189=andre, 190=fuldtekst). These sub-types only appear on ekstern server (32) — likely sub-categories of 187. Do not sum 187 with 188–190.
- bib2=82010 is the national total. Same 82xxx coding as other forsk tables.
- Use ColumnValues("forsk5c", "matypelek") for the full list of electronic material types.