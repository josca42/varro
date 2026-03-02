table: fact.nfisk
description: Nøgletal for fiskeri efter fartøjslængde, regnskabsposter og tid
measure: indhold (unit -)
columns:
- farlaengd: values [9=ALLE VIRKSOMHEDER, 10=FARTØJER UNDER 12 METER, 40=Garn/krog under 12 m, 48=Jolle/ruse under 12 m, 50=Snur/garn/trawl under 12 m ... 20=FARTØJER 40,0 METER OG OVER, 78=Trawl industri over 40 m, 82=Not/trawl andet over 40 m, 84=HESTEREJEFISKERI, 86=MUSLINGEFISKERI]
- regnskposter: values [H115=H.3 Ejeraflønning (beregnet), 1000 kr., P200=P.2 Overskudsgrad, pct., P300=P.3 Afkastningsgrad, pct., P400=P.4 Soliditetsgrad, pct.]
- tid: date range 2009-01-01 to 2023-01-01

notes:
- nfisk has only 4 regnskposter: H115 (ejeraflønning, 1000 kr), P200 (overskudsgrad %), P300 (afkastningsgrad %), P400 (soliditetsgrad %). Mixed units — H115 is money, P200/P300/P400 are percentages. Never sum across regnskposter.
- Same farlaengd two-tier hierarchy as firegn1/firegn2. Filter to size-class aggregates (9, 10, 12, 14, 16, 18, 20) or gear subcategories (40-86), not both.
- For a financial overview of the fishing sector, nfisk gives the four key ratios; for deeper accounting detail use firegn1 (totals) or firegn2 (per-vessel).