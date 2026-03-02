table: fact.ligeab5
description: Beskæftigede i støttet beskæftigelse efter branche (DB07), ydelsestype, køn, alder og tid
measure: indhold (unit Antal)
columns:
- branche07: join dim.db on branche07=kode::text; levels [2, 3]
- ydelsestype: values [TOT=I alt, LT=Løntilskud, JB=Jobrotation, FL=Fleksjob, SK=Skånejob, SJ=Servicejob, VL=Voksenlærling, RV=Revalidering]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- branche07 has 12 values total (10 match dim.db at levels 2-3, plus TOT and code '4' which don't match). Use ColumnValues("ligeab5", "branche07") — the labels are already there. Small table, all branche07 values have labels inline.
- ydelsestype has TOT plus 7 subsidy types. Filter to TOT for all subsidised employment combined.
- kon has TOT, M, K.
- Table covers only persons in støttet beskæftigelse (subsidised employment). Counts are smaller than regular employment tables.
