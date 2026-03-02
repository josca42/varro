table: fact.ofats2
description: Danske datterselskaber i udlandet efter lande, enhed og tid
measure: indhold (unit Antal)
columns:
- lande: values [TOT=I alt, D2=EU-15 (- 2019), V1MD2=EU-medlemslande siden 2004, V5=EU-27 (uden Storbritannien), E1MV1=Europa udenfor EU, E8=Nordamerika, E9PF1=Syd- og Mellemamerika, E4=Afrika, F2=Asien, F7=Oceanien]
- enhed: values [DSANTAL=Datterselskaber, DSANSAT=Ansatte]
- tid: date range 2007-01-01 to 2023-01-01

notes:
- enhed is a measurement selector: every lande/tid row exists twice — DSANTAL (antal datterselskaber) and DSANSAT (antal ansatte). Always filter to one value, e.g. WHERE enhed='DSANTAL'.
- lande is inline regional groupings, not individual countries. TOT=I alt (world total), D2=EU-15, V5=EU-27 (excl. UK), V1MD2=EU members since 2004, E1MV1=Europa udenfor EU, E8=Nordamerika, E9PF1=Syd- og Mellemamerika, E4=Afrika, F2=Asien, F7=Oceanien. These are mutually exclusive at this aggregation level — don't sum across codes unless you know they don't overlap.
- This is the oldest table (from 2007); use it when you need regional breakdowns prior to 2010.