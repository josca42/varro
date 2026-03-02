table: fact.kv2urb
description: Forbrug af kulturaktiviteter efter kulturaktivitet, køn og alder, urbaniseringsgrad og tid
measure: indhold (unit Pct.)
columns:
- kultur: values [10100=Har set film, 10200=Har set serier, 10300=Har lyttet til musik, 10400=Har læst eller lyttet til bøger, 10500=Har læst, lyttet til eller set nyheder, 10600=Har brugt sociale medier, 10700=Har spillet digitale spil, 10800=Har dyrket sport eller motion, 20100=Har været i biografen, 20200=Har været til koncert eller musikfestival, 20300=Har set scenekunst eller sceneforestillinger live, på internettet eller i TV, 20400=Har opsøgt billedkunst fysisk eller digitalt, 20500=Har været fysisk på biblioteket, 20600=Har benyttet bibliotekernes digitale tjenester, 20700=Har overværet sportsbegivenhed som tilskuer, 20800=Har været på museum, 20900=Har besøgt dansk kulturarv]
- koal: values [0=I alt, 1=Mænd, 2=Kvinder, 3=16-24 år, 4=25-34 år, 5=35-44 år, 6=45-54 år, 7=55-64 år, 8=65-74 år, 9=75 år og derover]
- urbangrad: values [0=Hele landet, 100=Tætbefolket område, 200=Mellembefolket område, 300=Tyndtbefolket område]
- tid: date range 2024-01-01 to 2025-04-01
notes:
- koal combines gender and age into a single column: 0=I alt, 1=Mænd, 2=Kvinder, 3–9=age groups (16-24 through 75+). Unlike kv2hoved there is no separate kon and alder column — they are merged. For the total across all gender/age: koal='0'.
- urbangrad='0' is the national total (hele landet); 100/200/300 are the three urbanisation bands. Filter to one urbangrad value at a time.
- For national totals: filter koal='0' AND urbangrad='0'. Quarterly updates; annual counterpart is kv2aurb.
