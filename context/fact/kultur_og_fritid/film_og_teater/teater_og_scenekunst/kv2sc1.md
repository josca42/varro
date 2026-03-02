table: fact.kv2sc1
description: Forbrug af scenekunst efter genre, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- genre: values [41030=Teater eller skuespil, 41040=Musical eller teaterkoncert, 41050=Opera eller operette, 41060=Ballet eller scenisk dans, 41070=Standup, 41080=Revy eller kabaret, 41090=Børneteater, dukketeater eller animationsteater, 41100=Nycirkus, performance eller gadeteater, 41110=Skolekomedie eller amatørteater, 42060=Andre genrer]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- All values are survey percentages (Pct.) from Kulturvaneundersøgelsen 2024. Single snapshot — only one year of data.
- genre values are independent: each measures the share who consumed that specific art form. They are NOT mutually exclusive; percentages sum well above 100%. Never sum across genre.
- kon: 10=Køn i alt, 1=Mænd, 2=Kvinder. Filter to one.
- alder: TOT=Alder i alt is the aggregate; the 7 age bands (16-24 to 75+) are non-overlapping. Filter to one. Survey covers population 16+.
- To read a single figure: "X% of [kon] aged [alder] have consumed [genre] in the past year".