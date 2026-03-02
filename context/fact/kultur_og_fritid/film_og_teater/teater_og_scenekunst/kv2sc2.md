table: fact.kv2sc2
description: Forbrug af scenekunst efter adgang, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- adgang: values [41130=Liveforestillinger, 41140=I tv, 41150=Livestreaming, 41160=Streaming af optagede forestillinger, 41170=På DVD o.lign., 41180=På YouTube eller andre videodelingstjenester, 41190=I biografen, 41200=Andre måder]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- All values are survey percentages from Kulturvaneundersøgelsen 2024. Single snapshot.
- adgang (access method) values are NOT mutually exclusive — a respondent can have used multiple ways (e.g., both live and streaming). Never sum across adgang.
- kon: 10=Køn i alt, 1=Mænd, 2=Kvinder. Filter to one.
- alder: TOT=Alder i alt is the aggregate; 7 age bands are non-overlapping. Filter to one.