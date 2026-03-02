table: fact.pille02
description: Boliger med træpilleovn og forbrug af træpiller efter primær varmekilde, enhed og tid
measure: indhold (unit -)
columns:
- pvarmekilde: values [1045=Varmekilder i alt, 1050=Naturgasfyr, 1060=Oliefyr, 1070=Fjernvarme, 1080=Varmepumpe, 1090=El-radiator, 1100=Brændeovn, 1110=Træpilleovn, 1130=Øvrige varmekilder]
- enhed: values [1300=Boliger (antal), 1320=Boliger med træpilleovn (antal), 1430=Boliger med træpilleovn (pct.), 1440=Forbrug af træpiller (gigajoule, GJ), 1450=Gennemsnitligt forbrug af træpiller (gigajoule, GJ)]
- tid: date range 2023-01-01 to 2023-01-01

notes:
- enhed is a measurement selector — every pvarmekilde has 5 different enhed values: 1300 (boliger i alt, antal), 1320 (boliger med træpilleovn, antal), 1430 (boliger med træpilleovn, pct.), 1440 (forbrug af træpiller, GJ), 1450 (gennemsnitligt forbrug af træpiller, GJ). Always filter to one enhed.
- pvarmekilde=1045 is the total across all heat sources. Filter it out when comparing sources: WHERE pvarmekilde != '1045'.
- Structure mirrors brande02 but for træpilleovn; note the different enhed codes (1320/1430/1440/1450 vs. brande02's 1310/1330/1350/1370).
- Only 2023 data. For multi-year national totals use brande01 (aktp=1000 for count, aktp=1020 for consumption).