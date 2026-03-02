table: fact.flyung6
description: Flytninger blandt unge (15-29-årige) efter flyttetype, alder, tilflytningssted og tid
measure: indhold (unit Antal)
columns:
- flyttetype: values [0=Flyttetype i alt, 101=Flyttet fra forældre, 102=Flyttet til forældre, 103=Flyttet med/mellem forældre, 104=Øvrige flytninger]
- alder: values [TOT1529=15-29 år i alt, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25=25 år, 26=26 år, 27=27 år, 28=28 år, 29=29 år]
- tilflytomr: values [TOT=Tilflytningssted i alt, 50=Inden for kommunen, 51=Mellem kommuner]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- No dimension links. All coding is inline.
- alder has `TOT1529` as aggregate for all 15–29 ages, plus individual years 15–29. Don't sum individual ages alongside TOT1529.
- tilflytomr has `TOT` as aggregate. Filter to `50` (inden for kommunen) or `51` (mellem kommuner) for the within/between split.
- flyttetype has `0` = total. All three non-tid columns have aggregates — filter all to avoid overcounting.
- Mirrors flyung3/flyung4 structure but without geographic breakdown, using individual ages instead of broad groups.