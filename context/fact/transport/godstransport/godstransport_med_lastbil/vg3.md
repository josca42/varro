table: fact.vg3
description: Vejgodstransport (sæsonkorrigeret) efter kørselsart, enhed og tid
measure: indhold (unit -)
columns:
- korart: values [1000=KØRSEL I ALT, 1500=National kørsel, 2000=Vognmandskørsel, 3000=Firmakørsel, 3500=International kørsel i alt, TIL=Til Danmark fra udlandet, FRA=Fra Danmark til udlandet, 3510=Øvrig international kørsel]
- enhed: values [70=Pålæsset godsmængde (1000 ton), 88=Transportarbejde (mio. tonkm), 99=Kørte km (mio. km)]
- tid: date range 2010-01-01 to 2025-04-01

notes:
- enhed is a measurement selector (70=tons, 88=mio. tonkm, 99=mio. km). Filter to one.
- korart has the same overlapping hierarchy as vg2. 1000=grand total; 1500+3500=1000; TIL+FRA+3510=3500.
- Seasonally adjusted figures only, from 2010. For actual figures or longer series use vg2.
- Never mix vg2 and vg3 in the same analysis.