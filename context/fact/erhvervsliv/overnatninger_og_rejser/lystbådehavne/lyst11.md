table: fact.lyst11
description: Overnatninger i lystbådehavne efter farvand, gæstens nationalitet, periode, overnatningsform og tid
measure: indhold (unit Antal)
columns:
- farvand: values [1000=Hele landet, 1010=Sydlige jyske vestkyst, 1020=Limfjorden, 1030=Nordlige jyske vestkyst, 1040=Kattegat, 1050=Østjylland, 1060=Nord og øst for Fyn, 1070=Syd og vest for Fyn, 1080=Smålandsfarvandet, 1090=Vestsjælland, 1100=Isefjorden, 1110=Sundet, 1120=Bornholm og Christiansø]
- nation1: values [TOT=I alt, DAN=Danmark, UDLAN=Verden udenfor Danmark, BELU=Belgien, FIN=Finland ... ØST=Østrig, USA=USA, AUS=Australien, OCEX=Oceanien uden Australien, ANDRE=Uoplyst land]
- periode: values [1=Hele året, 2=År til dato, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September]
- overnatf: values [210=Personovernatninger, 215=Gæstebådsovernatninger]
- tid: date range 1992-01-01 to 2024-01-01

notes:
- farvand is inline coded (no dim join). 1000=Hele landet, 1010–1120=12 sea areas.
- overnatf is a measure selector: 210=Personovernatninger, 215=Gæstebådsovernatninger. Two different metrics — always filter to one.
- periode: same critical overcounting risk. Filter to exactly one periode value.
- nation1: 27 values, TOT=I alt is the grand total.
- lyst11 is the farvand (sea area) equivalent of lyst10 (region/landsdel). Use lyst11 when the question is about coastal/water geography rather than administrative regions.