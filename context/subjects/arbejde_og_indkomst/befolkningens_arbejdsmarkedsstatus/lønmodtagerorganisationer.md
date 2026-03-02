<fact tables>
<table>
id: lonmed3
description: Lønmodtagerorganisationernes medlemstal pr. 31.12 (Enkelte organisationer) efter medlemsorganisationer, køn og tid
columns: medorg, koen, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: lonmed2
description: Lønmodtagerorganisationernes medlemstal pr. 31.12 (Hovedorganisationer) efter medlemsorganisationer, køn og tid
columns: medorg, koen, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Use lonmed2 for totals or comparisons between the 4 main umbrella organizations (FH, Ledernes, AC, Uden for). Clean table, no gotchas.
- Use lonmed3 for data on specific individual unions/associations (115 organizations). Always filter by exact medorg code — do NOT use medorg='0' (it's assigned to both the grand total and the "2B" organization, causing duplicate rows from 2009 onwards).
- Both tables cover 2007–2024 annually (pr. 31.12). Both share the same koen column (TOT/M/K) — always filter to one value.
- Never sum indhold across multiple medorg values in lonmed3: individual orgs roll up into umbrella bodies, so you'd double-count.