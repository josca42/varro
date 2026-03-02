table: fact.kv2mk1
description: Forbrug af musik efter adgang, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- adgang: values [41810=CD, vinylplade eller kasettebånd, 41820=Streamer gratis, 41830=Streamer mod betaling, 41840=Podcast, 41850=Radio, 41860=TV, 41870=Sociale medier eller videodelingsplatforme, 41880=Andre adgange]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Single survey year (2024) — no time series.
- indhold is a percentage (Pct.). adgang categories are multi-select — people use multiple access methods. Categories sum to ~254 for kon=10/alder='TOT'. Never sum across adgang.
- Each row is an independent rate: "X% of respondents access music via this method." Compare individual rows directly (e.g., streaming paid vs. radio) without aggregating.
- Key split: traditional physical (41810 CD/vinyl), free streaming (41820), paid streaming (41830), broadcast (41850 radio, 41860 TV), digital-social (41870 sociale medier/video).
- Filter to kon=10 AND alder='TOT' for population totals.