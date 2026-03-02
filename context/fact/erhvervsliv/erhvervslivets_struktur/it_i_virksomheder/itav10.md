table: fact.itav10
description: It-anvendelse i virksomheder (5-9 ansatte) efter branche (DB07), emner og tid
measure: indhold (unit Pct.)
columns:
- brancherev2: values [ITATOT=Alle virksomhedsbrancher (private, ikke-finansielle byerhverv), ITAC=10-39 Industri mv., ITAF=41-43 Bygge og anlæg, ITAGHI=45-56 Handel og transport mv., ITAJ=58-63 Information og kommunikation, ITALMN2=68-75, 77-82, 95.1 Erhvervsservice (2021-), ITALMN=68-74, 77-82, 95.1 Erhvervsservice (-2020)]
- emner: values [6910=1. Internetadgang til arbejdsbrug, 6920=1.1 Alle ansatte anvender computer med internetadgang, 6930=1.2 Mindst 75 pct. af de ansatte anvender computer med internetadgang, 6940=1.3 Mindst 50 pct. af de ansatte anvender computer med internetadgang, 6950=2.1 Hurtigste faste internetforbindelse er over 30 Mbit/s ... 7280=8. Beskæftiger it-specialister, 7290=9. Havde brud på IT-sikkerheden i foregående kalenderår, 7310=9.1 Har oplevet blokkeret adgang til it-services i foregående kalenderår, 7320=9.2 Har oplevet sletning eller ødelæggelse af data i foregående kalenderår, 7330=9.3 Har oplevet videregivelse af fortrolige data (forsætligt eller utilsigtet) i foregående kalenderår]
- tid: date range 2019-01-01 to 2024-01-01
notes:
- Covers 5–9 employee companies only — no virkstrrda column; all data is for this single size band.
- All values are percentages — never sum across emner; each code is an independent survey question.
- emner spans a wide range of topics: internet access, websites, cloud, AI/robots, security incidents, IT specialists — essentially a broad IT survey in a single table. Use ColumnValues("itav10", "emner") to browse all 41 codes.
- emner is hierarchical in places: 6910 (internetadgang i alt) contains 6920–6940; security codes 7290 (brud på IT-sikkerheden) contains 7310–7330. Pick parent OR children.
- brancherev2 break: ITALMN covers ≤2020, ITALMN2 covers 2021+. Use WHERE brancherev2 IN ('ITALMN', 'ITALMN2') for time series.
- Small date range: 2019–2024 only. For longer series on the same topics use the 10+ employee tables (itav9, itav15, itav16, itav19).
