table: fact.kv2mo3
description: Forbrug af sport og motion efter type af sport og motion, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- typsport: values [41530=Badminton, 41540=Bordtennis, 41550=Cykling, 41560=Dans, 41570=Fitness eller styrketræning, 41580=Fodbold, 41590=Golf, 41600=Gymnastik, 41610=Hold-boldspil, 41620=Løb, 41630=Rulle- eller street-aktiviteter, 41640=Svømning, 41650=Tennis, padeltennis eller squash, 41660=Vandreture eller gåture, 41670=Vandsport, 41680=Yoga, 41690=Andre sports- eller motionstyper]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- typsport values are NOT mutually exclusive — people do multiple types of sport. Values sum to ~235% for kon=10, alder=TOT. Each row = "X% of sport/motion consumers do this type".
- Single time point (2024 only) — no time series. Compare with idrvan1a for adults (from 2007) or idrvan9a for children.
- kon 10=i alt, alder TOT=i alt.