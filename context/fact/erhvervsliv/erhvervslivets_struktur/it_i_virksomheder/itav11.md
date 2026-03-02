table: fact.itav11
description: Virksomhedernes e-handel (5-9 ansatte) efter branche (DB07), emner og tid
measure: indhold (unit Pct.)
columns:
- brancherev2: values [ITATOT=Alle virksomhedsbrancher (private, ikke-finansielle byerhverv), ITAC=10-39 Industri mv., ITAF=41-43 Bygge og anlæg, ITAGHI=45-56 Handel og transport mv., ITAJ=58-63 Information og kommunikation, ITALMN2=68-75, 77-82, 95.1 Erhvervsservice (2021-), ITALMN=68-74, 77-82, 95.1 Erhvervsservice (-2020)]
- emner: values [7403=1. E-salg i alt fra hjemmesider, apps, digitale markedsplatforme og EDI, 7410=1.1 E-salg fra hjemmeside, apps eller EDI, 7420=2.1 E-salg fra hjemmeside eller apps, 7425=2.2 E-salg via digitale platforme, 7430=2.3 E-salg via EDI (Electronic Data Interchange) ... 7526=5.2 E-salg til udlandet via digitale platforme, 7530=6. EDI salg til Danmark, 7540=7. EDI salg til udlandet (andre EU-lande eller resten af verden), 7550=7.1 EDI-salg til andre EU-lande, 7560=7.2 EDI-salg til resten af verden]
- tid: date range 2019-01-01 to 2024-01-01
notes:
- Covers 5–9 employee companies only — no virkstrrda column; all data is for this single size band.
- All values are percentages — never sum across emner; each code is an independent e-commerce survey question.
- emner is hierarchical: 7410 (e-salg fra hjemmeside, apps eller EDI) contains 7420 (web) and 7430 (EDI) as sub-types. 7403 (e-salg i alt) is the broadest parent. Pick parent OR children.
- brancherev2 break: ITALMN covers ≤2020, ITALMN2 covers 2021+. Use WHERE brancherev2 IN ('ITALMN', 'ITALMN2') for time series.
- Small date range: 2019–2024. For longer e-commerce series use itav12 (10+ employees, from 2008).
