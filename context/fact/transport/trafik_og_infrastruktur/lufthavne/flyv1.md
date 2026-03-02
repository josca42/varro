table: fact.flyv1
description: Offentlige betjente lufthavne efter lufthavn, banelængde og tid
measure: indhold (unit -)
columns:
- lufthavn: values [10010=LUFTHAVNE IALT, 10015=København, 10020=Billund, 10025=Aarhus, 10030=Aalborg, 10035=Midtjyllands Lufthavn (tidligere Karup), 10040=Esbjerg, 10045=Bornholm, 10050=Sønderborg, 10055=Roskilde, 10060=Thisted, 10065=Hans Christian Andersen Airport (Odense), 10070=Øvrige lufthavne]
- banel: values [2010=Antal baner i alt, 2015=Antal baner under 1800 m, 2020=Antal baner mindst 1800 m, 2025=Antal græsbaner, 2030=Antal standpladser, 2035=Heraf bropladser, 2040=Befæstet areal 1000 kvadratmeter, 2045=Bebygget areal 1000 kvadratmeter, 2050=Hangarer og værksteder 1000 kvadratmeter, 2055=Fragtterminaler  1000 kvadratmeter, 2060=Passagerterminaler 1000 kvadratmeter]
- tid: date range 1997-01-01 to 2024-01-01

notes:
- banel contains 11 heterogeneous metrics with different implicit units. Never sum across banel values — they are completely different measurements.
- Count metrics (2010–2035): number of runways/stands. Area metrics (2040–2060): 1000 kvadratmeter. The column unit listed as "-" means the unit comes from the banel label itself.
- banel=2010 (Antal baner i alt) = 2015 (under 1800m) + 2020 (mindst 1800m) + 2025 (græsbaner). Don't include banel=2010 alongside 2015/2020/2025 or you'll double-count.
- banel=2035 (Heraf bropladser) is a subset of 2030 (Antal standpladser) — do not add them together.
- lufthavn=10010 (LUFTHAVNE IALT) is the national aggregate. Earliest year is 1997 (shorter series than flyv3/flyv21).