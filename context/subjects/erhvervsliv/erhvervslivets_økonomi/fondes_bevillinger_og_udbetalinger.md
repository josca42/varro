<fact tables>
<table>
id: fond00
description: Bevilligede fondsmidler efter fondstype, bevillingsniveau, nøgletal og tid
columns: fondstype, bevilling2, aktp, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2023-01-01
</table>
<table>
id: fond01
description: Bevilligede fondsmidler efter fondstype, nøgletal, formål og tid
columns: fondstype, aktp, formal, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2023-01-01
</table>
<table>
id: fond02
description: Bevilligede fondsmidler efter fondstype, virkemidler, formål og tid
columns: fondstype, virke, formal, tid (time), indhold (unit Mio. kr.)
tid range: 2016-01-01 to 2023-01-01
</table>
<table>
id: fond03
description: Bevilligede fondsmidler efter fondstype, modtagertype, formål og tid
columns: fondstype, modtag, formal, tid (time), indhold (unit Mio. kr.)
tid range: 2016-01-01 to 2023-01-01
</table>
<table>
id: fond04
description: Bevilligede fondsmidler efter fondstype, modtagernationalitet, formål og tid
columns: fondstype, modtager, formal, tid (time), indhold (unit Mio. kr.)
tid range: 2016-01-01 to 2023-01-01
</table>
<table>
id: fond06
description: Bevilligede fondsmidler til kulturelle formål efter fondstype, hovedområder og tid
columns: fondstype, homr, tid (time), indhold (unit Mio. kr.)
tid range: 2016-01-01 to 2023-01-01
</table>
<table>
id: fond12
description: Bevilligede fondsmidler til sociale formål efter fondstype, målgruppe, hovedområder og tid
columns: fondstype, mlgrp, homr, tid (time), indhold (unit Mio. kr.)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: fond14
description: Bevilligede fondsmidler til sundhedsformål efter fondstype, hovedområder og tid
columns: fondstype, homr, tid (time), indhold (unit Mio. kr.)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: fond15
description: Bevilligede fondsmidler til uddannelses- og folkeoplysningsformål efter fondstype, hovedområder og tid
columns: fondstype, homr, tid (time), indhold (unit Mio. kr.)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: fond16
description: Bevilligede fondsmidler til erhvervsfremme- og regionaludviklingsformål efter fondstype, hovedområder og tid
columns: fondstype, homr, tid (time), indhold (unit Mio. kr.)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: fond17
description: Bevilligede fondsmidler til almennyttige- og ikke-almennyttige formål efter fondstype, nøgletal, formål og tid
columns: fondstype, aktp, formal, tid (time), indhold (unit Mio. kr.)
tid range: 2021-01-01 to 2023-01-01
</table>
<table>
id: fond19
description: Bevilligede fondsmidler til natur-, klima- og miljøformål efter fondstype, hovedområder og tid
columns: fondstype, homr, tid (time), indhold (unit Mio. kr.)
tid range: 2022-01-01 to 2023-01-01
</table>
<table>
id: fond20
description: Bevilligede fondsmidler til forskning efter fondstype, fagområde, fondsmidler og tid
columns: fondstype, fagomr, fondsmidler, tid (time), indhold (unit Mio. kr.)
tid range: 2022-01-01 to 2023-01-01
</table>
<table>
id: fond21
description: Bevilligede fondsmidler til grøn forskning efter fondstype, underområde og tid
columns: fondstype, underomrade, tid (time), indhold (unit Mio. kr.)
tid range: 2022-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- Universal gotcha: fondstype=1000 (Alle fonde) is always the aggregate total of 1005+1010. Never sum all three fondstype values — it doubles the total.
- The `homr` column appears in many tables (fond06/12/14/15/16/19) but the code values are completely different in each table — they are table-specific, not a shared dimension.

Table selection guide:
- Cross-formål overview (antal, bevilget, udbetalt): fond01 — the only table covering all 11 formål with 3 metrics, back to 2016.
- Grant size brackets (50M+, 10-50M, under 10M, 0 kr.): fond00 — unique to this table.
- How grants are used (anlæg, forskning, innovation, formidling, etc.): fond02 — breakdown by virkemidler × formål.
- Who receives the grants (public, individuals, firms, non-profits): fond03 — by modtagertype × formål.
- Domestic vs. international recipients: fond04 — by modtagernationalitet × formål.
- Almennyttig vs. ikke-almennyttig split: fond17 — unique, but only from 2021.
- Cultural sub-areas (23 categories): fond06, back to 2016.
- Social grants by target group + area: fond12, from 2019, sparse cross of mlgrp × homr.
- Health grants with sub-category hierarchy: fond14 — caution: homr has two levels (uppercase=parent, lowercase=child); use only 3010+3015+3020 for top-level totals.
- Education sub-areas: fond15, from 2019.
- Business promotion + regional development: fond16, from 2019 (only 3 homr codes).
- Nature/climate/environment sub-areas: fond19, only 2022-2023.
- Research by academic field: fond20, only 2022-2023. fondsmidler=4005 is a subset of 4000 — never sum them.
- Green research sub-areas: fond21, only 2022-2023.

Time coverage pattern: fond00/01/02/03/04/06 cover 2016-2023 (8 years). Topic-specific tables (fond12/14/15/16) cover 2019-2023. Newest tables (fond17/19/20/21) cover only 2021-2023 or 2022-2023. Use fond01 when you need a longer series or cross-formål comparison regardless of sub-area detail.