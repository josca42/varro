table: fact.mms2
description: Miljøstøtte efter miljøformål og tid
measure: indhold (unit Mio. kr.)
columns:
- mformaal: values [MF05=Miljøstøtte i alt (1+2), MF10=1. Støtte til miljøbeskyttelse i alt, MF100=1.1 Beskyttelse af luft og klima, MF15=1.2 Spildevandshåndtering, MF20=1.3 Affaldshåndtering, MF25=1.4 Beskyttelse af jord, grundvand og overfladevand, MF30=1.5 Støj- og vibrationsbekæmpelse, MF35=1.6 Beskyttelse af biodiversitet og landskab, MF40=1.7 Beskyttelse imod stråling, MF45=1.8 Forskning & udvikling inden for miljøbeskyttelse, MF50=1.9 Andre miljøbeskyttelsesaktiviteter (inkl. administration), MF55=2. Støtte til ressourcehåndtering i alt, MF60=2.1 Vand, MF65=2.2 Skov, MF70=2.3 Dyreliv og planter, MF75=2.4 Vedvarende energi og energibesparelser m.m., MF80=2.5 Mineraler, MF85=2.6 Forskning og udvikling inden for naturresourcer, MF90=2.7 Andre ressourcehåndteringsaktiviteter (inkl. administration)]
- tid: date range 1995-01-01 to 2024-01-01

notes:
- mformaal is hierarchical: MF05 = total, MF10 = støtte til miljøbeskyttelse i alt, MF55 = støtte til ressourcehåndtering i alt. MF10 and MF55 sum to MF05. Sub-categories MF100–MF50 are breakdowns under MF10; MF60–MF90 are under MF55. Don't mix levels in a SUM.
- For total environmental subsidies by purpose type: WHERE mformaal IN ('MF10','MF55'). For detailed purpose breakdown under miljøbeskyttelse: WHERE mformaal BETWEEN 'MF100' AND 'MF50' (9 sub-categories).
- No dim table link — all values are inline. Use ColumnValues("mms2", "mformaal") to browse all codes with labels.