table: fact.recidv10
description: Personer efter køn, alder, tidligere domme, recidiv hændelser, varighed til tilbagefald og tid
measure: indhold (unit Antal)
columns:
- konams: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [00=I alt, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- tidldom: values [0=I alt, 0=Ingen tidligere domme, 1=1 tidligere dom, 2=2 tidligere domme, 3=3 tidligere domme, 4=4 tidligere domme, 5=5-9 tidligere domme, 10=10 eller flere tidligere domme]
- rechen: values [0=I alt, 106=Ingen tilbagefald, 107=1 tilbagefald, 108=2 tilbagefald, 109=3 tilbagefald, 110=4-9 tilbagefald, 111=10 eller flere tilbagefald]
- vartilbage: values [0=I alt, 0=Ingen tilbagefald, 6=I løbet af 6 måneder, 712=Efter 6 måneder og indenfor 1 år, 1324=Efter 1 år og indenfor 2 år]
- tid: date range 2009 to 2024
notes:
- Uses konams (not kon) and alder (varchar, not alder1 smallint). alder starts at 2024 (20-24 år) — no 15-19 age group; this table covers convicted persons who need a conviction history, so younger ages are absent.
- tid is rolling 3-year follow-up windows (starts 2009). Do not sum across overlapping tid values.
- tidldom (prior convictions): ColumnValues shows id=0 twice ("I alt" and "Ingen tidligere domme") — metadata quirk; only one code 0 in data, meaning I alt. tidldom=1 through 5/10 are the specific prior-conviction counts.
- rechen and vartilbage are cross-tabulated. rechen=106 (Ingen tilbagefald) only appears with vartilbage=0. For rechen=107+ (those with recidivisms), vartilbage=0 is their I alt and vartilbage=6/712/1324 breaks down time to first recidivism.
- 5 dimension columns all have total rows (TOT/"0"/0). Clean total: konams='TOT', alder='0', tidldom=0, rechen=0, vartilbage=0, single tid.
