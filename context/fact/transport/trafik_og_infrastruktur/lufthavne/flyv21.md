table: fact.flyv21
description: Flyoperationer på større, betjente danske lufthavne efter lufthavn, flyvning, transporttype og tid
measure: indhold (unit 1.000 stk.)
columns:
- lufthavn: values [10010=LUFTHAVNE IALT, 10015=København, 10020=Billund, 10025=Aarhus, 10030=Aalborg, 10035=Midtjyllands Lufthavn (tidligere Karup), 10040=Esbjerg, 10045=Bornholm, 10050=Sønderborg, 10055=Roskilde, 10060=Thisted, 10065=Hans Christian Andersen Airport (Odense)]
- flyvning: values [20080=Flyvninger i alt, 20085=Ruteflyvninger, 20090=Charter/taxi flyvning, 20095=Anden flyvning]
- transport: values [0=I alt, 15=National, 25=International]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- Both flyvning and transport have total rows. Each (lufthavn, tid) has 12 rows (4 flyvning × 3 transport). Always filter both dimensions to avoid overcounting.
- flyvning=20080 (Flyvninger i alt) is the sum of 20085+20090+20095. transport=0 (I alt) is the sum of 15+25. To get a simple total: WHERE flyvning=20080 AND transport=0.
- lufthavn=10010 (LUFTHAVNE IALT) is the national aggregate; exclude when summing individual airports.
- flyv21 covers only the larger airports — it does NOT include lufthavn=10070 (Øvrige lufthavne). Use flyv3 if you need full coverage.
- Unit is 1.000 stk. (thousands of flight operations).