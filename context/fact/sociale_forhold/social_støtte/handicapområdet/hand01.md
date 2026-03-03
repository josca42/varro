table: fact.hand01
description: Handicapydelser efter område, ydelsestype og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- ydelsestype: values [30011=Aktivitets- og samværstilbud (§ 104 i lov om social service), 30013=Behandling (§ 102 i lov om social service), 30014=Beskyttet beskæftigelse (§ 103 i lov om social service), 30117=Kontant tilskud efter § 95 til ansættelse af hjælpere (§§ 83, 84) (§ 95 i lov om social service), 30181=Længerevarende botilbud inkl. tilknyttede ydelser fx §§ 83, 85 (§ 108 i lov om social service) ... 31213=Hjælp, omsorg eller støtte til personer i hjemløshed eller i risiko for hjemløshed, ACT og M-ACT-støttemetode (§ 85 a i Serviceloven) (2024K1-), 32001=Hjælp og støtte ved hastigt fremskridende sygdom, jf. § 83 i lov om social service (§ 117 a i Serviceloven) (2024K3-), 32002=Hjælp og støtte ved hastigt fremskridende sygdom, jf. § 97 i lov om social service (§ 117 a i Serviceloven) (2024K3-), 32003=Hjælp og støtte ved hastigt fremskridende sygdom, jf. § 112 i lov om social service (§ 117 a i Serviceloven) (2024K3-), 32004=Hjælp og støtte ved hastigt fremskridende sygdom, jf. § 116 i lov om social service (§ 117 a i Serviceloven) (2024K3-)]
- tid: date range 2015-01-01 to 2024-10-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau=3 only (97 kommuner). No national total row — omrade=0 does not exist here. To get a national figure, SUM across all kommuner.
- indhold values are decimal (e.g. 867.6) because DST reports quarterly averages of daily service counts. This measures services delivered, not unique recipients. For headcounts use hand07 instead.
- ydelsestype has 21 inline service types with no aggregate/total row. Summing all 21 gives total services across all types. Use ColumnValues("hand01", "ydelsestype") to see the full list with labels.
- hand05 covers the same dimensions but ends 2024-01-01 and only has 17 ydelsestype (missing 32001–32004: "hastigt fremskridende sygdom" types added 2024K3). hand01 supersedes hand05.
- Map: /geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
