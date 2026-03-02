table: fact.hdyroeko
description: Økologiske landbrug med udvalgte dyr efter enhed, art og tid
measure: indhold (unit -)
columns:
- enhed: values [ANTAL=Bedrifter (antal), DYR=Dyr (antal)]
- dyr: values [0=Økologiske  bedrifter med dyr i alt, 105=Kvæg i alt, 110=Malkekøer, 115=Får og geder, 120=Svin i alt, 125=Søer, 130=Æglæggende høner, 135=Slagtekyllinger, 140=Fjerkræ i øvrigt]
- tid: date range 2010-01-01 to 2024-01-01

notes:
- enhed is a measurement selector (ANTAL=bedrifter, DYR=dyr). Always filter to one value.
- dyr has only 9 simple values: 0=Økologiske bedrifter med dyr i alt, 105=Kvæg i alt, 110=Malkekøer, 115=Får og geder, 120=Svin i alt, 125=Søer, 130=Æglæggende høner, 135=Slagtekyllinger, 140=Fjerkræ i øvrigt. Code 0 is the overall total; 105 and 120 are animal-type totals that overlap with their subtypes. Don't sum all dyr codes.
- No regional breakdown — national organic farming totals only. Coverage 2010–2024.