table: fact.kv2kar3
description: Besøg på dansk kulturarv efter seværdighed, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- sevaerd: values [30710=Jelling-monumentet, 30720=Roskilde Domkirke, 30730=Brødremenighedens By Christiansfeld, 30740=Parforcejagtlandskabet (i Nordsjælland), 30750=Kronborg Slot, 30760=Stevns Klint, 30770=Vadehavet, 30780=Vikingetidens ringborge]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- indhold is percentage (Pct.) of kulturarv visitors who visited each UNESCO/landmark site. Categories are NOT mutually exclusive — sums to 63% across all sevaerd. Compare individual site rates, never sum.
- 8 specific sites: Jelling (8%), Roskilde Domkirke (9%), Christiansfeld (5%), Parforcejagtlandskabet (3%), Kronborg (12%), Stevns Klint (8%), Vadehavet (12%), Vikingeborge (6%).
- Single year only (2024) — no trend analysis possible.