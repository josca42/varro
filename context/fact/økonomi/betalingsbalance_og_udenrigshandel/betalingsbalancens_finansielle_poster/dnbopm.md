table: fact.dnbopm
description: Betalingsbalancens finansielle poster - transaktioner mellem Danmark og udlandet efter balance, instrument, indenlandsk sektor, valuta, land og tid
measure: indhold (unit Mio. kr.)
columns:
- balanc: values [A=Aktiver, P=Passiver, N=Nettoaktiver]
- instrument: values [100=1.0: Alle finansielle poster, 200=2.0: Direkte investeringer, 300=3.0: Porteføljeinvesteringer, 310=3.1: Aktier, 320=3.2: Investeringsforeningsbeviser, 330=3.3: Obligationer, 400=4.0: Finansielle derivater, 500=5.0: Andre investeringer (lån, handelskreditter mv.), 600=6.0: Reserveaktiver, V000=A.1: Nettofordringserhvervelsen, V100=A.1.1: Kapitaloverførsler, V200=A.1.2: Løbende poster, V900=A.2: Fejl og udeladelser]
- indsek: values [1000.0=1000: Alle indenlandske sektorer, 1100.0=1100: Ikke-finansielle selskaber, 1200.0=1200: Finansielle selskaber, 1221.0=1221: Heraf pengeinstitutter, 1300.0=1300: Offentlig forvaltning og service, 1400.0=1400: Husholdninger mv.]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- land: join dim.lande_uht_bb on land=kode [approx]
- tid: date range 2005-01-01 to 2025-08-01
dim docs: /dim/lande_uht_bb.md, /dim/valuta_iso.md

notes:
- land and valuta are NOT joinable to their documented dim tables. Both use inline coded values specific to this BoP table. Do not join dim.lande_uht_bb or dim.valuta_iso.
- land has exactly 3 values (no dim join needed): Z9=Udlandet i alt (world total), B5=EU-27 ekskl. Danmark, I7=Euroområdet. B5 and I7 are subsets of Z9 — summing across all three double-counts. Use land='Z9' for world totals.
- valuta has 3 values: Z01=Alle valutaer, DKK=Danske kroner, NULL (no breakdown). Use valuta='Z01' for currency-aggregated totals. NULL rows appear for certain instrument/land combinations and represent missing breakdowns.
- instrument is hierarchical with aggregate totals: 100 = sum of 200+300+400+500+600. 300 = sum of 310+320+330. Filter to a single level to avoid double-counting. The V-codes (V000, V100, V200, V900) are balance-of-payments accounts, not financial instruments.
- indsek is hierarchical: 1000 = sum of 1100+1200+1300+1400. 1221 (pengeinstitutter) is a subset of 1200 — not additive with it. Use indsek=1000 for all-sector totals.
- balanc: N = A − P (Nettoaktiver = Aktiver − Passiver). Never sum across all three balanc values.
- For a clean total (e.g. net financial position by instrument): filter land='Z9', valuta='Z01', indsek=1000, balanc='N', then filter instrument to one level (e.g. 200–600 only, not 100).
- Monthly data from 2005M01 to 2025M08.