table: fact.kuarb3
description: Ansatte på kulturarbejdspladser efter køn, kulturemne, jobtype og tid
measure: indhold (unit Antal)
columns:
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- kulturemne: join dim.kulturemner on kulturemne::text=kode [approx: Fact int64 vs dim object KODE; top-level codes 1-6 match semantically]; levels [1]
- jobtyp: values [HJ=Hovedjob ultimo november, BJ=Bijob ultimo november]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/kulturemner.md

notes:
- kulturemne: same unreliable join situation as kuarb2 — use inline ColumnValues for labels.
- jobtyp: HJ=Hovedjob, BJ=Bijob. These are distinct job-slot types, NOT mutually exclusive for a person (someone can hold both a main and a side job in culture). Do NOT sum HJ + BJ expecting a person count — you will overcount. There is no total row for jobtyp.
- kon=10 is the total; filter when comparing gender.