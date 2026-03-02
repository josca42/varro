table: fact.ivg13
description: International vejgodstransport  med dansk lastbil efter kørselsart, land, enhed og tid
measure: indhold (unit -)
columns:
- korart: values [1000=KØRSEL I ALT, 4000=Fra Danmark, 5000=Til Danmark]
- land: values [TOT=I alt, BENE=Benelux, FRA=Frankrig, ITA=Italien, SPA=Spanien, STO=Storbritannien, SVE=Sverige, NOR=Norge, TYS=Tyskland, OVRI=Verden udenfor Benelux, Frankrig, Italien, Norge, Spanien, Storbritannien, Sverige og Tyskland]
- enhed: values [70=Pålæsset godsmængde (1000 ton), 80=Transportarbejde (1000 tonkm)]
- tid: date range 1999-01-01 to 2025-04-01

notes:
- enhed is a measurement selector (70=tons, 80=tonkm). Filter to one.
- korart: 1000=KØRSEL I ALT, 4000=Fra Danmark, 5000=Til Danmark. Only 3 values — no tredjelandskørsel/cabotage breakdown.
- land uses a custom 9-group scheme (TOT, BENE, FRA, ITA, SPA, STO, SVE, NOR, TYS, OVRI). TOT=total. The 8 country groups (BENE through OVRI) sum to TOT. This is NOT joinable to dim.lande_uhv — it's a simplified regional grouping covering major trade partners only.
- For country-level detail use ivg5 (start/end country) or ivg23 (paland/afland with dim.lande_uhv).