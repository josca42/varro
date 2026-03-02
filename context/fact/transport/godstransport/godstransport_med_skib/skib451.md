table: fact.skib451
description: National godsomsætning på danske havne efter havn, retning, godsart og tid
measure: indhold (unit 1.000 ton)
columns:
- havn: values [0=HAVNE I ALT, 1000=LANDSDEL BYEN KØBENHAVN, 25=Københavns Havn, 2000=LANDSDEL KØBENHAVNS OMEGN, 10=Avedøreværkets Havn ... 790=Skagen Havn, 720=Thisted Havn, 795=Vesterø Havn, 730=Aalborg Havn, 735=Aalborg Portland Havn]
- ret: values [1184=INDGÅENDE OG UDGÅENDE GODS I ALT, 1186=Indgående gods, 1188=Udgående gods]
- gods: values [100=GODS I ALT, 900=Flydende gas, 905=Råolie, 910=Mineralske olieprodukter, 915=Flydende kemikalier ... 980=Færgegods, 985=Ro-ro-gods i øvrigt, 990=Træ, 995=Jern- og stålprodukter, 1000=Stykgods i øvrigt]
- tid: date range 2007-01-01 to 2024-01-01
notes:
- National (domestic/indenrigs) counterpart to skib431 (international). Same column structure: havn, ret, gods — same filtering rules apply.
- ret: filter to one value (1184 total, 1186 indgående, 1188 udgående). Never sum across ret.
- gods: 100=GODS I ALT is the only aggregate; individual cargo types 900–1000. Use gods='100' for totals.
- havn has aggregate codes (0=I ALT, LANDSDEL-level codes) mixed with individual ports. Filter to individual ports or havn='0'. Use ColumnValues("skib451", "havn") for labels.
