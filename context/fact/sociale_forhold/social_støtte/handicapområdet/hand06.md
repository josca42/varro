table: fact.hand06
description: Handicapydelser (Antal pr. 1.000 indbyggere) efter område, ydelsestype og tid
measure: indhold (unit Pr. 1.000 indb.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- ydelsestype: values [30011=Aktivitets- og samværstilbud (§ 104 i lov om social service), 30013=Behandling (§ 102 i lov om social service), 30014=Beskyttet beskæftigelse (§ 103 i lov om social service), 30117=Kontant tilskud efter § 95 til ansættelse af hjælpere (§§ 83, 84) (§ 95 i lov om social service), 30181=Længerevarende botilbud inkl. tilknyttede ydelser fx §§ 83, 85 (§ 108 i lov om social service) ... 31213=Hjælp, omsorg eller støtte til personer i hjemløshed eller i risiko for hjemløshed, ACT og M-ACT-støttemetode (§ 85 a i Serviceloven) (2024K1-), 32001=Hjælp og støtte ved hastigt fremskridende sygdom, jf. § 83 i lov om social service (§ 117 a i Serviceloven) (2024K3-), 32002=Hjælp og støtte ved hastigt fremskridende sygdom, jf. § 97 i lov om social service (§ 117 a i Serviceloven) (2024K3-), 32003=Hjælp og støtte ved hastigt fremskridende sygdom, jf. § 112 i lov om social service (§ 117 a i Serviceloven) (2024K3-), 32004=Hjælp og støtte ved hastigt fremskridende sygdom, jf. § 116 i lov om social service (§ 117 a i Serviceloven) (2024K3-)]
- tid: date range 2015-01-01 to 2024-10-01
dim docs: /dim/nuts.md
notes:
- indhold is a rate (pr. 1.000 indbyggere), not a count. Never SUM across kommuner — the rates are not additive across geographies.
- omrade joins dim.nuts at niveau=3 (97 kommuner), no national total row.
- Use this table when comparing municipalities. For absolute counts use hand01 (services) or hand07 (recipients).
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
