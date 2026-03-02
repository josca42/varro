table: fact.hdyr1
description: Landbrug med dyr efter areal, enhed, art og tid
measure: indhold (unit -)
columns:
- areal1: values [AIALT=I alt, A1=Under 10,0 ha, A19=10,0 - 19,9 ha, A29=20,0 - 29,9 ha, A49=30,0 - 49,9 ha, A62=50,0 - 74,9 ha, A100=75,0 - 99,9 ha, A210=100,0 - 199,9 ha, A220=200,0 ha og derover]
- enhed: values [ANTAL=Bedrifter (antal), DYR=Dyr (antal)]
- art: values [D1=Heste, D2=Tyre- og studekalve, - under 1/2 år, D3=Tyre- og studekalve, 1/2-1 år, D39=Tyre- og studekalve i alt, D4=Tyre og stude, 1-2 år ... D35=Høns i alt, D36=Kalkuner, D362=Ænder, D364=Gæs, D366=Fjerkræ i alt]
- tid: date range 1982-01-01 to 2024-01-01

notes:
- enhed is a measurement selector (ANTAL=bedrifter, DYR=dyr). Every art×areal1 combination is repeated for both enhed values. Always filter to one.
- art has 146 values with the same mixed coding scheme as hdyr07's dyr column: D-prefix codes are specific animal categories; letter-prefix codes (MK, AK, KK, K, SO, SS, S, F, MF) are herd size groups per animal type. Never sum across different prefix families. Use ColumnValues("hdyr1", "art") to find the right code.
- areal1 has AIALT (national total across all farm sizes) + 8 farm size groups (A1=under 10 ha, ..., A220=200+ ha). Filter to AIALT for a simple total; use size groups for farm-size-stratified analysis.
- Longest regional alternative for farm-size breakdown: goes back to 1982 (hdyr07 goes back to 2006 with regional breakdown; hdyr1 has farm-size breakdown instead of geographic).