table: fact.itav13
description: Virksomhedernes andel af omsætning og køb fra e-handel (10+ ansatte) efter virksomhedsstørrelse, branche (DB07), emner og tid
measure: indhold (unit Pct.)
columns:
- virkstrrda: values [1010=Alle virksomheder (mindst 10 ansatte), 1110=10-49 ansatte, 1120=50-99 ansatte, 1130=100-249 ansatte, 1140=250 ansatte og derover]
- brancherev2: values [ITATOT=Alle virksomhedsbrancher (private, ikke-finansielle byerhverv), ITAC=10-39 Industri mv., ITAF=41-43 Bygge og anlæg, ITAGHI=45-56 Handel og transport mv., ITAJ=58-63 Information og kommunikation, ITALMN2=68-75, 77-82, 95.1 Erhvervsservice (2021-), ITALMN=68-74, 77-82, 95.1 Erhvervsservice (-2020)]
- emner: values [7810=1. E-salgs andel af omsætningen (web-salg eller EDI salg), 7815=2. E-salg til Danmark (andel af omsætning), 7820=3. E-salg til udland (andel af omsætning), 7825=3.1 E-salg til andre EU-lande (andel af omsætning), 7830=3.2 E-salg til resten af verden (andel af omsætning) ... 7905=13.2 Web-salg til andre virksomheder eller offentlige institutioner (andel af omsætning), 7910=14.1 Web salg fra egne hjemmesider eller apps (andel af omsætning), 7915=14.2 Web salg fra digitale markedsplatforme (andel af omsætning), 7920=15. E-købs andel af samlet køb (indenlandsk køb og import), 7925=16. E-køb fra udland (andel af samlet køb)]
- tid: date range 2013-01-01 to 2025-01-01
notes:
- Measures e-commerce as a share of turnover/purchases (Pct.) — not the share of companies that do e-commerce (that's itav12). Each emner code is an independent rate; never sum them.
- emner parallels itav12 but reports revenue shares: 7810 (e-salgs andel af omsætning i alt), broken down by geography and channel in sub-codes.
- virkstrrda 1010 is the total; 1110–1140 are size breakdowns. Don't sum them.
- brancherev2 break: ITALMN covers ≤2020, ITALMN2 covers 2021+. Use WHERE brancherev2 IN ('ITALMN', 'ITALMN2') for time series.
- Starts from 2013. Use alongside itav12 when the question is both "how many companies e-sell?" and "how large a share of revenue is e-commerce?".
