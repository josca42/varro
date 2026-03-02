<fact tables>
<table>
id: zoo3
description: Aktivitet i zoologiske haver og akvarier efter zookategori, zootype, aktivitet og tid
columns: zookat, zoo, aktivitet, tid (time), indhold (unit Antal)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: zoo4
description: Besøg i zoologiske haver og akvarier efter zookategori, zootype, besøgstype og tid
columns: zookat, zoo, besogstype, tid (time), indhold (unit Antal)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: kv2for1
description: Besøg i forlystelsespark, zoologisk have m.m. efter sted, køn, alder og tid
columns: sted, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For total annual visits to zoos/aquaria over time (2021–2024): use zoo3 (filter aktivitet=420) or zoo4 (filter besogstype=640). Both give the same total visitor count; zoo4 adds the breakdown by ticket type and age group.
- For other activity metrics (opening hours, educational events, volunteers, revenue): zoo3 is the only option — filter to the relevant aktivitet value. Never sum across aktivitet values; they measure different things.
- For survey data on share of Danes who visited: use kv2for1. Only 2024, single time point, values are percentages — not comparable to the absolute counts in zoo3/zoo4.
- zoo3 and zoo4 share the same zookat and zoo dimensions. zookat=740 covers both zoos and aquaria combined, 745=zoos only, 750=aquaria only. zoo=TOT5 is grand total across funding types. Always filter both columns to your target to avoid double-counting.
- zoo3 has 12 NULL aktivitet rows only in 2021 — exclude them (WHERE aktivitet IS NOT NULL) when doing time-series comparisons.