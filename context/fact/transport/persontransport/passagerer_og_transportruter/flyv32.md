table: fact.flyv32
description: Afrejsende passagerer fra større, offentlige, betjente lufthavne efter lufthavn, transporttype, flyvning og tid
measure: indhold (unit 1.000 stk.)
columns:
- lufthavn: values [10010=LUFTHAVNE IALT, 10015=København, 10020=Billund, 10025=Aarhus, 10030=Aalborg, 10035=Midtjyllands Lufthavn (tidligere Karup), 10040=Esbjerg, 10045=Bornholm, 10050=Sønderborg, 10055=Roskilde, 10060=Thisted, 10065=Hans Christian Andersen Airport (Odense)]
- transport: values [0=I alt, 15=National, 25=International]
- flyvning: values [20080=Flyvninger i alt, 20085=Ruteflyvninger, 20090=Charter/taxi flyvning, 20095=Anden flyvning]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- Departing passengers only (not arrivals). Both transport and flyvning have aggregate codes: transport=0 (I alt) = 15 + 25; flyvning=20080 (i alt) = 20085 + 20090 + 20095. Always filter to one value per column or use the aggregate.
- lufthavn=10010 is the total across all airports. Exclude when summing individual airports.
- Has all 11 individual airports. Annual data from 1990 — use for long historical series or when small-airport detail is needed.
- For current quarterly departing-passenger data use flyv91 (same structure, 5 airports, quarterly 2001–2025). For monthly all-airports combined use flyv92.
