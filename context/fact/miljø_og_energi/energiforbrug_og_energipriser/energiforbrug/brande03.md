table: fact.brande03
description: Boliger med brændeovn og forbrug af brænde efter boligtype, enhed og tid
measure: indhold (unit -)
columns:
- boltyp: values [1140=Boligtype i alt, 1150=Helårsboliger i alt, 1160=Enfamilieshuse, 1162=Enfamilieshuse med fjernvarme, 1164=Enfamilieshuse uden fjernvarme, 1170=Lejligheder, 1180=Fritidshuse med CPR-tilmeldte personer, 1190=Fritidshuse uden CPR-tilmeldte personer i alt]
- enhed: values [1300=Boliger (antal), 1310=Boliger med brændeovn (antal), 1330=Boliger med brændeovn (pct.), 1350=Forbrug af brænde (gigajoule, GJ), 1370=Gennemsnitligt forbrug af brænde (gigajoule, GJ)]
- tid: date range 2023-01-01 to 2023-01-01

notes:
- enhed is a measurement selector — every boltyp has 5 different enhed values: 1300 (boliger i alt, antal), 1310 (boliger med brændeovn, antal), 1330 (boliger med brændeovn, pct.), 1350 (forbrug af brænde, GJ), 1370 (gennemsnitligt forbrug af brænde, GJ). Always filter to one enhed.
- boltyp=1140 is the total for all housing types. Filter it out when comparing individual types: WHERE boltyp != '1140'.
- Note boltyp=1150 (helårsboliger i alt) is a sub-aggregate of 1140; boltyp=1160 (enfamilieshuse) further splits into 1162 (med fjernvarme) and 1164 (uden fjernvarme) — avoid summing parent + children.
- Only 2023 data. For a multi-year time series use brande01.