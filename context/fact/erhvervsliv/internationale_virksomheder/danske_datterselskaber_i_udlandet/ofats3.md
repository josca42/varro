table: fact.ofats3
description: Danske datterselskaber i udlandet efter lande, branche, enhed og tid
measure: indhold (unit Antal)
columns:
- lande: values [TOT=I alt, D2=EU-15 (- 2019), V1MD2=EU-medlemslande siden 2004, V5=EU-27 (uden Storbritannien), E1MV1=Europa udenfor EU, E8=Nordamerika, E9PF1=Syd- og Mellemamerika, E4=Afrika, F2=Asien, F7=Oceanien]
- branche: join dim.db_10 on branche=kode::text [approx]; levels [1]
- enhed: values [DSANTAL=Datterselskaber, DSANSAT=Ansatte]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/db_10.md

notes:
- enhed is a measurement selector: every lande/branche/tid combination exists twice — DSANTAL (antal datterselskaber) and DSANSAT (antal ansatte). Always filter to one value.
- lande is the same inline regional groupings as ofats2 (TOT, D2, V5, E8, etc.) — not individual countries.
- branche joins dim.db_10 at niveau 1 for codes 2, 4, 5, 6, 7, 8. Two codes don't match the dim:
  - TOT = total across all branches (aggregate — exclude when summing).
  - 3910 = a custom aggregate grouping for branches 1 (landbrug), 3 (bygge og anlæg), 9 (offentlig admin) and 10 (kultur/service), which are too sparse to show individually. Its values sum exactly to the difference between the branch subtotals and TOT. Use it as-is but don't try to join it to dim.db_10.
- To query by industry: filter WHERE f.branche NOT IN ('TOT') and join dim.db_10 d ON f.branche = d.kode::text AND d.niveau = 1. 3910 will be a LEFT JOIN orphan — label it manually as 'Øvrige brancher' if needed.