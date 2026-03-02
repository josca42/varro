table: fact.skib431
description: International godsomsætning på danske havne efter havn, retning, godsart og tid
measure: indhold (unit 1.000 ton)
columns:
- havn: values [0=HAVNE I ALT, 1000=LANDSDEL BYEN KØBENHAVN, 25=Københavns Havn, 2000=LANDSDEL KØBENHAVNS OMEGN, 10=Avedøreværkets Havn ... 790=Skagen Havn, 720=Thisted Havn, 795=Vesterø Havn, 730=Aalborg Havn, 735=Aalborg Portland Havn]
- ret: values [1184=INDGÅENDE OG UDGÅENDE GODS I ALT, 1186=Indgående gods, 1188=Udgående gods]
- gods: values [100=GODS I ALT, 900=Flydende gas, 905=Råolie, 910=Mineralske olieprodukter, 915=Flydende kemikalier ... 980=Færgegods, 985=Ro-ro-gods i øvrigt, 990=Træ, 995=Jern- og stålprodukter, 1000=Stykgods i øvrigt]
- tid: date range 2007-01-01 to 2024-01-01
notes:
- Three columns all have aggregate codes that inflate results if not filtered: havn (0=HAVNE I ALT, plus LANDSDEL aggregate codes), ret (1184=I alt), gods (100=GODS I ALT). For any meaningful query, filter all three to avoid double-counting.
- ret has 3 values: 1184=INDGÅENDE OG UDGÅENDE I ALT, 1186=Indgående gods, 1188=Udgående gods. Filter to 1186 or 1188 for directional analysis, 1184 for combined.
- gods: 100=GODS I ALT is the only aggregate; the other ~21 codes (900–1000) are individual cargo types. Summing them all equals code 100. Use gods='100' for totals or pick specific types.
- havn has the same LANDSDEL aggregate structure as skib421. Use ColumnValues("skib431", "havn") to browse ports.
- This table covers international trade only. Use skib451 for domestic (national) flows with the same port/direction/cargo breakdown.
