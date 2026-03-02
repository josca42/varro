table: fact.aus07
description: Fuldtidsledige (sæsonkorrigeret) efter ydelse køn og alder, sæsonkorrigering og faktiske tal og tid
measure: indhold (unit -)
columns:
- yd: values [TOT=Bruttoledige, NET=Nettoledige, LDP=Nettoledige dagpengemodtagere, LKT=Nettoledige kontanthjælpsmodtagere, AKI=Aktiverede i alt, ADP=Aktiverede dagpengeberettigede, AKT=Aktiverede kontanthjælpsmodtagere (arbejdsmarkedsparate), MEN=Mænd, KVR=Kvinder, U25=16-24 år, O25=25-29 år, O30=30-39 år, O40=40-49 år, O50=50-59 år, O60=60 år og derover]
- saesonfak: values [9=Sæsonkorrigeret i pct. af arbejdsstyrken, 10=Sæsonkorrigeret, 22=Opregnede faktiske i pct. af arbejdsstyrken, 24=Opregnede faktiske]
- tid: date range 2007-01-01 to 2025-09-01

notes:
- saesonfak is a measurement selector — always filter to one. 10=seasonally adjusted count, 24=actual count, 9/22=percentage forms.
- yd column is highly unusual: it mixes ydelsestype (TOT, NET, LDP, LKT, AKI, ADP, AKT), køn (MEN, KVR), and alder (U25, O25, O30, O40, O50, O60) all in a single column. These values are NOT mutually exclusive — MEN+KVR=TOT, components add up to aggregates. Always select exactly one yd value; never sum across multiple yd values.
- saesonfak 9/22 (percentage) only available for TOT, NET, MEN, KVR — not for individual ydelse components or age groups.
- National level only; no omrade column.