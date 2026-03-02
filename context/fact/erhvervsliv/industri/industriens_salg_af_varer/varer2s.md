table: fact.varer2s
description: Industriens salg af egne varer, SITC (kvartal) efter SITC-hovedgrupper, sæsonkorrigering og tid
measure: indhold (unit 1.000 kr.)
columns:
- sitc: join dim.sitc on sitc=kode [approx]; levels [2]
- saeson: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 2007-01-01 to 2024-10-01
dim docs: /dim/sitc.md

notes:
- sitc joins dim.sitc at niveau 2 (Gruppe, 63 codes). TOT, TOT0–TOT8 are aggregates (grand total + division totals 0–8) not present in dim.sitc — filter them out with WHERE sitc NOT LIKE 'TOT%' before joining, or handle separately. Use ColumnValues("varer2s", "sitc") to browse all 74 codes with labels.
- saeson is a measurement selector: EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret. Every sitc×tid combination appears twice. Always filter to one: WHERE saeson='EJSÆSON' for raw figures or 'SÆSON' for seasonally adjusted. Omitting doubles all values.
- All values in 1.000 kr. (value only — no quantity dimension here, unlike varer/varer1).