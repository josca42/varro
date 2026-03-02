table: fact.flyv41
description: Lufttransport af gods over betjente danske lufthavne efter lufthavn, transporttype og tid
measure: indhold (unit 100 ton)
columns:
- lufthavn: values [10010=LUFTHAVNE IALT, 10015=København, 10020=Billund, 10025=Aarhus, 10030=Aalborg, 10035=Midtjyllands Lufthavn (tidligere Karup), 10040=Esbjerg, 10045=Bornholm, 10050=Sønderborg, 10055=Roskilde, 10060=Thisted, 10065=Hans Christian Andersen Airport (Odense), 10070=Øvrige lufthavne]
- transport: values [0=I alt, 15=National, 25=International]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- No dimension joins — lufthavn and transport are inline coded values fully listed above.
- lufthavn=10010 (LUFTHAVNE IALT) is the grand total across all airports. The individual airports (10015–10070) sum to this total. Never mix 10010 with individual airports in the same aggregation.
- transport=0 (I alt) equals National(15) + International(25). Filter to one value; summing across all three transport values triples the count.
- For a clean total: WHERE lufthavn=10010 AND transport=0 gives the national aggregate in 100 ton. To break down by airport, filter transport=0 and exclude lufthavn=10010.
- indhold unit is 100 ton — multiply by 100 to get tonnes.
- lufthavn=10065 (Hans Christian Andersen Airport, Odense) only has data for 1993, 1997, 1998 — essentially inactive, effectively zero cargo.
- Data is annual (tid = year-01-01). The series runs 1990–2024.