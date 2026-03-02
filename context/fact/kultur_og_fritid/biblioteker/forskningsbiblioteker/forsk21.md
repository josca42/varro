table: fact.forsk21
description: Forskningsbiblioteker med særlige forpligtelser efter bibliotek, aktivitet og tid
measure: indhold (unit Antal)
columns:
- bib2: values [82010=Alle forskningsbiblioteker med særlige forpligtelser, 82130=Arbejdermuseet og Arbejderbevægelsens Bibliotek og Arkiv, 82090=AU Library, Fuglesangs Alle  (fusioneret i 2017 med Det Kgl. Bibliotek), 82140=Biblioteket Arkitektskolen Aarhus, 82150=CBS Bibliotek ... 82380=VIA UC Bibliotekerne, 82390=Aalborg Universitetsbibliotek, 82400=AU Library, Navitas  (fusioneret i 2017 med Det Kgl. Bibliotek), 82205=DIIS Biblioteket, 82405=Øvrige forskningsbiblioteker]
- aktivi: values [11110=Hovedbibliotek (åbningstimer pr. uge), 11130=Filialernes samlede åbningstid (timer pr. uge), 11140=Siddepladser med bordplads, 11150=Publikumsareal (kvm, netto), 11160=Lukket magasinareal (kvm, netto) ... 11310=Øvrigt akademisk uddannet personale (årsværk), 11320=Øvrige personale (årsværk), 11330=Personale, heraf i beskæftigelsesordning mv. (årsværk), 11340=Frivillige på biblioteket, 11350=Frivilliges tid på biblioteket (timer pr. uge)]
- tid: date range 2009-01-01 to 2024-01-01

notes:
- bib2=82010 is the aggregate "Alle forskningsbiblioteker med særlige forpligtelser". bib2=82405 is "Øvrige forskningsbiblioteker" (catch-all for smaller institutions). Filter to a specific library or use 82010 for the national total.
- aktivi has 26 heterogeneous activity metrics with different units (hours/week, sqm, counts, FTEs, volunteers). Never sum across aktivi — each code measures something different. Always filter WHERE aktivi = <code>.
- Use ColumnValues("forsk21", "aktivi") to browse all 26 activity codes and pick the one you need.