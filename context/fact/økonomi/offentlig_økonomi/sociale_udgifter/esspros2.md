table: fact.esspros2
description: Sociale udgifter efter formål, finansieringskilde og tid
measure: indhold (unit Mio. kr.)
columns:
- formal: join dim.esspros on formal=kode [approx]
- finans: values [60=FINANSIERING I ALT, 65=Staten, 71=Kommuner, 75=Arbejdsgivere, 80=Sikrede, 85=Formueindkomst]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/esspros.md

notes:
- formal does NOT join dim.esspros. The dim uses codes 1–9, but formal uses a 3-digit system (100–140). Use ColumnValues("esspros2", "formal") to get the 9 values: 100=SOCIALE UDGIFTER I ALT, 105=Sygdom og sundhed, 110=Invaliditet, 115=Alderdom, 120=Efterladte, 125=Familier, 130=Arbejdsløshed, 135=Bolig, 140=Øvrige sociale ydelser.
- formal only has one hierarchy level (the 8 main categories + total). There are no subcategories — for detailed breakdown by foranstaltning use esspros1 instead.
- finans is a financing source selector: 60=FINANSIERING I ALT (total), 65=Staten, 71=Kommuner, 75=Arbejdsgivere, 80=Sikrede, 85=Formueindkomst. Never sum across finans values — always filter to one. For total expenditure by purpose filter finans=60.
- Not all (formal, finans) combinations exist — e.g. Arbejdsløshed (130) has no Sikrede (80) or Formueindkomst (85) rows. Outer join or check before assuming all combinations are present.
- Each (formal, tid) pair appears once per applicable finans value. Forgetting to filter finans inflates sums.