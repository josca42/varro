table: fact.lyst2
description: Overnatninger i lystbådehavne efter farvand, gæstens nationalitet, periode og tid
measure: indhold (unit Antal)
columns:
- farvand: values [1000=Hele landet, 1010=Sydlige jyske vestkyst, 1020=Limfjorden, 1030=Nordlige jyske vestkyst, 1040=Kattegat, 1050=Østjylland, 1060=Nord og øst for Fyn, 1070=Syd og vest for Fyn, 1080=Smålandsfarvandet, 1090=Vestsjælland, 1100=Isefjorden, 1110=Sundet, 1120=Bornholm og Christiansø]
- nation1: values [TOT=I alt, DAN=Danmark, UDLAN=Verden udenfor Danmark, BELU=Belgien, FIN=Finland ... ØST=Østrig, USA=USA, AUS=Australien, OCEX=Oceanien uden Australien, ANDRE=Uoplyst land]
- periode: values [1=Hele året, 2=År til dato, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September]
- tid: date range 1992-01-01 to 2025-01-01

notes:
- farvand is inline coded (no dim join). 1000=Hele landet, 1010–1120=12 named farvande (sea areas). Use farvand='1000' for national total.
- periode is a critical overcounting column. Values 1=Hele året (annual sum), 2=År til dato, 5-9=individual months May–Sep. Always filter to exactly one periode value.
- nation1: same 27-value structure as lyst1. TOT=I alt is the grand total; filter nation1='TOT' for overall counts.
- For a simple annual national total: WHERE f.farvand='1000' AND f.nation1='TOT' AND f.periode='1'.