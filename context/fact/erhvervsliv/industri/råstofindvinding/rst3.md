table: fact.rst3
description: Råstoffer indvundet fra Farvande (1000 m3) efter område, råstoftype og tid
measure: indhold (unit 1.000 m3)
columns:
- omrade: values [TOT=I alt, NORDSØ=Nordsøen, SKAGERAK=Skagerrak, LIMFJORD=Limfjorden, KATTEGAT5=Kattegat omkring Læsø, KATTEGAT4=Kattegat omkring Anholt, KATTEGAT3=Kattegat omkring Hesselø, KATTEGAT2=Kattegat øst for Samsø, KATTEGAT1=Kattegat vest for Samsø, LILLEBÆLT=Lillebælt, STOREBÆLT=Storebælt, ØRESUND=Øresund, FARVAND=Farvandet syd for Fyn, SMÅLAND=Smålandsfarvandet, ØSTER1=Østersøen omkring Bornholm, ØSTER2=Østersøen omkring Møn, ØSTER3=Østersøen omkring Gedser]
- rastoftype: values [TOTHAV=SAMLET INDVINDING PÅ HAV, SAND1=Sand, RAL=Ral og sten, GRUS=Grus, FYLD=Fyldsand, GRABSØ=Grabsten og søsten, SKALLER=Skaller, ANDET=Andet]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- omrade is fully inline — no dim join. 17 named sea areas: Nordsøen, Skagerrak, Limfjorden, 5 Kattegat zones (KATTEGAT1–5), Lillebælt, Storebælt, Øresund, FARVAND (syd for Fyn), Smålandsfarvandet, ØSTER1–3 (Østersøen around Bornholm/Møn/Gedser). TOT = sum across all areas.
- This table tracks extraction location (where material was harvested from the seabed). Compare with rst04, which tracks landing location (where the ship unloaded). Use rst3 when the question is about which sea area the materials came from.
- rastoftype TOTHAV = aggregate total. Filter `WHERE rastoftype != 'TOTHAV'` when summing across types. Same 7 individual types as rst04: SAND1, RAL, GRUS, FYLD, GRABSØ, SKALLER, ANDET.
- Longest historical series among the sea tables: 1990–2024. rst04 starts in 2007.
- indhold unit is 1.000 m³.