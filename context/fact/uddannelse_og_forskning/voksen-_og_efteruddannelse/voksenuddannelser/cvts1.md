table: fact.cvts1
description: Efteruddannelse i virksomhederne (CVTS) efter type af efteruddannelse på virksomhed, antal ansatte og tid
measure: indhold (unit Pct.)
columns:
- eftervir: values [1=Virksomheder med kurser, 10=Uden uddannelse, 2=Virksomheder med eksterne kurser, 3=Virksomheder med interne kurser, 4=Virksomheder med anden efteruddannelse, 5=Sidemandsoplæring, 6=Jobrotation, 7=ERFA-grupper, 8=E-læring, 9=Konferencer]
- ansatte: values [104=Alle virksomheder, 101=10-49 ansatte, 102=50-249 ansatte, 103=250 ansatte og derover]
- tid: date range 2005-01-01 to 2020-01-01

notes:
- indhold is percentage of companies — not a count. Never sum indhold across eftervir values.
- eftervir values are NOT mutually exclusive. Code 1 (virksomheder med kurser) is a superset that includes codes 2 (externe) and 3 (interne). Code 10 (uden uddannelse) is the complement of code 1. Codes 4–9 (sidemandsoplæring, jobrotation, ERFA, e-læring, konferencer, anden efteruddannelse) may also overlap. Pick one eftervir code per query.
- ansatte=104 is the "alle virksomheder" aggregate. ansatte 101/102/103 are size bands that sum to approximately 104.
- Only goes to 2020 — this is CVTS survey data (Continuing Vocational Training Survey), conducted every ~5 years. The table has sparse years; check distinct tid values before assuming annual coverage.