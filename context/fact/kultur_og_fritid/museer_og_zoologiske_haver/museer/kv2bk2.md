table: fact.kv2bk2
description: Forbrug af billedkunst efter kunsttype, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- kunsttype: values [30180=Maleri, 30190=Skulptur, 30200=Kunsthåndværk, 30210=Design, 30220=Fotografi, 30230=Installationskunst, 30240=Videokunst, 30250=Performance, 30260=Billedkunst skabt af kunstig intelligens, 30270=Andre typer billedkunst]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- indhold is % of respondents who consumed that type of visual art. kunsttype values are independent — a person appreciates multiple art types. Never sum across kunsttype.
- Filter kon=10 and alder='TOT' for national results. Single year only (2024 survey).