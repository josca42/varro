table: fact.flyv91
description: Afrejsende passagerer fra større, offentlige, betjente lufthavne efter lufthavn, transporttype, flyvning og tid
measure: indhold (unit 1.000 personer)
columns:
- lufthavn: values [10010=LUFTHAVNE IALT, 10015=København, 10020=Billund, 10025=Aarhus, 10030=Aalborg, 10070=Øvrige lufthavne]
- transport: values [0=I alt, 15=National, 25=International]
- flyvning: values [20080=Flyvninger i alt, 20085=Ruteflyvninger, 20090=Charter/taxi flyvning, 20095=Anden flyvning]
- tid: date range 2001-01-01 to 2025-04-01

notes:
- Quarterly version of flyv32 with updated unit (1.000 personer vs. flyv32's 1.000 stk.). Prefer flyv91 for current or recent quarterly departing-passenger data.
- Only 5 airport codes (IALT, KBH, Billund, Aarhus, Aalborg, Øvrige) vs. flyv32's 11 individual airports. Use flyv32 for small-airport detail or annual historical series from 1990.
- transport=0 and flyvning=20080 are aggregate totals — filter to one value per column.
- lufthavn=10010 is the total across all airports. Exclude when summing individual airports.
