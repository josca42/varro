<fact tables>
<table>
id: varer
description: Industriens salg af egne varer (kvartal) efter varegruppe, enhed og tid
columns: varegr, enhed, tid (time), indhold (unit -)
tid range: 1995-01-01 to 2024-10-01
</table>
<table>
id: varer1
description: Industriens salg af egne varer (år) efter varegruppe, enhed og tid
columns: varegr, enhed, tid (time), indhold (unit -)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: varer2s
description: Industriens salg af egne varer, SITC (kvartal) efter SITC-hovedgrupper, sæsonkorrigering og tid
columns: sitc, saeson, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2024-10-01
</table>
<table>
id: varer3
description: Industriens salg af egne varer, SITC (år) efter SITC-hovedgrupper og tid
columns: sitc, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: oms5
description: Industriens salg (kvartal) efter branche (DB07), omsætningstype, sæsonkorrigering og tid
columns: branche07, omstype, saeson, tid (time), indhold (unit 1.000 kr.)
tid range: 2000-01-01 to 2024-10-01
</table>
<table>
id: oms6
description: Industriens salg (år) efter branche (DB07), omsætningstype og tid
columns: branche07, omstype, tid (time), indhold (unit 1.000 kr.)
tid range: 2000-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Suffix pattern: tables without suffix or ending in a number = annual or quarterly by product (varer/varer1), tables with 's' = includes sæsonkorrigering (varer2s, oms5). 'k' in name → quarterly, annual otherwise — but here: varer=quarterly, varer1=annual, varer2s=quarterly, varer3=annual, oms5=quarterly, oms6=annual.
- For sales by product (varegruppe, CN10): use varer (quarterly, 1995–) or varer1 (annual, 1995–). Both have enhed (V=value/M=quantity) — must filter. dim.kn join does NOT work; use ColumnValues for product labels.
- For sales by SITC product group: use varer2s (quarterly, saeson, 2007–) or varer3 (annual, 2007–). SITC niveau 2 joins dim.sitc; TOT/TOT0-TOT8 are aggregate rows to exclude before joining.
- For sales by industry branch: use oms5 (quarterly, saeson, 2000–) or oms6 (annual, 2000–). These have omstype breakdown (SAMLET/EGVARE/TJENIALT/HANDEL etc.) — hierarchical, filter to one level.
- Key gotcha across all tables: measurement selector columns (enhed in varer/varer1, saeson in varer2s/oms5) silently double counts if not filtered. omstype in oms5/oms6 is hierarchical — summing across omstype values inflates totals.
- branche07 in oms5/oms6 is a custom survey classification (not standard dim.db). Use ColumnValues to browse — letter codes (B, C, CA...) are NACE aggregates; 5-digit numerics (10001, 10002...) are sub-industries.