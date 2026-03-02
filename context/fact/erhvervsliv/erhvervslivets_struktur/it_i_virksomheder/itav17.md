table: fact.itav17
description: Virksomhedernes brug af 3D print (10+ ansatte)  efter anvendelse, branche (DB07), virksomhedsstørrelse og tid
measure: indhold (unit Pct.)
columns:
- anvend: values [8130=1. Anvendte 3D printning i foregående kalenderår, 8135=1.1 Anvendte 3D print til at fremstille prototyper eller 3D-modeller til salg, 8140=1.2 Anvendte 3D print til at fremstille andre 3D-produkter til salg, 8145=1.3 Anvendte 3D print til at fremstille prototyper eller 3D-modeller til virksomhedens eget brug, 8150=1.4 Anvendte 3D print til at fremstille andre 3D-produkter til virksomhedens eget brug]
- brancherev2: values [ITATOT=Alle virksomhedsbrancher (private, ikke-finansielle byerhverv), ITAC=10-39 Industri mv., ITAF=41-43 Bygge og anlæg, ITAGHI=45-56 Handel og transport mv., ITAJ=58-63 Information og kommunikation, ITALMN2=68-75, 77-82, 95.1 Erhvervsservice (2021-), ITALMN=68-74, 77-82, 95.1 Erhvervsservice (-2020)]
- virkstrrda: values [1010=Alle virksomheder (mindst 10 ansatte), 1110=10-49 ansatte, 1120=50-99 ansatte, 1130=100-249 ansatte, 1140=250 ansatte og derover]
- tid: date range 2018-01-01 to 2025-01-01
notes:
- All values are percentages — each anvend code is an independent 3D printing usage question; never sum them.
- anvend is hierarchical: 8130 (anvendte 3D print i alt) is the parent; 8135–8150 are specific use cases (prototypes for sale, products for sale, prototypes for own use, products for own use). Pick parent OR children.
- virkstrrda 1010 is the total; 1110–1140 are size breakdowns. Don't sum them.
- brancherev2 break: ITALMN covers ≤2020, ITALMN2 covers 2021+. Use WHERE brancherev2 IN ('ITALMN', 'ITALMN2') for time series.
- Small topic scope (5 codes, from 2018). Mainly useful for "what share of companies use 3D printing and for what purpose?".
