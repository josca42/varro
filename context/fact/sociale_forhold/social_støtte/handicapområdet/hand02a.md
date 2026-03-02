table: fact.hand02a
description: Modtagere af handicapydelser efter ydelsestype, alder, køn og tid
measure: indhold (unit Antal)
columns:
- ydelsestype: values [30011=Aktivitets- og samværstilbud (§ 104 i lov om social service), 30013=Behandling (§ 102 i lov om social service), 30014=Beskyttet beskæftigelse (§ 103 i lov om social service), 30117=Kontant tilskud efter § 95 til ansættelse af hjælpere (§§ 83, 84) (§ 95 i lov om social service), 30181=Længerevarende botilbud inkl. tilknyttede ydelser fx §§ 83, 85 (§ 108 i lov om social service) ... 31213=Hjælp, omsorg eller støtte til personer i hjemløshed eller i risiko for hjemløshed, ACT og M-ACT-støttemetode (§ 85 a i Serviceloven) (2024K1-), 32001=Hjælp og støtte ved hastigt fremskridende sygdom, jf. § 83 i lov om social service (§ 117 a i Serviceloven) (2024K3-), 32002=Hjælp og støtte ved hastigt fremskridende sygdom, jf. § 97 i lov om social service (§ 117 a i Serviceloven) (2024K3-), 32003=Hjælp og støtte ved hastigt fremskridende sygdom, jf. § 112 i lov om social service (§ 117 a i Serviceloven) (2024K3-), 32004=Hjælp og støtte ved hastigt fremskridende sygdom, jf. § 116 i lov om social service (§ 117 a i Serviceloven) (2024K3-)]
- alder: values [9919=0-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8099=80 år og derover, 9999=Uoplyst alder]
- kon: values [1=Mænd, 2=Kvinder, 9=Uoplyst køn]
- tid: date range 2018-01-01 to 2024-10-01
notes:
- No dim table joins. No total/aggregate rows in any column — alder has 9 age bands (9919=0-19 through 8099=80+) plus 9999=uoplyst, kon has 1=Mænd, 2=Kvinder, 9=Uoplyst. Safe to SUM across alder and kon (exclude uoplyst codes if you want clean totals).
- ydelsestype has 21 types with no total row. Use ColumnValues("hand02a", "ydelsestype") for labels.
- National only — no regional breakdown. For recipients by region use hand07.
