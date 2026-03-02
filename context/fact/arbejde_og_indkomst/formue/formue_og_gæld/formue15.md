table: fact.formue15
description: Formue efter formue, definition, prisenhed, alder og tid
measure: indhold (unit -)
columns:
- formue: values [0000M10=Under (-1.000.000 kr.), M100M05=(-1.000.000 kr.) - (-500.000 kr.), M050000=(-500.000 kr.) - 0 kr., 0000005=0 kr. - 500.000 kr., 0050010=500.000 kr. - 1.000.000 kr., 0100015=1.000.000 kr. - 1.500.000 kr., 0150020=1.500.000 kr. - 2.000.000 kr., 0200025=2.000.000 kr. - 2.500.000 kr., 0250030=2.500.000 kr. - 3.000.000 kr., 0300035=3.000.000 kr. - 3.500.000 kr., 0350040=3.500.000 kr. - 4.000.000 kr., 0400045=4.000.000 kr. - 4.500.000 kr., 0450050=4.500.000 kr. - 5.000.000 kr., 0500055=5.000.000 kr. - 5.500.000 kr., 0550060=5.500.000 kr. - 6.000.000 kr., 0600000=Over 6.000.000 kr.]
- definition: values [D20=2020-definition (inkl. unoterede aktier og gæld til til inddrivelse, fra 2020), D14=2014-definition (ekskl. unoterede aktier og gæld til til inddrivelse)]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 6=Nominelle priser]
- alder: values [1802=18 år og derover, 1829=18-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8089=80-89 år, 9099=90 år og derover]
- tid: date range 2020-01-01 to 2023-01-01

notes:
- indhold is a count of persons in each wealth bracket (not a median or mean). The 16 formue brackets are a complete distribution — summing across all brackets gives the total population for that alder/definition/prisenhed combination.
- Two mandatory selectors: definition (D20 or D14) and prisenhed (5=faste or 6=nominelle). Every alder/tid combination is repeated 4 times (2×2). Filter both to get a single distribution.
- D20 is the broader 2020-definition (includes unlisted equities and collection debt). D14 is the older narrower definition. For comparisons across the full 2014-2023 period use D14; for most current analysis use D20.
- Shorter time series: 2020-2023 only (vs 2014-2023 for formue11-14/17). D20 data only exists from 2020.
- No gender, region, socio, or origin breakdown — use formue11-14 for those dimensions.
