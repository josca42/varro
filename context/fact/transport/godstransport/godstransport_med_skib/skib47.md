table: fact.skib47
description: Fragtskibes godsomsætning på større danske havne efter flagstat, retning, godsart og tid
measure: indhold (unit 1.000 ton)
columns:
- flag: values [901=Danmark, 990=Udlandet]
- ret: values [1184=INDGÅENDE OG UDGÅENDE GODS I ALT, 1190=Indgående gods i alt, 1195=Indgående gods fra udland, 1200=Indgående gods fra indland, 1205=Udgående gods i alt, 1210=Udgående gods til udland, 1215=Udgående  gods til indland]
- gods: values [100=GODS I ALT, 900=Flydende gas, 905=Råolie, 910=Mineralske olieprodukter, 915=Flydende kemikalier ... 975=Uindregistrerede motorkøretøjer, 985=Ro-ro-gods i øvrigt, 990=Træ, 995=Jern- og stålprodukter, 1000=Stykgods i øvrigt]
- tid: date range 1997-01-01 to 2024-01-01
notes:
- flag has only 2 values: 901=Danmark, 990=Udlandet. Always filter to one unless the question is specifically about comparing flag states. Never sum both — that doubles the total.
- ret has 7 values forming a hierarchy: 1184=I alt (total) → 1190=Indgående i alt → 1195 fra udland + 1200 fra indland; 1205=Udgående i alt → 1210 til udland + 1215 til indland. Filter to one level to avoid double-counting.
- gods: 100=GODS I ALT is the aggregate; ~20 individual cargo types (900–1000). Use gods='100' for totals.
- No havn dimension — covers larger ports in aggregate. Goes back to 1997, the longest series with cargo type breakdown.
