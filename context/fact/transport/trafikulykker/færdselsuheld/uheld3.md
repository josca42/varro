table: fact.uheld3
description: Færdselsuheld med personskade efter uheldsart, uheldssituation, by/landområde, hastighedsbegrænsning og tid
measure: indhold (unit Antal)
columns:
- uhelda: values [0=Alle uheld, 1000=Spiritusuheld, 2000=Øvrige uheld]
- uheldsit: values [0=Eneuheld, 100=Indhentningsuheld, 200=Mødeuheld, 300=Svingningsuheld mellem medkørende, 400=Svingningsuheld mellem modkørende, 500=Uheld mellem krydsende køretøjer, 600=Svingningsuheld mellem krydsende køretøjer, 700=Parkeringsuheld, 800=Fodgængeruheld, 900=Forhindringsuheld, 999=Uoplyst]
- byland: values [1=I byzone, 2=I landzone]
- hast: values [0=Uoplyst, 1=20 km/t og derunder, 2=25-50 km/t, 3=60 km/t, 4=70 km/t, 5=80 km/t, 6=90 km/t, 7=100 km/t, 8=110 km/t, 9=120 km/t, 10=130 km/t]
- tid: date range 1997-01-01 to 2024-01-01
notes:
- uhelda=0 (Alle uheld) is an aggregate equal to Spiritusuheld + Øvrige uheld. Always filter to one uhelda value — summing across all three silently triples counts.
- uheldsit=0 means Eneuheld (single-vehicle accident), NOT a total. There is no aggregate code for uheldsit; all 10 situation types (0–999) are mutually exclusive and exhaustive — sum across all to get the full total.
- hast=0 means Uoplyst (unknown speed limit), not an aggregate.
- byland has only 2 values (I byzone / I landzone) — no total code. Sum both to get the national figure.
- Typical total query: filter uhelda='0', then GROUP BY uheldsit or hast or byland without additional filters.
