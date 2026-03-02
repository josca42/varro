table: fact.hand05
description: Handicapydelser efter område, ydelsestype og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- ydelsestype: values [30011=Aktivitets- og samværstilbud (§ 104 i lov om social service), 30013=Behandling (§ 102 i lov om social service), 30014=Beskyttet beskæftigelse (§ 103 i lov om social service), 30117=Kontant tilskud efter § 95 til ansættelse af hjælpere (§§ 83, 84) (§ 95 i lov om social service), 30181=Længerevarende botilbud inkl. tilknyttede ydelser fx §§ 83, 85 (§ 108 i lov om social service), 30182=Midlertidige botilbud inkl. tilknyttede ydelser fx §§ 83, 85 (§ 107 i lov om social service), 31132=Borgerstyret personlig assistance - BPA (§ 96 i lov om social service), 31133=Kontaktperson for døvblinde (§ 98 i lov om social service), 31134=Ledsageordning (§ 97 i lov om social service), 31181=Gruppebaseret socialpædagogisk hjælp og støtte (§ 82 a i lov om social service) (2020K3-), 31182=Individuel tidsbegrænset socialpædagogisk hjælp og støtte (§ 82 b i lov om social service) (2020K3-), 31183=Socialt akuttilbud (§ 82 c i Serviceloven) (2024K1-), 31201=Socialpædagogisk støtte i botilbudslignende tilbud, fx botilbud efter ABL § 105/115 (§ 85 i lov om social service), 31202=Øvrig socialpædagogisk støtte, fx borgernes private hjem (§ 85 i lov om social service), 31211=Hjælp, omsorg eller støtte til personer i hjemløshed eller i risiko for hjemløshed, CTI støttemetode (§ 85 a i Serviceloven) (2024K1-), 31212=Hjælp, omsorg eller støtte til personer i hjemløshed eller i risiko for hjemløshed, ICM støttemetode (§ 85 a i Serviceloven) (2024K1-), 31213=Hjælp, omsorg eller støtte til personer i hjemløshed eller i risiko for hjemløshed, ACT og M-ACT-støttemetode (§ 85 a i Serviceloven) (2024K1-)]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Largely superseded by hand01. hand05 ends 2024-01-01 and covers only 17 ydelsestype — the 4 "hastigt fremskridende sygdom" types (32001–32004, added 2024K3) are absent. Use hand01 for current or complete data.
- omrade joins dim.nuts at niveau=3 (97 kommuner), no national total (no omrade=0).
- Same decimal-value semantics as hand01: quarterly service averages, not headcounts.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
