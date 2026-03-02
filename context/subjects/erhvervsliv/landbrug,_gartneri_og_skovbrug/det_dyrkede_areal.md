<fact tables>
<table>
id: afg6
description: Afgrøder efter afgrøde, enhed, areal og tid
columns: afgrode, enhed, areal1, tid (time), indhold (unit -)
tid range: 1982-01-01 to 2024-01-01
</table>
<table>
id: afg207
description: Bedrifter og arealer med udvalgte afgrøder efter område, areal med afgrøden, enhed og tid
columns: omrade, arealafg, enhed, tid (time), indhold (unit -)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: afg3
description: Bedrifter og arealer med udvalgte afgrøder efter område, areal med afgrøden, enhed og tid
columns: omrade, arealafg, enhed, tid (time), indhold (unit -)
tid range: 1982-01-01 to 2024-01-01
</table>
<table>
id: afg4
description: Bedrifter med korn efter område(2), bedriftstype, areal og tid
columns: omr2, bedrift, areal1, tid (time), indhold (unit -)
tid range: 1982-01-01 to 2024-01-01
</table>
<table>
id: frugt4
description: Nettoareal  og trætæthed for æbler og pærer efter enhed, sort, træernes alder og tid
columns: maengde4, sort, tre, tid (time), indhold (unit -)
tid range: 2002-01-01 to 2023-01-01
</table>
<table>
id: vhus15
description: Kulturer i væksthuse efter enhed, kulturer og tid
columns: tal, kult, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2024-01-01
</table>
</fact tables>
notes:
- afg6 is the main comprehensive crop table: 61 crop codes (hierarchical with dot-notation), farm size classes, bedrifter or hektar, 1982–2024. No regional breakdown. Start here for national crop area questions.
- afg207 and afg3 both give bedrifter/hectares for specific crops by farm-size distribution, but at very coarse regional detail. afg207 (2006–2024) covers korn, hvede, raps, varig græs, and has the most regional granularity (regioner + selected landsdele). afg3 (1982–2024) covers rug, havre, kartofler, raps, frø with only 3 regions (Hele landet / Jylland / Øerne).
- afg4 (1982–2024) gives grain area breakdown by dominant crop type on each farm, split into 4 regions (Hele landet / Jylland / Fyn / Øst for Storebælt). Useful for farm-type composition.
- frugt4 (2002–2023) is specific to apples and pears: nettoareal and tree density by variety and tree age. No other fruit or regional breakdown.
- vhus15 (2015–2024) covers greenhouse cultures only: area (m²) or number of farms by crop type. Use for greenhouse vegetable, flower, and plant production.
- arealafg in afg207/afg3 encodes crop type and farm-size class together (10000–10505). Always use ColumnValues to find the right code — there's no separate crop column.
- All tables with enhed or tal have a measurement selector that doubles all rows. Always filter: enhed='HA'/'ANTAL', tal='KVM'/'ANTAL', or areal1=specific code in afg4.
- Map: afg207 supports choropleth at region (niveau 1) and landsdel (niveau 2) level via context/geo/regioner.parquet and context/geo/landsdele.parquet. afg3 and afg4 use non-standard regional codes (L3/L4/1580) with no geo file match.
