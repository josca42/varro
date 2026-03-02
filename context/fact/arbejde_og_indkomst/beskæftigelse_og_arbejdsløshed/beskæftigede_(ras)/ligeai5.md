table: fact.ligeai5
description: Ligestillingsindikator for beskæftigede (over 15 år) i støttet beskæftigelse efter branche (DB07), ydelsestype, indikator og tid
measure: indhold (unit -)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [2, 3]
- ydelsestype: values [TOT=I alt, LT=Løntilskud, JB=Jobrotation, FL=Fleksjob, SK=Skånejob, SJ=Servicejob, VL=Voksenlærling, RV=Revalidering]
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- indhold is a gender indicator, NOT a count. Same as ligeai3/4: LA1, LA2, LA3. Never sum across indikator values.
- ydelsestype has TOT plus 7 subsidy types. Filter to TOT for all subsidised employment.
- branche07 uses DB07-127 intermediate coding — small set (12 codes). Use ColumnValues("ligeai5", "branche07").
