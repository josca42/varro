table: fact.ferieh4
description: Antal udlejede hus-uger i feriehuse efter enhed, periode og tid
measure: indhold (unit Antal)
columns:
- enhed: values [2000=I alt udlejede uger, 2010=Danske udlejede uger, 2020=Svenske udlejede uger, 2030=Norske udlejede uger, 2040=Tyske udlejede uger, 2050=Nederlandske udlejede uger, 2060=Uoplyst land udlejede uger, 2080=Disponible huse]
- periode: values [U01=Uge 1, U02=Uge 2, U03=Uge 3, U04=Uge 4, U05=Uge 5 ... U49=Uge 49, U50=Uge 50, U51=Uge 51, U52=Uge 52, U53=Uge 53]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- enhed is a measurement selector where each value is a distinct nationality's leased week count (or total/available). Never sum across enhed values — 2010+2020+2030+2040+2050+2060 = 2000 (I alt). Pick one enhed per query.
- enhed=2080 (Disponible huse) has fewer rows than rental categories (209 vs 888) — it is only available for a subset of year/week combinations.
- periode = week numbers U01–U53. Use string comparison (periode = 'U07') not integer. Some years have U53.
- tid is always Jan 1 of the reporting year (2008–2024). Nationality breakdown goes 2010=Dansk, 2020=Svensk, 2030=Norsk, 2040=Tysk, 2050=Nederlandsk, 2060=Uoplyst land.