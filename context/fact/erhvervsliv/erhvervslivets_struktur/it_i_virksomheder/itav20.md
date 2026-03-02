table: fact.itav20
description: Virksomhedernes brug af satellitter og Internet of Things (10+ ansatte)  efter anvendelse, branche (DB07), virksomhedsstørrelse og tid
measure: indhold (unit Pct.)
columns:
- anvend: values [8155=1. Benyttede satellitbaserede tjenester, 8160=1.1 Brug af satellitbaserede tjenester havde en positiv indvirkning på virksomheden, 8215=2. Anvender smarte enheder eller systemer til overvågning eller fjernstyring via internettet (IOT), 8220=2.1 Anvender smarte enheder eller systemer til styring af energiforbrug, 8225=2.2 Anvender smarte enheder eller systemer, RFID tags eller IP kameraer til forbedring af kundeservice, 8230=2.3 Anvender  smarte enheder eller systemer til overvågning af køretøjers kørsel eller vedligeholdelsesbehov, 8235=2.4 Anvender smarte enheder, systemer, sensorer eller RFID-tags til at overvåge vareproduktion, styre logistik eller spore varerne i produktionsprocessen, 8240=2.5 Anvender andre smarte enheder eller systemer der kan overvåges eller fjernstyres via internettet, 8245=2.6 Anvender smarte enheder eller systemer til sikring af virksomhedens bygninger, 8250=2.7 Anvender smarte enheder eller systemer til styring af virksomhedens logistik]
- brancherev2: values [ITATOT=Alle virksomhedsbrancher (private, ikke-finansielle byerhverv), ITAC=10-39 Industri mv., ITAF=41-43 Bygge og anlæg, ITAGHI=45-56 Handel og transport mv., ITAJ=58-63 Information og kommunikation, ITALMN2=68-75, 77-82, 95.1 Erhvervsservice (2021-), ITALMN=68-74, 77-82, 95.1 Erhvervsservice (-2020)]
- virkstrrda: values [1010=Alle virksomheder (mindst 10 ansatte), 1110=10-49 ansatte, 1120=50-99 ansatte, 1130=100-249 ansatte, 1140=250 ansatte og derover]
- tid: date range 2017-01-01 to 2024-01-01
notes:
- All values are percentages — each anvend code is an independent satellite/IoT question; never sum them.
- anvend has two groups: satellites (8155–8160) and IoT (8215–8250). 8215 (IoT i alt) contains 8220–8250 (specific IoT use cases). Pick parent OR children.
- virkstrrda 1010 is the total; 1110–1140 are size breakdowns. Don't sum them.
- brancherev2 break: ITALMN covers ≤2020, ITALMN2 covers 2021+. Use WHERE brancherev2 IN ('ITALMN', 'ITALMN2') for time series.
- Ends at 2024 (not updated to 2025 unlike most other tables). Niche topic — use when specifically asked about IoT or satellite technology adoption.
