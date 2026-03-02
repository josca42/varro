table: fact.kv2sc4
description: Scenekunstnere efter kunstnertype, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- ktyp: values [41210=Udøver scenekunst som professionel scenekunstner, 41220=Udøver scenekunst som amatørkunstner]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- All values are survey percentages from Kulturvaneundersøgelsen 2024. Single snapshot.
- ktyp: only 2 values — professionel (41210) vs amatør (41220). These are not mutually exclusive (someone could be both). Do not sum.
- kon: 10=Køn i alt. Filter to one.
- alder: TOT=Alder i alt is the aggregate. Filter to one.
- This table is about practicing performing arts (as a performer), not consuming it. Contrast with kv2sc1–3 which are about audience consumption.