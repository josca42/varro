table: fact.skib72
description: Godsomsætning på større danske havne efter havn, retning, godsart og tid
measure: indhold (unit 1.000 ton)
columns:
- havn: values [0=HAVNE I ALT, 10=Avedøreværkets Havn, 12=Avedøre Råstofhavn, 25=Københavns Havn, 45=Helsingør Havn ... 730=Aalborg Havn, 735=Aalborg Portland Havn, 750=Frederikshavn Havn, 765=Hirtshals Havn, 785=Nordjyllandsværkets Havn]
- ret: values [1184=INDGÅENDE OG UDGÅENDE GODS I ALT, 1190=Indgående gods i alt, 1195=Indgående gods fra udland, 1200=Indgående gods fra indland, 1205=Udgående gods i alt, 1210=Udgående gods til udland, 1215=Udgående  gods til indland]
- gods: values [100=GODS I ALT, 102=FRAGTSKIBSGODS I ALT, 900=Flydende gas, 905=Råolie, 910=Mineralske olieprodukter ... 985=Ro-ro-gods i øvrigt, 990=Træ, 995=Jern- og stålprodukter, 1000=Stykgods i øvrigt, 1002=FÆRGEGODS I ALT]
- tid: date range 2000-01-01 to 2025-04-01
notes:
- Three columns all have hierarchical aggregate codes — always filter each to a single level: havn (0=I ALT), ret (7-level hierarchy), gods (3 aggregate codes).
- ret hierarchy: 1184=I alt → 1190=Indgående i alt → 1195 fra udland + 1200 fra indland; 1205=Udgående i alt → 1210 til udland + 1215 til indland. Filter to exactly one ret code.
- gods aggregate codes: 100=GODS I ALT (fragtskibe + færger combined), 102=FRAGTSKIBSGODS I ALT, 1002=FÆRGEGODS I ALT. The ~20 individual cargo type codes (900–1000) sum to 102. Choosing gods='100' gives all goods; gods='102' gives freight-ship goods only.
- havn: code 0=I ALT plus ~35 larger ports (no LANDSDEL aggregate rows unlike skib421/431). Use ColumnValues("skib72", "havn") for port labels.
- This is the most current table for port-by-cargo analysis (data through 2025), combining both freight ships and ferries. Use skib431 for all ports (including smaller ones, from 2007) or skib47 for flag-state breakdown.
