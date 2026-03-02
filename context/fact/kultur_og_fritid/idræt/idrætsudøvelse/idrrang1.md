table: fact.idrrang1
description: Rangering af samlet præstation i OL-discipliner efter disciplin, land, præstation, rangplacering og tid
measure: indhold (unit Antal)
columns:
- diciplin: values [OLSOM=Discipliner ved Sommer-OL , OLVIN=Discipliner ved Vinter-OL]
- land: values [5100=Danmark, 5706=Belarus, 5126=Belgien, 5128=Bulgarien, 5104=Finland ... 5444=Japan, 5448=Kina, 5484=Sydkorea, 5502=Australien, 5514=New Zealand]
- praestation: values [WIN005=Guldmedalje/1. plads, WIN010=Medaljer/Podie, WIN015=Top-8-placeringer]
- rang: values [RANG05=Alle lande, RANG10=Lande under 10 mio. indbyggere]
- tid: date range 2016-01-01 to 2024-01-01

notes:
- indhold = rank position (lower = better). E.g., Denmark ranked 21st among all countries for gold medals at sommer-OL 2021.
- praestation values are nested (guldmedalje ≤ medaljer ≤ top-8). Filter to one praestation value per query.
- rang filters the peer group: RANG05 = ranked among alle lande, RANG10 = ranked among lande med <10 mio. indbyggere. Pick one.
- land does NOT include TOT (unlike idrres01). Only individual countries are ranked.
- Typical Denmark query: `WHERE land='5100' AND diciplin='OLSOM' AND praestation='WIN010' AND rang='RANG10'`.