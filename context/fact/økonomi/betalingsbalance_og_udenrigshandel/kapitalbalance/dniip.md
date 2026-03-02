table: fact.dniip
description: Kapitalbalancen - beholdning af Danmarks aktiver og passiver overfor udlandet efter balance, instrument, indenlandsk sektor, valuta, land, udenlandsk sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- balanc: values [A=Aktiver, P=Passiver, N=Nettoaktiver]
- instrument: values [100.0=1.0: Alle finansielle poster, 200.0=2.0: Direkte investeringer, 300.0=3.0: Porteføljeinvesteringer, 310.0=3.1: Aktier, 320.0=3.2: Investeringsforeningsbeviser, 330.0=3.3: Obligationer, 400.0=4.0: Finansielle derivater, 500.0=5.0: Andre investeringer (lån, handelskreditter mv.), 600.0=6.0: Reserveaktiver]
- indsek: values [1000=1000: Alle indenlandske sektorer, 1100=1100: Ikke-finansielle selskaber, 1200=1200: Finansielle selskaber, 1221=1221: Heraf pengeinstitutter, 1240=1240: Heraf investeringsforeninger, 12FP=12FP: Heraf forsikringsselskaber og pensionskasser, 1300=1300: Offentlig forvaltning og service, 1400=1400: Husholdninger mv.]
- valuta: values [Z01=Alle valutaer, DKK=Danske kroner]
- land: values [Z9=Udlandet i alt, B5=EU-27 ekskl. Danmark, I7=Euroområdet, R12=Offshore centre]
- udsek: values [1000.0=1000: Alle udenlandske sektorer, 1100.0=1100: Ikke-finansielle selskaber, 1200.0=1200: Finansielle selskaber, 1221.0=1221: Heraf pengeinstitutter, 1300.0=1300: Offentlig forvaltning og service, 1400.0=1400: Husholdninger mv.]
- tid: date range 2005-01-01 to 2025-04-01

notes:
- balanc: N=Nettoaktiver is derived (Aktiver − Passiver). Never sum across A, P, and N together — pick one.
- instrument is hierarchical: 100=alle finansielle poster (total), sub-categories are 200=direkte investeringer, 300=porteføljeinvesteringer (→310 aktier, 320 investeringsforeningsbeviser, 330 obligationer), 400=finansielle derivater, 500=andre investeringer, 600=reserveaktiver. Don't mix aggregate and sub-item codes in a SUM. Note: the fact doc shows codes as "100.0", "200.0" etc. but the actual DB values are the integer strings "100", "200" etc.
- indsek: 1000=alle indenlandske sektorer (total). 12FP is a sub-component of 1200 — not a peer sector. Use indsek='1000' for all-sector totals.
- udsek: 1000=alle udenlandske sektorer (total). 1221 (pengeinstitutter) is a sub-component of 1200, not a peer. Use udsek='1000' for all-sector totals.
- land only has 4 aggregate geographic codes: Z9=Udlandet i alt, B5=EU-27 ekskl. Danmark, I7=Euroområdet, R12=Offshore centre. There is no individual country breakdown — use dnpi for that.
- valuta: Z01=Alle valutaer is the aggregate; DKK is a subset.
- Minimal working query (total Danish net foreign position, 2024): WHERE balanc='N' AND instrument='100' AND indsek='1000' AND valuta='Z01' AND land='Z9' AND udsek='1000' AND tid='2024-01-01'.