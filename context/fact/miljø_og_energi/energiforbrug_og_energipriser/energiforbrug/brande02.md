table: fact.brande02
description: Boliger med brændeovn og forbrug af brænde efter primær varmekilde, enhed og tid
measure: indhold (unit -)
columns:
- pvarmekilde: values [1045=Varmekilder i alt, 1050=Naturgasfyr, 1060=Oliefyr, 1070=Fjernvarme, 1080=Varmepumpe, 1090=El-radiator, 1100=Brændeovn, 1110=Træpilleovn, 1130=Øvrige varmekilder]
- enhed: values [1300=Boliger (antal), 1310=Boliger med brændeovn (antal), 1330=Boliger med brændeovn (pct.), 1350=Forbrug af brænde (gigajoule, GJ), 1370=Gennemsnitligt forbrug af brænde (gigajoule, GJ)]
- tid: date range 2023-01-01 to 2023-01-01

notes:
- enhed is a measurement selector — every pvarmekilde has 5 different enhed values: 1300 (boliger i alt, antal), 1310 (boliger med brændeovn, antal), 1330 (boliger med brændeovn, pct.), 1350 (forbrug af brænde, GJ), 1370 (gennemsnitligt forbrug af brænde, GJ). Always filter to one: e.g. WHERE enhed = '1350' for consumption in GJ.
- pvarmekilde=1045 is the total across all heat sources. Filter it out when comparing individual sources: WHERE pvarmekilde != '1045'.
- Only 2023 data. For a multi-year national time series use brande01 instead.