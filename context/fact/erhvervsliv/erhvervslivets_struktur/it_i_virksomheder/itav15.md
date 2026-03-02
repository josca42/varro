table: fact.itav15
description: It-sikkerhed og it-sikkerhedshændelser i virksomheder (10+ ansatte) efter virksomhedsstørrelse, branche (DB07), emner og tid
measure: indhold (unit Pct.)
columns:
- virkstrrda: values [1010=Alle virksomheder (mindst 10 ansatte), 1110=10-49 ansatte, 1120=50-99 ansatte, 1130=100-249 ansatte, 1140=250 ansatte og derover]
- brancherev2: values [ITATOT=Alle virksomhedsbrancher (private, ikke-finansielle byerhverv), ITAC=10-39 Industri mv., ITAF=41-43 Bygge og anlæg, ITAGHI=45-56 Handel og transport mv., ITAJ=58-63 Information og kommunikation, ITALMN2=68-75, 77-82, 95.1 Erhvervsservice (2021-), ITALMN=68-74, 77-82, 95.1 Erhvervsservice (-2020)]
- emner: values [8350=1. Implementeret én eller flere typer it-sikkerhedsmæssige foranstaltninger, 8355=1.1 Har stærke adgangskoder til autentificering, 8360=1.2 Har systematisk opdatering af software (inkl. styresystemer), 8365=1.3 Har biometriske metoder til brugeridentifikation og autentifikation, 8370=1.4 Foretager kryptering af data, filer eller e-mails ... 8455=5.1 Har dokumentation om styring af it-adgangsrettigheder, 8460=5.2 Har dokumentation om lagring, beskyttelse, adgang til data, 8465=5.3 Har dokumentation om procedurer ved it-sikkerhedshændelser, 8470=5.4 Har dokumentation om de ansattes ansvar vedr. it-sikkerhedsmæssige forhold, 8475=5.5 Har dokumentation om træning af ansatte i it-sikkerhedsmæssige forhold]
- tid: date range 2016-01-01 to 2025-01-01
notes:
- All values are percentages — never sum across emner; each code is an independent IT security question.
- emner is hierarchical: 8350 (én eller flere foranstaltninger i alt) is the top-level parent for all security measures (8355–8400). 8425 (dokumentation i alt) contains 8455–8475. Pick parent OR children.
- virkstrrda 1010 is the total; 1110–1140 are size breakdowns. Don't sum them.
- brancherev2 break: ITALMN covers ≤2020, ITALMN2 covers 2021+. Use WHERE brancherev2 IN ('ITALMN', 'ITALMN2') for time series.
- Covers both proactive measures (policies, encryption, access control) and incidents (blocked access, data loss, data leak). Be precise about which emner you select — these are very different question types.
