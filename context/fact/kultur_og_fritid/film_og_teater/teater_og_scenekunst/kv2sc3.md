table: fact.kv2sc3
description: Forbrug af scenekunst efter forestillingens placering, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- forstilplac: values [30390=I lokalområdet (din by eller din omegn), 30400=I Danmark uden for lokalområdet, 30410=I udlandet]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- All values are survey percentages from Kulturvaneundersøgelsen 2024. Single snapshot.
- forstilplac (location of performance attended): 3 categories — lokalområde, Danmark uden for lokalområdet, udlandet. These reflect the most recent live performance attended; not mutually exclusive across time, but typically filter to one for a clean comparison.
- kon: 10=Køn i alt. Filter to one.
- alder: TOT=Alder i alt is the aggregate. Filter to one.