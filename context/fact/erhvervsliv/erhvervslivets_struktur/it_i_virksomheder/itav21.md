table: fact.itav21
description: Virksomhedernes brug af informationsdeling og fakturering (10+ ansatte) efter aktivitet, branche (DB07), virksomhedsstørrelse og tid
measure: indhold (unit Pct.)
columns:
- aktivi: values [4310=1. Anvender ERP-software til at dele information internt i virksomheden (fx køb, salg, produktion), 4410=2. Anvender CRM-software til behandling af kundeinformation, 4420=2.1 Anvender CRM-software til at opfange og dele kundeinformationer med andre interne funktioner., 4430=2.2 Anvender CRM software til kunde-analyse til markedsføring, 4510=3. Anvender Business Intelligence software, 4810=4. Deler SCM information (supply chain management) med andre virksomheder eller kunder, 4820=4.1 Deler SCM information via hjemmesider, 4830=4.2 Deler SCM information via automatiseret dataudveksling (fx EDIFACT), 4835=5. Sendt fakturaer i et elektronisk format, der kan databehandles automatisk., 4840=6. Modtaget fakturaer i et elektronisk format, der kan databehandles automatisk.]
- brancherev2: values [ITATOT=Alle virksomhedsbrancher (private, ikke-finansielle byerhverv), ITAC=10-39 Industri mv., ITAF=41-43 Bygge og anlæg, ITAGHI=45-56 Handel og transport mv., ITAJ=58-63 Information og kommunikation, ITALMN2=68-75, 77-82, 95.1 Erhvervsservice (2021-), ITALMN=68-74, 77-82, 95.1 Erhvervsservice (-2020)]
- virkstrrda: values [1010=Alle virksomheder (mindst 10 ansatte), 1110=10-49 ansatte, 1120=50-99 ansatte, 1130=100-249 ansatte, 1140=250 ansatte og derover]
- tid: date range 2008-01-01 to 2025-01-01
notes:
- All values are percentages — each aktivi code is an independent question about software or information-sharing practices; never sum them.
- aktivi codes cover distinct systems: ERP (4310), CRM (4410–4430), Business Intelligence (4510), SCM sharing (4810–4830), and e-invoicing (4835, 4840). The CRM codes are hierarchical: 4410 (CRM i alt) contains 4420 and 4430.
- virkstrrda 1010 is the total; 1110–1140 are size breakdowns. Don't sum them.
- brancherev2 break: ITALMN covers ≤2020, ITALMN2 covers 2021+. Use WHERE brancherev2 IN ('ITALMN', 'ITALMN2') for time series from 2008.
- Good for questions about ERP/CRM/BI adoption and e-invoicing compliance. Longest series from 2008.
