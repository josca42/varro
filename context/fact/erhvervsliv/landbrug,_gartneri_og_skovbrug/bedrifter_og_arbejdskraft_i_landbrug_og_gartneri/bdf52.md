table: fact.bdf52
description: Bedrifter efter enhed, areal, landmandens alder og tid
measure: indhold (unit -)
columns:
- enhed: values [ANTAL=Bedrifter (antal), AREAL=Samlet dyrket areal (ha)]
- areal1: values [AIALT=I alt, A1=Under 10,0 ha, A19=10,0 - 19,9 ha, A29=20,0 - 29,9 ha, A49=30,0 - 49,9 ha, A62=50,0 - 74,9 ha, A100=75,0 - 99,9 ha, A210=100,0 - 199,9 ha, A220=200,0 ha og derover]
- bdfalder: values [IALT=Alder i alt, 25UN=Under 25 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75OV=75 år og derover, 999=Uoplyst alder]
- tid: date range 1984-01-01 to 2024-01-01

notes:
- enhed is a measure-type selector: ANTAL (farm count) or AREAL (ha). Filter to one — the same farm/area appears twice in every cross-section.
- areal1: AIALT = all farm sizes. Filter to AIALT unless you need a specific size class.
- bdfalder: IALT = all ages. 999=Uoplyst alder is a separate real category, not a total. Filter to IALT for national totals without age breakdown.
- Longest series in the subject for farm counts by farmer age (back to 1984), but no regional breakdown — national only.