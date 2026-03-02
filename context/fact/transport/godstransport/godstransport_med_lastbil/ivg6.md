table: fact.ivg6
description: Danske lastbilers kapacitetsudnyttelse ved international transport efter enhed, turlængde, kørselsart/vogntype, læs og tid
measure: indhold (unit -)
columns:
- maengde4: values [90=Pct. af lasteevnen (ton) , 95=Pct. af lasteevnen (ton) korrigeret for volumengods, 100=Pct. af muligt transportarbejde (tonkm), 110=Pct. af muligt transportarbejde (tonkm) korrigeret for volumengods]
- turkm: values [00=Ture i alt, 000-250=Mindre end 250 km, 250-499=250-499 km, 500-999=500-999 km, 1000OV=1000 km eller mere]
- vogn1: values [0=I ALT, 50=Solovogn, i alt, 55=Påhængsvogntog, i alt, 60=Sættevognstog, i alt, 105=Fra Danmark, i alt, 110=Fra Danmark, Solovogn, 115=Fra Danmark, Påhængsvogntog, 120=Fra Danmark, Sættevognstog, 200=Til Danmark, i alt, 210=Til Danmark, Solovogn, 215=Til Danmark, Påhængsvogntog, 220=Til Danmark, Sættevognstog, 300=Anden kørsel, i alt, 310=Anden kørsel, Solovogn, 315=Anden kørsel, Påhængsvogntog, 320=Anden kørsel, Sættevognstog]
- laes: values [1010=Kørsel i alt (inkl. tomkørsel), 1030=Kørsel med læs i alt]
- tid: date range 1999-01-01 to 2024-01-01

notes:
- maengde4 is the measurement selector (capacity utilization percentages). All values are rates — do not sum across maengde4. Filter to one.
- turkm=00 (Ture i alt) aggregates across all distances. International trips are much longer than national — bands go up to 1000km+.
- vogn1 mixes vehicle type (Solovogn/Påhængs/Sætte, codes 50/55/60) and direction (Fra Danmark/Til Danmark/Anden kørsel, codes 105/200/300) with cross combinations. Code 0=I ALT. Pick one dimension: either vehicle type or direction, not both.
- laes: 1010=Kørsel i alt (incl. empty) and 1030=Kørsel med læs overlap. Pick one.
- International equivalent of nvg5, with longer trip distances and direction-based vogn breakdown.