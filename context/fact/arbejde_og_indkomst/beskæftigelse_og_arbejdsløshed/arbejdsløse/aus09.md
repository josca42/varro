table: fact.aus09
description: Ledighedsindikator efter ydelsestype, sæsonkorrigering og faktiske tal og tid
measure: indhold (unit -)
columns:
- ydelsestype: values [TOT=Bruttoledige, LDM=Ledige dagpengemodtagere, LKM=Ledige kontanthjælpsmodtagere]
- saesonfak: values [9=Sæsonkorrigeret i pct. af arbejdsstyrken, 10=Sæsonkorrigeret, 22=Opregnede faktiske i pct. af arbejdsstyrken, 24=Opregnede faktiske]
- tid: date range 2007-01-01 to 2025-09-01

notes:
- saesonfak is a measurement selector — every (ydelsestype, tid) combination appears up to 4 times, once per saesonfak. Always filter to exactly one: 10 for seasonally-adjusted count, 24 for actual count, 9 for pct seasonally adjusted, 22 for pct actual. Failing to filter inflates sums by 2-4x.
- saesonfak 9 and 22 (percentage of workforce) only appear for TOT=Bruttoledige; LDM and LKM only have 10 and 24.
- ydelsestype: TOT≈LDM+LKM but not exact (different methodology). National level only; for regional breakdown use aus08.