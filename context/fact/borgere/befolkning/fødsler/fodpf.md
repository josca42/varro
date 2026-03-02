table: fact.fodpf
description: Levendefødte efter faders alder, levendefødtnummer og tid
measure: indhold (unit Antal)
columns:
- faald: values [9915=Under 15 år, 15=15 år, 16=16 år, 17=17 år, 18=18 år ... 66=66 år, 67=67 år, 68=68 år, 69=69 år, 7099=70 år og derover]
- lfnr: values [1=1. barn, 2=2. barn, 3=3. barn, 4=4. barn, 5=5. barn, 6=6. barn, 7=7. barn, 8+=8. barn og flere, 99=Uoplyst]
- tid: date range 2007-01-01 to 2024-01-01
notes:
- No total rows in either column. faald holds individual father ages 15–69 plus boundary codes 9915 (Under 15) and 7099 (70+). lfnr is birth-order 1–7 and 8+ — the listed 99=Uoplyst is absent from the actual data.
- All lfnr categories are mutually exclusive. SUM all rows for a given tid and faald to get total births for that father's age.
- Note the boundary age codes: 9915 sorts before 15 alphabetically/numerically, 7099 sorts after 69. Cast to integer carefully if ordering by age.
