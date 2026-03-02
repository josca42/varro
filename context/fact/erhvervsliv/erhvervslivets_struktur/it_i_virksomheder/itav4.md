table: fact.itav4
description: Virksomhedernes brug af hjemmesider og sociale medier (10+ ansatte) efter virksomhedsstørrelse, branche (DB07), emner og tid
measure: indhold (unit Pct.)
columns:
- virkstrrda: values [1010=Alle virksomheder (mindst 10 ansatte), 1110=10-49 ansatte, 1120=50-99 ansatte, 1130=100-249 ansatte, 1140=250 ansatte og derover]
- brancherev2: values [ITATOT=Alle virksomhedsbrancher (private, ikke-finansielle byerhverv), ITAC=10-39 Industri mv., ITAF=41-43 Bygge og anlæg, ITAGHI=45-56 Handel og transport mv., ITAJ=58-63 Information og kommunikation, ITALMN2=68-75, 77-82, 95.1 Erhvervsservice (2021-), ITALMN=68-74, 77-82, 95.1 Erhvervsservice (-2020)]
- emner: values [3710=1. Egen hjemmeside, 3810=2.1 Hjemmesiden har produktbeskrivelser, prislister mv., 3820=2.2 Hjemmesiden har online køb, bestilling eller reservering, 3830=2.3 Brugere af hjemmesiden kan tilpasse eller designe produkter, 3840=2.4 Brugere af hjemmesiden kan følge ordrer ... 4230=5.3 Anvender sociale medier til inddragelse af kunder i udvikling af produkter, 4240=5.4 Anvender sociale medier til samarbejde med forretningsforbindelser, organisationer eller myndigheder, 4250=5.5 Anvender sociale medier til rekruttering, 4260=5.6 Anvender sociale medier til vidensdeling internt i virksomheden, 4280=6. Betaler for annoncering på internettet (søgemaskiner, sociale medier eller andre hjemmesider)]
- tid: date range 2004-01-01 to 2025-01-01
notes:
- All values are percentages — never sum across emner; each code is an independent survey question (website feature or social media usage type).
- emner is hierarchical: e.g. 3710 (egen hjemmeside) is a parent with 3810–3840 as sub-features; social media usage codes 4210–4280 are also independent. Pick parent OR children, not both.
- virkstrrda 1010 is the total; 1110–1140 are size breakdowns. Don't sum them.
- brancherev2 break: ITALMN covers ≤2020, ITALMN2 covers 2021+. For a time series use WHERE brancherev2 IN ('ITALMN', 'ITALMN2') and don't GROUP BY brancherev2 across the break.
- Longest time series in this subject group — goes back to 2004. Useful for long-run trends on website and social media adoption.
