table: fact.skolm04b
description: Ansatte på musikskolerne efter køn, alder, uddannelse og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 0049=49 år og derunder, 5099=50 år og derover]
- uddannelse: values [0=Uddannelse i alt, 10700=Konservatorie, 10715=Studerende, 10720=Seminarium, 10725=Universitet, 10740=Anden uddannelse, 9997=Ingen eller uoplyst uddannelse]
- tid: date range 2021 to 2025

notes:
- Counts individual employees (headcount), not FTE. Use skolm04a for FTE (årsværk).
- No regional or municipality breakdown — national totals only.
- TOT rows present for kon, alder, and uddannelse. Filter all three to avoid overcounting: kon='TOT', alder='TOT', uddannelse='0' for the national total. Pick one dimension and filter the rest to totals.
- alder has only two groups (0049=under 50, 5099=50 and over) — very coarse breakdown.