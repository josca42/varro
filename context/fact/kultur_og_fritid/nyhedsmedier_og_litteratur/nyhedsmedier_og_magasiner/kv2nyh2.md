table: fact.kv2nyh2
description: Forbrug af skriftlige medier og nyhedspodcasts efter adgang, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- adgang: values [40400=Abonnerer på netavis, 40410=Abonnerer på kombineret trykt avis og netavis, 40420=Abonnerer på udenlandsk trykt avis eller netavis, 40430=Abonnerer på (betaler for) nyhedspodcast, 40440=Gratis nyhedspodcast, 40450=Gratis netavis eller nyhedsapps, 40460=Gratis udenlandsk trykt avis eller gratis udenlandske nyhedsartikler på nettet, 40470=Via familie, venner eller bekendte, 40480=Via arbejde eller uddannelse, 40490=Køber avis i løssalg, 41880=Andre adgange]
- koen: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey data (2024 only). indhold is Pct. of people who access written news/podcasts via each channel.
- adgang values are NOT mutually exclusive — a person can have multiple subscriptions or access types. The 11 adgang values sum to 147% for koen='10'/alder='TOT'. Never sum across adgang.
- koen='10' = Køn i alt (total); alder='TOT' = Alder i alt (total). Filter to these for overall rates.
- Covers paid subscriptions, free access, and podcast access — more granular than kv2nyh1's general channel categories.