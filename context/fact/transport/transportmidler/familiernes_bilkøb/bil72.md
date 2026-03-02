table: fact.bil72
description: Familiernes bilkøb (faktiske tal) efter bystørrelse, købsmønster og tid
measure: indhold (unit Antal)
columns:
- byst: values [TOT=I alt, HOVEDS=Hovedstadsområdet, 100000=100.000 indbyggere og derover, 50000=50.000-99.999 indbyggere, 40000=40.000-49.999 indbyggere, 30000=30.000-39.999 indbyggere, 29000=20.000-29.999 indbyggere, 10000=10.000-19.999 indbyggere, 5000=5.000-9.999 indbyggere, 2000=2.000-4.999 indbyggere, 1000=1.000-1.999 indbyggere, 500=500-999 indbyggere, 201=200-499 indbyggere, LAND=Landdistrikter, UOPBY=Uoplyst bystørrelse]
- koebmoens: values [10000=Familier i alt, 10010=Familier der Ikke har købt bil i alt, 10020=Familier der har købt bil i alt, 10030=Familier der har købt 1 bil i alt, 10040=Familier der har købt personbil ... 10142=Familier der har købt 1 personbil og leaset 2 personbiler, 10144=Familier der har købt 2 varebiler og leaset 1 personbiler, 10146=Familier der har købt 1 varebil og leaset 2 personbiler, 10148=Familier der har købt 1 varebil, 1 personbil og leaset 1 personbil, 10149=Familier der har købt eller leaset mere end 3 biler]
- tid: date range 2016-01-01 to 2024-01-01
notes:
- byst=TOT is the grand total. The remaining codes are NOT all equivalent: HOVEDS (Hovedstadsområdet) is a special aggregate that replaces the fine-grained size bands for the entire capital area — it does NOT appear in the numeric size-band codes. Structure is: TOT = HOVEDS + size bands (201–100000) + LAND + UOPBY. Verified: HOVEDS (~787k) + all numeric bands + LAND + UOPBY = TOT.
- Only available from 2016. Use bil600 for regional breakdown going back to 2006.
- koebmoens same hierarchy as bil600: use 10020 for "bought car".
