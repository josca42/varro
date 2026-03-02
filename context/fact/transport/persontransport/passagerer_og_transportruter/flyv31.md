table: fact.flyv31
description: Passagerer på større offentlige, betjente danske lufthavne efter lufthavn, passagerkategori og tid
measure: indhold (unit 1.000 stk.)
columns:
- lufthavn: values [10010=LUFTHAVNE IALT, 10015=København, 10020=Billund, 10025=Aarhus, 10030=Aalborg, 10035=Midtjyllands Lufthavn (tidligere Karup), 10040=Esbjerg, 10045=Bornholm, 10050=Sønderborg, 10055=Roskilde, 10060=Thisted, 10065=Hans Christian Andersen Airport (Odense)]
- passager: values [7010=PASSAGERER I ALT, 1000, 7030=Afrejsende passagerer, i alt, 7035=Afrejsende passagerer, terminal, 7040=Afrejsende passagerer, transfer, 7045=Afrejsende passagerer, transit, 7050=Ankommende passagerer, i alt, 7055=Ankommende passagerer, terminal, 7060=Ankommende passagerer, transfer]
- tid: date range 2003-01-01 to 2024-01-01

notes:
- passager is a hierarchical measurement selector — always filter to exactly one value. Hierarchy: 7010 (total throughput) = 7030 (departures) + 7050 (arrivals). 7030 = 7035 + 7040 + 7045. 7050 = 7055 + 7060.
- 7010 (PASSAGERER I ALT) counts each passenger twice (once departing, once arriving) — it represents airport throughput, not number of trips. For trips, use 7030 (departing passengers only).
- lufthavn=10010 is the pre-computed total across all airports. Exclude when summing individual airports.
- Annual data with all 11 individual airports. For current quarterly data by airport use flyv91 (but only 5 airports). For departing-only breakdown by transport/flight type, use flyv32.
