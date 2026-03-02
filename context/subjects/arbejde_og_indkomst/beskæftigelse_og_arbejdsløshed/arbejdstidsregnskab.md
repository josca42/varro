<fact tables>
<table>
id: atr110
description: Arbejdstidsregnskab (kvartal) efter branche (DB07), sektor, type, socioøkonomisk status og tid
columns: branche07, sektor, type, socio, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2025-04-01
</table>
<table>
id: atr112
description: Arbejdstidsregnskab (kvartal) (sæsonkorrigeret) efter branche (DB07 10- og 19-grp), type, socioøkonomisk status og tid
columns: branchedb071038, type, socio, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2025-04-01
</table>
<table>
id: atr114
description: Arbejdstidsregnskab (kvartal) (sæsonkorrigeret) efter sektor, type, socioøkonomisk status og tid
columns: sektor, type, socio, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2025-04-01
</table>
<table>
id: atr116
description: Arbejdstidsregnskab (år) efter branche (DB07), sektor, type, socioøkonomisk status, køn og tid
columns: branche07, sektor, type, socio, kon, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: atr118
description: Arbejdstidsregnskab på nationalregnskabets branchegrupperinger (år) efter branche (DB07), sektor, type, socioøkonomisk status, køn og tid
columns: branche07, sektor, type, socio, kon, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: atr122
description: Arbejdstidsregnskab (år), indeks efter køn, sektor, type og tid
columns: kon, sektor, type, tid (time), indhold (unit Indeks)
tid range: 2008-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- All tables share a critical pattern: `type` is always a measurement selector (HAC/HACS=timer, ABESK=beskæftigede, AJOB=job, WSUM=lønsum). Every dimension combination appears once per type — always filter to one type or counts will be 4x too high.
- Quarterly unadjusted: atr110 (with branche + sektor). Quarterly seasonally adjusted: atr112 (branche, no sektor) and atr114 (sektor only, no branche). Annual: atr116, atr118, atr122.
- For industry breakdown by quarter: use atr110. For seasonal trend analysis: use atr112 (with branche) or atr114 (without branche).
- For annual data with gender (kon): use atr116. It has the most dimensions: branche + sektor + socio + kon.
- For national accounts context (GDP components): use atr118. Its branche classification is nationalregnskabets branchegrupperinger — different from standard DB07, with two parallel coding series (5-digit and 6-digit) in the same column.
- For index trends since 2008: use atr122 (no branche, just kon + sektor).
- The `branche07` column in atr110, atr112, atr116 mixes multiple classification schemes (10-gruppe numeric + 19-gruppe letter codes) in the same column. Never GROUP BY branche07 without first filtering to one scheme — see individual fact doc notes.
- `socio` codes differ by table: atr110/112/114 have codes 13, 14, TOT (where 14 is a custom group not in dim.socio); atr116/118 have 11, 12, 13, TOT (standard niveau 2 socio codes, all join dim.socio).