<fact tables>
<table>
id: orgout11
description: International outsourcing efter firma, branche (DB07 10-grp), funktioner og tid
columns: firma, branchedb0710, funktioner, tid (time), indhold (unit Antal)
tid range: 2009 to 2024
</table>
<table>
id: orgout21
description: Outsourcede job fra Danmark til udlandet efter branche (DB07 10-grp.), jobtype og tid
columns: branche0710, jobtyp, tid (time), indhold (unit Antal)
tid range: 2009 to 2024
</table>
<table>
id: orgout36
description: Firmaers international outsourcing efter destination efter funktioner, destination og tid
columns: funktioner, destina, tid (time), indhold (unit Antal)
tid range: 2009 to 2024
</table>
<table>
id: orgout41
description: Firmaers motiver for international outsourcing efter branche (DB07 10-grp.), motiver, betydning og tid
columns: branche0710, motiv, betyd, tid (time), indhold (unit Pct.)
tid range: 2009 to 2024
</table>
<table>
id: orgout60
description: Firmaers forhold for organisering af deres globale værdikæder efter branche (DB07 10-grp), forholdstype, betydning og tid
columns: branchedb0710, fortyp, betyd, tid (time), indhold (unit Andel i pct.)
tid range: 2021 to 2024
</table>
</fact tables>

notes:
- All tables use int4range for tid with 4 survey waves: [2009,2012), [2014,2017), [2018,2021), [2021,2024). These are 3-year survey periods, not annual data. There are gaps: 2012–2014 and 2017–2018 have no data. Filter tid with e.g. WHERE tid = '[2021,2024)'::int4range.
- For number of firms doing international outsourcing (by industry or function type): use orgout11. Key gotcha: firma='SINT' for outsourcing firms only, firma='TOT' for all firms in scope.
- For number of outsourced jobs (total or high-skilled): use orgout21. IS_LOST_HIGH is a subset of IS_LOST — don't sum them.
- For geographic destination of outsourcing: use orgout36. Destination counts overlap (firms can outsource to multiple countries), so individual destinations don't add up to SINT.
- For why firms outsource (motives, rated by importance): use orgout41. indhold is %, and betyd (VERYIMP/IMP/NOTIMP/'') distributes 100% per motive. Filter to one betyd value; never sum across betyd.
- For global value chain challenges (supply shortages, cost increases, sanctions): use orgout60. Same betyd distribution structure as orgout41. Only covers [2021,2024).
- orgout41 and orgout60 both have a betyd column where NA/Ikke relevant is stored as '' (empty string), not 'NA'.