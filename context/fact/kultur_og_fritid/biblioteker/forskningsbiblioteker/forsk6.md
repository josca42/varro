table: fact.forsk6
description: Interurbanindlån på forskningsbiblioteker med særlige forpligtelser efter bibliotek, kilde og tid
measure: indhold (unit Antal)
columns:
- bib2: values [82010=Alle forskningsbiblioteker med særlige forpligtelser, 82130=Arbejdermuseet og Arbejderbevægelsens Bibliotek og Arkiv, 82090=AU Library, Fuglesangs Alle  (fusioneret i 2017 med Det Kgl. Bibliotek), 82140=Biblioteket Arkitektskolen Aarhus, 82150=CBS Bibliotek ... 82390=Aalborg Universitetsbibliotek, 82400=AU Library, Navitas  (fusioneret i 2017 med Det Kgl. Bibliotek), 82120=Aarhus Universitet Handels- og IngeniørHøjskolens Bibliotek, Herning, 84270=Aarhus University Library, 82205=DIIS Biblioteket]
- kild: values [19169=Interurbanindlån i alt, 19170=Fra folkebiblioteker i Danmark, 19171=Fra andre biblioteker i Danmark, 19172=Fra biblioteker i Norden, 19173=Fra biblioteker i øvrige udland]
- tid: date range 2009-01-01 to 2024-01-01

notes:
- kild=19169 is "Interurbanindlån i alt" (the total). The other 4 kild values (19170–19173) are breakdowns by source (domestic folk libraries, other Danish libraries, Nordic countries, rest of world). Do not sum 19169 together with 19170–19173 — double counting.
- bib2=82010 is the national total, same 82xxx coding as other forsk tables.