table: fact.dnpi
description: Porteføljeinvesteringer - danske porteføljeinvesteringer i udlandet efter datatype, instrument, indenlandsk sektor, valuta, land og tid
measure: indhold (unit Mio. kr.)
columns:
- data: values [1=Beholdninger, 2=Transaktioner]
- instrument: values [300=3.0: Porteføljeinvesteringer, 310=3.1: Aktier, 310N=3.1.1: Noteret, 310U=3.1.2:  Unoteret, 320=3.2: Investeringsforeningsbeviser, 330=3.3: Obligationer, 330S=3.3.1: Obligationer med oprindelig løbetid op til og med 1 år, 330L=3.3.2: Obligationer med oprindelig løbetid over 1 år]
- indsek: values [1000=1000: Alle indenlandske sektorer, 1100=1100: Ikke-finansielle selskaber, 1200=1200: Finansielle selskaber, 12FP=12FP: Heraf forsikringsselskaber og pensionskasser, 1300=1300: Offentlig forvaltning og service, 1400=1400: Husholdninger mv.]
- valuta: values [Z01=Alle valutaer, DKK=Danske kroner]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [4]
- tid: date range 2005-01-01 to 2025-09-01
dim docs: /dim/lande_uht_bb.md

notes:
- data is a measurement selector: 1=Beholdninger (positions/stocks), 2=Transaktioner (flows). Always filter to one — mixing them doubles the row count silently.
- instrument is hierarchical: 300 is the top-level total (alle porteføljeinvesteringer). Sub-items: 310=Aktier (→310N Noteret, 310U Unoteret), 320=Investeringsforeningsbeviser, 330=Obligationer (→330S short, 330L long). Never mix aggregate and leaf codes in a SUM.
- indsek=1000 is the aggregate total (alle indenlandske sektorer). 12FP (forsikringsselskaber og pensionskasser) is a sub-component of 1200 — don't add it to peers. Use 1000 for totals.
- valuta: Z01=Alle valutaer is the currency-neutral aggregate; DKK is a subset. Use Z01 for totals.
- land joins dim.lande_uht_bb, but only at niveau=4 (individual countries). The table has exactly 10 countries + 4 aggregate codes that are NOT in the dim table: Z9=Udlandet i alt, B5=EU-27 ekskl. Danmark, I7=Euroområdet, R12=Offshore centre. To get individual countries, join with WHERE d.niveau=4. To use aggregates, filter directly on f.land without a join (e.g. WHERE f.land='Z9'). Use ColumnValues("lande_uht_bb", "titel", for_table="dnpi") to see the 10 individual countries available.
- Minimal working query (Danish holdings abroad, all countries total, 2024): WHERE data='1' AND indsek='1000' AND valuta='Z01' AND land='Z9' AND instrument='300' AND tid='2024-01-01'.