table: fact.pl2
description: Bedrifter efter enhed, præcisionsteknologi, uddannelse og alder og tid
measure: indhold (unit -)
columns:
- enhed: values [ANTAL=Bedrifter (antal), AREAL=Samlet dyrket areal (ha)]
- praetek: values [100=Alle bedrifter med dyrket areal, 110=Bedrifter med præcisionsteknologi, 120=Bedrifter uden præcisionsteknologi]
- udalder: values [200=Uddannelse i alt, 220=Udelukkende praktisk erfaring, 230=Grundlæggende landbrugsuddannelse, 240=Driftsleder eller jordbrugsvidenskabelig uddannelse, 300=Alder i alt, 310=Under 40 år, 320=40-49 år, 330=50-60 år, 340=60 år og derover, 350=Alder uoplyst]
- tid: date range 2018-01-01 to 2025-01-01

notes:
- enhed is a measure-type selector: ANTAL or AREAL. Always filter to one.
- praetek has only 3 summary codes (100/110/120) — no specific technology breakdown (use pl1 for that).
- udalder combines two completely independent dimension categories in one column: uddannelse (200=Uddannelse i alt, 220-240 = education levels) and alder (300=Alder i alt, 310-350 = age brackets). Filter to ONE group per query — either education (WHERE udalder BETWEEN 200 AND 299) OR age (WHERE udalder BETWEEN 300 AND 399). Mixing both groups in a SUM is wrong.
- 200=Uddannelse i alt and 300=Alder i alt are each the total for their own group, not a combined total.
- National only, no regional breakdown.