table: fact.forsk24
description: Bestand af fysiske materialer på forskningsbiblioteker med særlige forpligtelser efter bibliotek, materialetype og tid
measure: indhold (unit Antal)
columns:
- bib2: values [82010=Alle forskningsbiblioteker med særlige forpligtelser, 82130=Arbejdermuseet og Arbejderbevægelsens Bibliotek og Arkiv, 82090=AU Library, Fuglesangs Alle  (fusioneret i 2017 med Det Kgl. Bibliotek), 82140=Biblioteket Arkitektskolen Aarhus, 82150=CBS Bibliotek ... 82380=VIA UC Bibliotekerne, 82390=Aalborg Universitetsbibliotek, 82400=AU Library, Navitas  (fusioneret i 2017 med Det Kgl. Bibliotek), 82205=DIIS Biblioteket, 82405=Øvrige forskningsbiblioteker]
- mater: values [655=Bøger og seriepublikationer, 660=Manuskripter, 665=Mikroformer, 670=Grafiske dokumenter, 675=Kartografiske dokumenter, 680=Trykte musikalier, 685=AV-dokumenter, 690=Digitale tekstdokumenter, 695=Andre biblioteksmaterialer, 700=Ikke katalogiseret biblioteksmateriale, 705=Seriepublikationer i trykt form (antal abon.), 710=Hyldemeter af fysiske enheder]
- tid: date range 2009-01-01 to 2024-01-01

notes:
- mater has 12 physical material type codes with no aggregate total row. To get total physical stock for a library, SUM across all mater values.
- mater=710 (Hyldemeter af fysiske enheder) is a shelf-meter measure, not a count of items — exclude it when summing item counts.
- bib2=82010 is the national total. Same 82xxx coding as other forsk tables.
- Use ColumnValues("forsk24", "mater") to see all 12 material types.