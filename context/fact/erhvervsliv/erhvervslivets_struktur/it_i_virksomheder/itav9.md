table: fact.itav9
description: Virksomhedernes adgang til internettet (10+ ansatte) efter virksomhedsstørrelse, branche (DB07), emner og tid
measure: indhold (unit Pct.)
columns:
- virkstrrda: values [1010=Alle virksomheder (mindst 10 ansatte), 1110=10-49 ansatte, 1120=50-99 ansatte, 1130=100-249 ansatte, 1140=250 ansatte og derover]
- brancherev2: values [ITATOT=Alle virksomhedsbrancher (private, ikke-finansielle byerhverv), ITAC=10-39 Industri mv., ITAF=41-43 Bygge og anlæg, ITAGHI=45-56 Handel og transport mv., ITAJ=58-63 Information og kommunikation, ITALMN2=68-75, 77-82, 95.1 Erhvervsservice (2021-), ITALMN=68-74, 77-82, 95.1 Erhvervsservice (-2020)]
- emner: values [6610=1. Internetadgang til arbejdsbrug, 6620=1.1 Alle ansatte anvender computer med internetadgang, 6630=1.2 Mindst 75 pct. af de ansatte anvender computer med internetadgang, 6640=1.3 Mindst 50 pct. af de ansatte anvender computer med internetadgang, 6650=2.1 Hurtigste faste internetforbindelse er over 30 Mbit/s, 6660=2.2 Hurtigste faste internetforbindelse er over 100 Mbit/s, 6670=2.3 Hurtigste faste internetforbindelse er over 500 Mbit/s, 6680=2.4 Hurtigste faste internetforbindelse er over 1 Gbit/s, 6690=3.1 Tilstrækkelig hastighed på fast internetforbindelse, 6710=3.2 Ikke tilstrækkelig hastighed på fast internetforbindelse, 6780=4. Mobil bredbåndsforbindelse, 6790=5. Alle ansatte har bærbart udstyr til mobil internetadgang, 6810=5.1 Mindst 75 pct. af de ansatte har bærbart udstyr til mobil internetadgang, 6820=5.2 Mindst 50 pct. af de ansatte har bærbart udstyr til mobil internetadgang]
- tid: date range 2004-01-01 to 2025-01-01
notes:
- All values are percentages — never sum across emner; each code is an independent survey question about internet access or connection speed.
- emner is hierarchical: 6610 (internetadgang i alt) contains 6620–6640 (employee coverage brackets). Speed thresholds 6650–6680 are nested ("over 100 Mbit/s" ⊂ "over 30 Mbit/s") — pick the single threshold you want, don't sum.
- virkstrrda 1010 is the total; 1110–1140 are size breakdowns. Don't sum them.
- brancherev2 break: ITALMN covers ≤2020, ITALMN2 covers 2021+. Use WHERE brancherev2 IN ('ITALMN', 'ITALMN2') for a time series spanning the break.
- Longest time series (from 2004) alongside itav4 — useful for long-run internet penetration trends.
