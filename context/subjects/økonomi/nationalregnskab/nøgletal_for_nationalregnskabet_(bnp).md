<fact tables>
<table>
id: nan1
description: Forsyningsbalance, bruttonationalprodukt (BNP),økonomisk vækst, beskæftigelse mv. efter transaktion, prisenhed og tid
columns: transakt, prisenhed, tid (time), indhold (unit -)
tid range: 1966-01-01 to 2024-01-01
</table>
<table>
id: vnan1
description: Versionstabel NAN1 - Forsyningsbalance (år) efter version, transaktion, prisenhed og tid
columns: version, transakt, prisenhed, tid (time), indhold (unit -)
tid range: 1966-01-01 to 2024-01-01
</table>
<table>
id: nan2
description: Real disponibel bruttonationalindkomst mv. efter transaktion, prisenhed og tid
columns: transakt, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 1966-01-01 to 2024-01-01
</table>
<table>
id: nan3
description: Forbrug, disponibel indkomst og opsparing for husholdninger og NPISH efter transaktion, prisenhed og tid
columns: transakt, prisenhed, tid (time), indhold (unit -)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: nkn1
description: Forsyningsbalance, Bruttonationalprodukt (BNP), beskæftigelse mv. efter transaktion, prisenhed, sæsonkorrigering og tid
columns: transakt, prisenhed, saeson, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2025-04-01
</table>
<table>
id: vnkn1
description: Versionstabel NKN1 - Forsyningsbalance (kvartaler) efter version, transaktion, prisenhed, sæsonkorrigering og tid
columns: version, transakt, prisenhed, saeson, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2025-04-01
</table>
<table>
id: nkn2
description: Real disponibel bruttonationalindkomst mv. efter transaktion, prisenhed, sæsonkorrigering og tid
columns: transakt, prisenhed, saeson, tid (time), indhold (unit Mio. kr.)
tid range: 1990-01-01 to 2025-04-01
</table>
<table>
id: nkn3
description: Forbrug, disponibel indkomst og opsparing for husholdninger og NPISH, sæsonkorrigeret efter transaktion, prisenhed og tid
columns: transakt, prisenhed, tid (time), indhold (unit -)
tid range: 1999-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- All 8 tables share the same key pattern: transakt selects the measure (BNP, import, export, consumption, employment, etc.) and prisenhed selects the unit/method (løbende priser, kædede 2020-priser, per capita, vækstrate). ALWAYS filter both to a single value — every query needs WHERE transakt='...' AND prisenhed='...'.
- Three content groups: (1) Forsyningsbalance/BNP (nan1/nkn1/vnan1/vnkn1) — expenditure approach with 31 transakt codes including employment. (2) Nationalindkomst (nan2/nkn2) — income approach from BNP → disponibel indkomst, 18 transakt codes in Mio. kr. (3) Husholdninger og NPISH (nan3/nkn3) — consumption, income, savings for households only, 11 transakt codes.
- Annual vs quarterly: nan1/nan2/nan3 are annual (from 1966/1966/1995). nkn1/nkn2/nkn3 are quarterly (from 1990/1990/1999). Quarterly tables add saeson column (Y/N) — a third selector that must also be filtered; nkn3 is the exception (always seasonally adjusted, no saeson column).
- For revision analysis: use vnan1 (42 annual vintages) or vnkn1 (44 quarterly vintages, F=first estimate, R=revised). Filter version to a single value for normal queries; self-join two versions to compare revisions.
- Real price codes differ between annual and quarterly: annual uses RAN/LAN_* (nan1/nan2), quarterly uses RKV/LKV_* (nkn1/nkn2/nkn3). They represent the same concept (2020-priser kædede værdier).
- Growth rates (prisenhed='L_V') and contribution to growth (prisenhed='L_VB') are in nkn1/nan1 only, not in nan2/nan3/nkn2/nkn3. Do not sum L_V or L_VB across transakt values.
- Employment (EMPH_DC hours, EMPM_DC persons) is in nan1/nkn1 only. These transakt codes only support prisenhed IN ('V_M','L_V') — no chained price variants.
- For most analytical questions about Danish GDP, use nan1 (annual, long history) or nkn1 (quarterly, seasonally adjusted growth). For income distribution/household analysis, use nan3 or nkn3.