table: fact.kv2sm1
description: Forbrug af sociale medier efter socialt medie, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- some: values [42620=BeReal, 42630=Facebook, 42640=Instagram, 42650=LinkedIn, 42660=Messenger, 42670=Pinterest, 42680=Reddit, 42690=Snapchat, 42700=TikTok, 42710=Twitch, 42720=WhatsApp, 42730=X (Twitter), 42740=YouTube, 42750=Andre sociale medier]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- kon='10' = køn i alt; alder='TOT' = alder i alt. Filter to these for national totals.
- some (social media platform) values are NOT mutually exclusive — a person can use multiple platforms. Values sum to ~470% for the total population. Each row is an independent % of population using that platform. Never sum across some values.
- Note: 'some' is a reserved word in SQL. Quote it: SELECT f."some", ... FROM fact.kv2sm1 f.
- 2024 data only.
