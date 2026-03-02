table: fact.kv2sp6
description: Forbrug af digitale spil efter samværdstype, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- samtype: values [42510=Flere i samme rum, 42520=Online, 42530=Både i samme rum og online]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- kon='10' = køn i alt; alder='TOT' = alder i alt. Filter to these for national totals.
- samtype has 3 values (fysisk i samme rum / online / begge). The "begge" (both) category means these are NOT strictly mutually exclusive as a share of all gamers. Do not sum the three values — the total would exceed 100% for active multiplayer gamers.
- 2024 data only.
