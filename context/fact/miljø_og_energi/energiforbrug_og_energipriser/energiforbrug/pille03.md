table: fact.pille03
description: Boliger med træpilleovn og forbrug af træpiller efter boligtype, enhed og tid
measure: indhold (unit -)
columns:
- boltyp: values [1140=Boligtype i alt, 1150=Helårsboliger i alt, 1160=Enfamilieshuse, 1162=Enfamilieshuse med fjernvarme, 1164=Enfamilieshuse uden fjernvarme, 1170=Lejligheder, 1180=Fritidshuse med CPR-tilmeldte personer, 1190=Fritidshuse uden CPR-tilmeldte personer i alt]
- enhed: values [1300=Boliger (antal), 1320=Boliger med træpilleovn (antal), 1430=Boliger med træpilleovn (pct.), 1440=Forbrug af træpiller (gigajoule, GJ), 1450=Gennemsnitligt forbrug af træpiller (gigajoule, GJ)]
- tid: date range 2023-01-01 to 2023-01-01

notes:
- enhed is a measurement selector — every boltyp has 5 different enhed values: 1300 (boliger i alt, antal), 1320 (boliger med træpilleovn, antal), 1430 (boliger med træpilleovn, pct.), 1440 (forbrug af træpiller, GJ), 1450 (gennemsnitligt forbrug af træpiller, GJ). Always filter to one enhed.
- boltyp=1140 is the total for all housing types. boltyp=1150 (helårsboliger) is a sub-aggregate; boltyp=1160 (enfamilieshuse) splits into 1162 and 1164. Don't sum parent and children.
- Structure mirrors brande03 but for træpilleovn.
- Only 2023 data. For multi-year national totals use brande01.