table: fact.kys01
description: Kontanthjælp (sæsonkorrigeret) efter visitation, sæsonkorrigering, alder, køn og tid
measure: indhold (unit Antal)
columns:
- visitation: values [TOT=I alt, 1A=Jobparate (inkl. åbentlyst uddannelsesparate), 2A=Aktivitetsparate (inkl. uddannelsesparate og uoplyste)]
- saeson: values [10=Sæsonkorrigeret, 20=Faktiske tal]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2539=25-39 år, 4099=40 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2025-06-01
notes:
- saeson is a measurement selector: 10=Sæsonkorrigeret, 20=Faktiske tal. Every dimension combination appears twice. Always filter to one value — use saeson=20 for actual figures, saeson=10 for smoothed trend analysis.
- visitation uses coarser groupings than ky01: TOT, 1A=Jobparate (includes åbenlyst uddannelsesparate), 2A=Aktivitetsparate (includes uddannelsesparate and uoplyst). Cannot distinguish the fine categories here.
- alder uses only 3 bands (16-24, 25-39, 40+) — coarser than ky01. For finer age breakdown use ky01.
- All non-time columns have TOT rows. For a simple national monthly count: WHERE saeson='20' AND visitation='TOT' AND alder='TOT' AND kon='TOT'.
