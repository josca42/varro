table: fact.forsk22
description: Økonomi på forskningsbiblioteker med særlige forpligtelser efter bibliotek, aktivitet og tid
measure: indhold (unit 1.000 kr.)
columns:
- bib2: values [82010=Alle forskningsbiblioteker med særlige forpligtelser, 82130=Arbejdermuseet og Arbejderbevægelsens Bibliotek og Arkiv, 82090=AU Library, Fuglesangs Alle  (fusioneret i 2017 med Det Kgl. Bibliotek), 82140=Biblioteket Arkitektskolen Aarhus, 82150=CBS Bibliotek ... 82380=VIA UC Bibliotekerne, 82390=Aalborg Universitetsbibliotek, 82400=AU Library, Navitas  (fusioneret i 2017 med Det Kgl. Bibliotek), 82205=DIIS Biblioteket, 82405=Øvrige forskningsbiblioteker]
- aktivi: values [13120=Løn, 13125=Udbetalt til ansatte i beskæftigelsesordninger, 13150=Indkøb andre materialer, 13230=Udgifter bygningsdrift, 13240=Udgifter anlæg mv, 13280=Indtægter øvrige, 13126=Indkøb fysiske materialer, 13128=Indkøb elektroniske materialer]
- tid: date range 2009-01-01 to 2024-01-01

notes:
- bib2=82010 is the national total (same coding as other forsk tables).
- aktivi has 8 independent financial line items (all in 1.000 kr.): wages, materials, buildings, investments, and income. There is no aggregate total row in aktivi — if you need total expenditure, build it manually by summing relevant codes.
- Note that 13125 (Udbetalt til ansatte i beskæftigelsesordninger) may be a sub-component of 13120 (Løn) — do not add them together without checking DST source documentation.
- Use ColumnValues("forsk22", "aktivi") to see all 8 expense/income categories.