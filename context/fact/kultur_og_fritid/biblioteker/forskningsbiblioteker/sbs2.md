table: fact.sbs2
description: Sammenlignende forskningsbiblioteksstatistik efter bibliotek, nøgletal og tid
measure: indhold (unit Antal)
columns:
- bib2: values [80010=Alle forskningsbiblioteker, 80440=Arbejdermuseet og Arbejderbevægelsens Bibliotek og Arkiv, 80270=Aarhus University Library, Fuglesangs Allé, 80280=AU Library, Matematik, 80450=Biblioteket Arkitektskolen Aarhus ... 80910=Aalborg Universitetsbibliotek, 80920=AU Library, Navitas, 80430=Aarhus Universitet Handels- og IngeniørHøjskolens Bibliotek, Herning, 80545=DIIS Biblioteket, 80930=AU Library, Kalø]
- bnogle: values [16110=Personaleårsværk, 16120=Aktive lånere, 16130=Fysiske besøg, 16140=Åbningstimer, 16150=Arbejdsstationer ... 16310=Lønudgifter (1.000 kr.), 16320=Materialeudgifter (1.000 kr.), 16330=Øvrige udgifter (1.000 kr.), 16340=Indtægter (1.000 kr.), 16350=Nettoudgifter (1.000 kr.)]
- tid: date range 2009-01-01 to 2024-01-01

notes:
- bib2 uses 80xxx coding — different from the other forsk tables which use 82xxx. These are not the same identifiers. bib2=80010 is "Alle forskningsbiblioteker" (the total), covering all research libraries (broader scope than the "med særlige forpligtelser" tables).
- bnogle has 25 KPI metrics with mixed units despite the table header saying "Antal". Codes 16310–16350 are in 1.000 kr. (løn, materiale, øvrige udgifter, indtægter, nettoudgifter). Always select a single bnogle at a time — never sum across bnogle.
- Use ColumnValues("sbs2", "bnogle") to browse all 25 KPI codes.