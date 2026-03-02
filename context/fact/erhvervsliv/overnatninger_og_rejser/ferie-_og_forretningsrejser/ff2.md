table: fact.ff2
description: Ferierejser efter destination, varighed, formål og tid
measure: indhold (unit Pct.)
columns:
- destina: values [DAN=Danmark, UDLAN=Verden udenfor Danmark]
- kmdr: values [1=Mindre end fire overnatninger, 2=Mindst fire overnatninger]
- formaaal: values [1=Helse- eller kurophold, 2=Sommerhus, 3=Badeferie (sol, strand og vand), 4=Ungrejse (fester og sociale aktiviteter), 5=Skiferie, 6=Storbyferie (shopping, kultur, cafémiljø), 7=Naturferie (opleve og opholde sig i naturen), 8=Kursus og uddannelse, 9=Besøge familie eller venner, 10=Kroferie, 11=Eventrejse (sport- eller koncertarrangementer), 12=Andet, 99=Ved ikke]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- indhold is percentage share of holiday trips by trip purpose (formaaal). Values sum to ~100 across formaaal for a fixed destina+kmdr+tid. Never sum across formaaal values — they're shares.
- SERIES BREAK around 2017: formaaal categories shrank significantly. 2007-2016 has 10-12 purpose codes; from 2018 onwards only 4 codes appear (2=Sommerhus, 3=Badeferie, 9=Familie/venner, 12=Andet). 2017 is a transition year with 5 codes. Cross-year comparisons of individual purposes are unreliable across this break.
- destina has only 2 values: DAN (domestic) and UDLAN (abroad). Always filter to one or compare both explicitly.
- kmdr splits short vs long trips — filter to one to avoid double-counting.
- formaaal=99 (Ved ikke) appears in the doc but is absent from the data. Don't rely on it.
- For recent years (2018+), "Andet" (formaaal=12) absorbs all the categories that were retired — its share is correspondingly inflated relative to earlier years.