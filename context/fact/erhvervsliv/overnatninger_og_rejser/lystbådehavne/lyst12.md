table: fact.lyst12
description: Lystbådehavne efter størrelse, kapacitet og tid
measure: indhold (unit Antal)
columns:
- storrelse: values [505=Lystbådehavne med faste bådepladser i alt, 510=Lystbådehavne med under 50 faste bådepladser, 515=Lystbådehavne med 50-99 faste bådepladser, 520=Lystbådehavne med 100-199 faste bådepladser, 525=Lystbådehavne med 200-299 faste bådepladser, 530=Lystbådehavne med 300-399 faste bådepladser, 535=Lystbådehavne med 400-499 faste bådepladser, 540=Lystbådehavne med 500-599 faste bådepladser, 545=Lystbådehavne med 600 eller derover faste bådepladser, 550=Lystbådehavne med uoplyst antal faste bådepladser]
- kapacitet: values [3025=Lystbådehavne, 3030=Faste bådepladser, 3035=Gæstebådsovernatninger, 3040=Personovernatninger]
- tid: date range 1992-01-01 to 2024-01-01

notes:
- kapacitet is a measure selector — 4 completely different metrics sharing one column. Always filter to exactly one: 3025=antal lystbådehavne (count of marinas), 3030=faste bådepladser (fixed berths), 3035=gæstebådsovernatninger (guest boat nights), 3040=personovernatninger (person nights). Summing across kapacitet is meaningless.
- storrelse groups marinas by size (number of fixed berths). 505=all marinas combined (national total). 510–545=size brackets, 550=unknown size. Summing 510–550 should equal 505.
- No periode column — no overcounting risk from time aggregation. Each row is an annual snapshot.
- Example: to get total fixed berths across all marinas: WHERE f.storrelse='505' AND f.kapacitet='3030'.