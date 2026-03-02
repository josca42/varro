<fact tables>
<table>
id: idrakt01
description: Idrætsorganisationernes medlemmer efter område, aktivitet, køn, alder og tid
columns: blstkom, aktivitet, kon, alder1, tid (time), indhold (unit Antal)
tid range: 2014-01-01 to 2024-01-01
</table>
<table>
id: idrakt02
description: Idrætsorganisationernes medlemskaber (andel af befolkningen) efter område, køn, alder og tid
columns: blstkom, kon, alder1, tid (time), indhold (unit Pct.)
tid range: 2014-01-01 to 2024-01-01
</table>
<table>
id: medalje1
description: Danske vindere af internationale sportsmedaljer efter mesterskab, idrætsgrene, medalje og tid
columns: mester, idraet, medalje, tid (time), indhold (unit Antal)
tid range: 1980-01-01 to 2024-01-01
</table>
<table>
id: idrres01
description: Idrætsresultater i OL-discipliner efter disciplin, land, præstation og tid
columns: diciplin, land, praestation, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: idrres02
description: Idrætsresultater i OL-discipliner efter disciplin, land, relativ præstation og tid
columns: diciplin, land, relativ, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: idrrang1
description: Rangering af samlet præstation i OL-discipliner efter disciplin, land, præstation, rangplacering og tid
columns: diciplin, land, praestation, rang, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: idrvan1a
description: Voksnes idrætsudøvelse efter køn og alder, idrætsgrene og tid
columns: konalder, idraet, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: idrvan02
description: Voksnes idrætsudøvelse efter køn og alder, deltagelse og tid
columns: koal, deltag1, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: idrvan04
description: Idrætsaktive voksnes idrætsudøvelse efter køn og alder, tidsforbrug og tid
columns: koal, tidbrug, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: idrvan05
description: Voksnes idrætsudøvelse efter køn og alder, organisering og tid
columns: koal, organ1, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: idrvan06
description: Voksnes idrætsudøvelse efter højest fuldførte uddannelse, deltagelse og tid
columns: uddannelsef, deltag1, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: idrvan08
description: Voksnes idrætsudøvelse efter socioøkonomisk status, deltagelse og tid
columns: socio, deltag1, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: idrvan9a
description: Børns idrætsudøvelse efter alder og køn, idrætsgrene og tid
columns: alderk, idraet, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: idrvan10
description: Børns idrætsudøvelse efter alder og køn, deltagelse og tid
columns: alderk, deltag1, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: idrvan12
description: Idrætsaktive børns idrætsudøvelse efter alder og køn, tidsforbrug og tid
columns: alderk, tidbrug, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: idrvan13
description: Børns idrætsudøvelse efter alder og køn, organisering og tid
columns: alderk, organ1, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: idrvan14
description: Børns idrætsudøvelse efter alder og køn, forældres baggrund og tid
columns: alderk, forback, tid (time), indhold (unit Pct.)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: idrtil01
description: Tilskuertal til udvalgte sportsgrene efter sportsgren, tilskuere og kampe og tid
columns: sports, tilskuer, tid (time), indhold (unit Antal)
tid range: 2006/2007 to 2024/2025
</table>
<table>
id: kv2mo1
description: Forbrug af sport og motion efter sted, køn, alder og tid
columns: sted, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mo2
description: Forbrug af sport og motion efter ledsager, køn, alder og tid
columns: ledsag, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mo3
description: Forbrug af sport og motion efter type af sport og motion, køn, alder og tid
columns: typsport, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mo4
description: Barrierer for forbrug af sport og motion efter årsag, køn og tid
columns: aarsag, kon, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mo5
description: Barrierer for forbrug af tilskuersport efter årsag, køn og tid
columns: aarsag, kon, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- **Survey tables (idrvan\*) are not annual** — data collected every 3-4 years (2007, 2011, 2016, 2020, 2024). These are survey-based percentages, not administrative registrations.
- **Adults vs. children**: idrvan1a/02/04/05/06/08 cover adults (16+); idrvan9a/10/12/13/14 cover children (7-15). The konalder/koal/alderk columns mix gender and age into one dimension — do not sum gender + age rows together.
- **Sports participation by sport** (which sports do people do): idrvan1a (adults, 2007–2024), idrvan9a (children, 2007–2024). Both have non-mutually-exclusive idraet values — each row is an independent percentage, never sum them.
- **Sports participation rate** (do they exercise at all): idrvan02 (adults), idrvan10 (children) — deltag1 is mutually exclusive and sums to ~100%.
- **Sports organisation membership with geographic breakdown**: idrakt01 (raw count Antal) or idrakt02 (% of population). Both join dim.nuts (niveau 2=landsdele, niveau 3=kommuner). Code 0 = national total, not in dim.
- **International medals**: medalje1 for Danish medal winners (1980–2024) by championship, sport, medal type. idrres01 for raw OL placement counts by country (2016–2024). idrres02 for population-adjusted OL metrics. idrrang1 for country rankings — use RANG10 to compare Denmark to similarly-sized countries.
- **Spectator sport**: idrtil01 for attendance at specific Danish leagues and landshold (2006/07–2024/25). MUST filter tilskuer to one measurement type (antal tilskuere / kampe / gennemsnit pr. kamp) — missing filter triples all sums. tid uses season format ("2006/2007").
- **kv2mo1–5 are 2024-only**: a new survey on sport/motion consumption patterns (location, companion, type) and barriers for non-participants. All categorical dimensions are non-mutually-exclusive — each row is an independent percentage.
- **Common pitfall**: idraet, organ1, sted, ledsag, typsport, and aarsag columns all exceed 100% when summed across their values. Never aggregate across these. Only deltag1 and tidbrug are mutually exclusive distributions safe to compare as a group.
- **Map**: idrakt01 and idrakt02 support choropleth maps — merge blstkom=dim_kode on context/geo/kommuner.parquet (niveau 3) or context/geo/landsdele.parquet (niveau 2). Exclude blstkom IN (0, 99). All other tables in this subject have no geographic dimension.