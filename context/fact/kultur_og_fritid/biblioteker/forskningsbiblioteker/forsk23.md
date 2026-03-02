table: fact.forsk23
description: Udlån på forskningsbiblioteker med særlige forpligtelser efter bibliotek, opgørelse, modtagertype og tid
measure: indhold (unit Antal)
columns:
- bib2: values [82010=Alle forskningsbiblioteker med særlige forpligtelser, 82130=Arbejdermuseet og Arbejderbevægelsens Bibliotek og Arkiv, 82090=AU Library, Fuglesangs Alle  (fusioneret i 2017 med Det Kgl. Bibliotek), 82140=Biblioteket Arkitektskolen Aarhus, 82150=CBS Bibliotek ... 82380=VIA UC Bibliotekerne, 82390=Aalborg Universitetsbibliotek, 82400=AU Library, Navitas  (fusioneret i 2017 med Det Kgl. Bibliotek), 82205=DIIS Biblioteket, 82405=Øvrige forskningsbiblioteker]
- opgoer1: values [18150=Udlån, 18160=Kopi der erstatter udlån]
- modtag: values [410=Direkte bruger, 420=Læsesalsbrug, 440=Interurbanudlån til folkebiblioteker i Danmark, 450=Interurbanudlån til andre offentlige biblioteker i Danmark, 480=Interurbanudlån til udenlandske biblioteker]
- tid: date range 2009-01-01 to 2024-01-01

notes:
- opgoer1 has two independent loan types: 18150=Udlån (physical loans) and 18160=Kopi der erstatter udlån (copies in lieu of loans). These are not additive — always filter to one type per query.
- modtag has 5 recipient categories with no "I alt" total row. Sum across all modtag values to get the total loans for a given opgoer1 type and library.
- bib2=82010 is the national total. Same 82xxx coding as other forsk tables.