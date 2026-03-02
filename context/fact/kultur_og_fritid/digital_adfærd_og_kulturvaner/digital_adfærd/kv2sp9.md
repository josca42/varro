table: fact.kv2sp9
description: Brug af penge på digitale spil efter forbrug, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- forbrug: values [42550=Har købt nye spil til mig selv, 42560=Har købt abonnementer til mig selv, 42570=Har købt mønter, ting og skins til spil, 42580=Har brugt penge på åbning af loot boxes, 42590=Har købt battlepasses eller seasonpasses, 42600=Har købt udvidelser, kapitler eller nye baner til spil, 42610=Har brugt penge på spil på anden vis]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- kon='10' = køn i alt; alder='TOT' = alder i alt. Filter to these for national totals.
- forbrug (spending type) values are NOT mutually exclusive — a person can spend money on multiple types (new games AND abonnements AND skins, etc.). Never sum across forbrug values.
- 2024 data only.
