table: fact.nahc12
description: Kollektiv forbrugsudgift efter forbrugsart, funktion, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- forbrugsart: values [P32S13=Offentlige kollektive forbrugsudgifter]
- funktion: join dim.cofog on funktion=kode::text [approx]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1995-01-01 to 2022-01-01
dim docs: /dim/cofog.md
notes:
- The dim.cofog join is wrong — funktion uses codes CO01-CO10 (custom COFOG mapping) not the numeric codes in dim.cofog. Treat funktion as an inline categorical column, not a dim join.
- funktion values: COT=I alt (total), CO01-CO10 = the 10 COFOG main groups (Generelle offentlige tjenester, Forsvar, etc.). COT is the total — CO01 through CO10 sum to COT.
- forbrugsart has only one value: P32S13=offentlige kollektive forbrugsudgifter. prisenhed (V/LAN) doubles row counts — filter to one value.
- Annual from 1995. No quarterly equivalent. The companion for individual public consumption is nahc011 (formaaal breakdown) or nahc1 (P31S13 row).
