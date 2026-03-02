table: fact.itav12
description: Andel af virksomheder med e-handel (10+ ansatte) efter virksomhedsstørrelse, branche (DB07), emner og tid
measure: indhold (unit Pct.)
columns:
- virkstrrda: values [1010=Alle virksomheder (mindst 10 ansatte), 1110=10-49 ansatte, 1120=50-99 ansatte, 1130=100-249 ansatte, 1140=250 ansatte og derover]
- brancherev2: values [ITATOT=Alle virksomhedsbrancher (private, ikke-finansielle byerhverv), ITAC=10-39 Industri mv., ITAF=41-43 Bygge og anlæg, ITAGHI=45-56 Handel og transport mv., ITAJ=58-63 Information og kommunikation, ITALMN2=68-75, 77-82, 95.1 Erhvervsservice (2021-), ITALMN=68-74, 77-82, 95.1 Erhvervsservice (-2020)]
- emner: values [7610=1. E-salg (web-salg eller EDI salg), 7615=2. E-salg til Danmark, 7620=3. E-salg til udland (andre EU-lande eller resten af verden), 7625=3.1 E-salg til andre EU-lande, 7630=3.2 E-salg til resten af verden ... 7690=10.2 Web-salg til andre virksomheder eller offentlige institutioner, 7695=11.1 Web salg fra egne hjemmesider eller apps, 7700=11.2 Web salg fra digitale markedsplatforme, 7705=12. E-køb (afgivet online ordre), 7710=13. E-køb i udland (afgivet online ordre til udland)]
- tid: date range 2008-01-01 to 2025-01-01
notes:
- All values are percentages of companies with e-commerce activity — never sum across emner; each code is an independent question.
- emner is hierarchical: 7610 (e-salg i alt) is the broadest parent covering both web-salg and EDI. Sub-codes break down by geography (Danmark/EU/resten af verden) and channel (hjemmeside, digitale platforme, EDI). Pick the level you need.
- virkstrrda 1010 is the total; 1110–1140 are size breakdowns. Don't sum them.
- brancherev2 break: ITALMN covers ≤2020, ITALMN2 covers 2021+. Use WHERE brancherev2 IN ('ITALMN', 'ITALMN2') for time series spanning 2008–2025.
- Longest e-commerce series (from 2008). Pair with itav13 when you also need the % of turnover (not just the share of companies).
