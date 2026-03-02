table: fact.bil73
description: Familiernes bilkøb (andele og fordelinger) efter enhed, bystørrelse, købsmønster og tid
measure: indhold (unit Pct.)
columns:
- maengde4: values [50=Procentfordelingen, 60=Andel af det totale bilkøb]
- byst: values [TOT=I alt, HOVEDS=Hovedstadsområdet, 100000=100.000 indbyggere og derover, 50000=50.000-99.999 indbyggere, 40000=40.000-49.999 indbyggere, 30000=30.000-39.999 indbyggere, 29000=20.000-29.999 indbyggere, 10000=10.000-19.999 indbyggere, 5000=5.000-9.999 indbyggere, 2000=2.000-4.999 indbyggere, 1000=1.000-1.999 indbyggere, 500=500-999 indbyggere, 201=200-499 indbyggere, LAND=Landdistrikter, UOPBY=Uoplyst bystørrelse]
- koebmoens: values [10000=Familier i alt, 10010=Familier der Ikke har købt bil i alt, 10020=Familier der har købt bil i alt, 10030=Familier der har købt 1 bil i alt, 10040=Familier der har købt personbil ... 10142=Familier der har købt 1 personbil og leaset 2 personbiler, 10144=Familier der har købt 2 varebiler og leaset 1 personbiler, 10146=Familier der har købt 1 varebil og leaset 2 personbiler, 10148=Familier der har købt 1 varebil, 1 personbil og leaset 1 personbil, 10149=Familier der har købt eller leaset mere end 3 biler]
- tid: date range 2016-01-01 to 2024-01-01
notes:
- maengde4 is a MEASUREMENT SELECTOR: always filter to 50 (within-city-size %) OR 60 (share of all DK car purchases). Omitting doubles every row.
- byst structure same as bil72: TOT=grand total, HOVEDS=capital area aggregate (not part of numeric size bands), numeric bands (201–100000) + LAND + UOPBY cover non-capital Denmark.
- Only from 2016.
