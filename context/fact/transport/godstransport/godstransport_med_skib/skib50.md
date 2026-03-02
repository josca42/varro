table: fact.skib50
description: International godsomsætning på større danske havne efter retning, land, godsart og tid
measure: indhold (unit 1.000 ton)
columns:
- ret: values [1184=INDGÅENDE OG UDGÅENDE GODS I ALT, 1186=Indgående gods, 1188=Udgående gods]
- land: join dim.lande_uhv on land=kode [approx]; levels [4]
- gods: values [100=GODS I ALT, 900=Flydende gas, 905=Råolie, 910=Mineralske olieprodukter, 915=Flydende kemikalier ... 980=Færgegods, 985=Ro-ro-gods i øvrigt, 990=Træ, 995=Jern- og stålprodukter, 1000=Stykgods i øvrigt]
- tid: date range 2004-01-01 to 2024-01-01
dim docs: /dim/lande_uhv.md
notes:
- land joins dim.lande_uhv at ~76% match — same issue as skib44. The 10 unmatched codes are special aggregates: IA=I alt, EUA=Europa i øvrigt, AC1=Afrika nord, AC2=Afrika vest, AC3=Afrika i øvrigt, E10=Syd og Mellemamerika, E2=Nær- og Mellemøsten, F2=Asien, Z5=Uoplyst land, CS=Serbien og Montenegro. Use ColumnValues("skib50", "land") instead of dim.lande_uhv to get the full label mapping.
- ret: filter to one value (1184 total, 1186 indgående, 1188 udgående).
- gods: 100=GODS I ALT is the only aggregate; individual cargo types 900–1000. Use gods='100' for totals or pick specific cargo types.
- No havn column — this is the country-by-cargo cross-table for larger ports in aggregate. Use skib44 if you need port breakdown by country (but no cargo type). Use skib431 for port+cargo breakdown (but no country detail).
- Available from 2004, covers the same port population as skib44 and skib72.
