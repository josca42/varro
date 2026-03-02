table: fact.ppp11
description: Købekraftkorrigerede indeks og værdier per indbygger efter varegrupper, land, enhed og tid
measure: indhold (unit -)
columns:
- vargr: values [A0=BNP, A01=Faktisk individuelt forbrug, A04=Faktisk kollektivt forbrug, A05=Faste bruttoinvesteringer, E01=Forbrugsudgift, E011=Husholdningernes endelige forbrug, E012=Offentlig forbrugsudgift , E0121=Kollektiv forbrugsudgift, E0122=Individuel forbrugsudgift ]
- land: join dim.lande_uhv on land=kode [approx]; levels [4]
- tal: values [30=Købekraftkorrigerede indeks per indbygger (indeks EU-15 = 100), 35=Købekraftkorrigerede indeks per indbygger  (indeks EU-27 = 100), 38=Købekraftkorrigerede indeks per indbygger (indeks EU-28 = 100), 39=Købekraftkorrigerede indeks per indbygger (Indeks EU-27 (uden Storbritannien) = 100), 40=Købekraftkorrigerede værdier per indbygger (PPS_EU-15), 45=Købekraftkorrigerede værdier per indbygger (PPS_EU-27), 48=Købekraftkorrigerede værdier per indbygger (PPS_EU-28), 49=Købekraftkorrigerede værdier per indbygger (PPS_EU-27 (uden Storbritannien))]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/lande_uhv.md

notes:
- Column is `vargr` (not `varegr` as in table ppp) — note the spelling difference.
- `tal` is the mandatory measurement selector. Two families: købekraftkorrigerede indeks per indbygger (30/38/39) and PPS-værdier per indbygger (40/48/49). Suffix indicates EU baseline: EU-15 (30/40), EU-28 (38/48), EU-27 uden UK (39/49). Always filter to one tal value. Prefer 39/49 for the most current baseline.
- `vargr` has 9 codes at mixed hierarchy levels: A0 (BNP), A01 (faktisk individuelt forbrug), A04 (kollektivt forbrug), A05 (bruttoinvesteringer), E01 (forbrugsudgift), E011 (husholdninger), E012 (offentlig forbrugsudgift), E0121 (kollektiv), E0122 (individuel). Parent and child codes coexist (e.g. E01 contains E011 and E012) — don't sum across all.
- Same `land` mismatch as ppp: DK and EU aggregate codes (U2, D2, D3, V3, V5, RS) not in dim.lande_uhv — use directly without joining.
- This table is for per capita comparisons only — if you need PPP or price level data across all expenditure categories, use ppp instead.