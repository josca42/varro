<fact tables>
<table>
id: itav3
description: Virksomhedernes adgang til it-kompetencer (10+ ansatte) efter virksomhedsstørrelse, branche (DB07), emner og tid
columns: virkstrrda, brancherev2, emner, tid (time), indhold (unit Pct.)
tid range: 2014-01-01 to 2024-01-01
</table>
<table>
id: itav4
description: Virksomhedernes brug af hjemmesider og sociale medier (10+ ansatte) efter virksomhedsstørrelse, branche (DB07), emner og tid
columns: virkstrrda, brancherev2, emner, tid (time), indhold (unit Pct.)
tid range: 2004-01-01 to 2025-01-01
</table>
<table>
id: itav9
description: Virksomhedernes adgang til internettet (10+ ansatte) efter virksomhedsstørrelse, branche (DB07), emner og tid
columns: virkstrrda, brancherev2, emner, tid (time), indhold (unit Pct.)
tid range: 2004-01-01 to 2025-01-01
</table>
<table>
id: itav13
description: Virksomhedernes andel af omsætning og køb fra e-handel (10+ ansatte) efter virksomhedsstørrelse, branche (DB07), emner og tid
columns: virkstrrda, brancherev2, emner, tid (time), indhold (unit Pct.)
tid range: 2013-01-01 to 2025-01-01
</table>
<table>
id: itav12
description: Andel af virksomheder med e-handel (10+ ansatte) efter virksomhedsstørrelse, branche (DB07), emner og tid
columns: virkstrrda, brancherev2, emner, tid (time), indhold (unit Pct.)
tid range: 2008-01-01 to 2025-01-01
</table>
<table>
id: itav15
description: It-sikkerhed og it-sikkerhedshændelser i virksomheder (10+ ansatte) efter virksomhedsstørrelse, branche (DB07), emner og tid
columns: virkstrrda, brancherev2, emner, tid (time), indhold (unit Pct.)
tid range: 2016-01-01 to 2025-01-01
</table>
<table>
id: itav17
description: Virksomhedernes brug af 3D print (10+ ansatte)  efter anvendelse, branche (DB07), virksomhedsstørrelse og tid
columns: anvend, brancherev2, virkstrrda, tid (time), indhold (unit Pct.)
tid range: 2018-01-01 to 2025-01-01
</table>
<table>
id: itav16
description: Virksomhedernes brug af cloud computing (10+ ansatte)  efter anvendelse, branche (DB07), virksomhedsstørrelse og tid
columns: anvend, brancherev2, virkstrrda, tid (time), indhold (unit Pct.)
tid range: 2011-01-01 to 2025-01-01
</table>
<table>
id: itav19
description: Virksomhedernes brug af robotteknologi og kunstig intelligens (10+ ansatte)  efter anvendelse, branche (DB07), virksomhedsstørrelse og tid
columns: anvend, brancherev2, virkstrrda, tid (time), indhold (unit Pct.)
tid range: 2017-01-01 to 2025-01-01
</table>
<table>
id: itav20
description: Virksomhedernes brug af satellitter og Internet of Things (10+ ansatte)  efter anvendelse, branche (DB07), virksomhedsstørrelse og tid
columns: anvend, brancherev2, virkstrrda, tid (time), indhold (unit Pct.)
tid range: 2017-01-01 to 2024-01-01
</table>
<table>
id: itav21
description: Virksomhedernes brug af informationsdeling og fakturering (10+ ansatte) efter aktivitet, branche (DB07), virksomhedsstørrelse og tid
columns: aktivi, brancherev2, virkstrrda, tid (time), indhold (unit Pct.)
tid range: 2008-01-01 to 2025-01-01
</table>
<table>
id: itav10
description: It-anvendelse i virksomheder (5-9 ansatte) efter branche (DB07), emner og tid
columns: brancherev2, emner, tid (time), indhold (unit Pct.)
tid range: 2019-01-01 to 2024-01-01
</table>
<table>
id: itav11
description: Virksomhedernes e-handel (5-9 ansatte) efter branche (DB07), emner og tid
columns: brancherev2, emner, tid (time), indhold (unit Pct.)
tid range: 2019-01-01 to 2024-01-01
</table>
</fact tables>
notes:
- All 13 tables measure percentages (Pct.) of companies — values are survey proportions, never sumable across emner/anvend/aktivi rows.
- All tables share the same brancherev2 structural break: ITALMN = Erhvervsservice ≤2020, ITALMN2 = Erhvervsservice 2021+. For any time series that spans 2020–2021, filter with WHERE brancherev2 IN ('ITALMN', 'ITALMN2') rather than a single code.
- All 10+ employee tables have virkstrrda: 1010 = total (alle virksomheder), 1110–1140 = size bands. Never sum size bands together or with the total.
- The 5-9 employee tables (itav10, itav11) have no virkstrrda — all rows are for the 5-9 ansatte cohort only.

Choosing a table by topic:
- Internet access and connection speeds → itav9 (from 2004, longest series)
- Websites and social media → itav4 (from 2004, longest series)
- E-commerce — share of companies → itav12 (from 2008, 10+ employees) or itav11 (2019–2024, 5–9 employees)
- E-commerce — share of turnover/purchases → itav13 (from 2013, 10+ employees)
- IT competencies, specialists, outsourcing → itav3 (from 2014)
- IT security measures and incidents → itav15 (from 2016)
- Cloud computing adoption and services → itav16 (from 2011)
- Robots and AI (machine learning, generative AI, etc.) → itav19 (from 2017)
- 3D printing → itav17 (from 2018, niche topic)
- Satellites and IoT → itav20 (2017–2024, not updated to 2025)
- ERP, CRM, BI, SCM, e-invoicing → itav21 (from 2008)
- Broad IT survey for 5-9 employee companies → itav10 (2019–2024, covers internet/cloud/security/AI)

Overlapping coverage:
- itav12 (share of companies e-selling) and itav13 (e-commerce share of turnover) are complementary — use together when the question has both angles.
- itav10 partially overlaps with itav9, itav15, itav16, itav19 but is the only source for 5-9 employee companies and has a narrower date range.
