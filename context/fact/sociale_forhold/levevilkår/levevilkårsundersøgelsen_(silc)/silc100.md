table: fact.silc100
description: Grunde til uopfyldt behov for læge og tandlæge efter spørgsmål, svarmulighed, enhed og tid
measure: indhold (unit -)
columns:
- sporg: values [PH050=Grund til uopfyldt lægebehov, PH070=Grund til uopfyldt tandlægebehov]
- svar: values [GR1=Havde ikke råd, GR2=Ventelisten var for lang, GR5=Bange for behandlingen/undersøgelsen, GR6=Ventede for at se, om ikke problemet gik over, GR7=Andre grunde, GR8=Havde ikke noget uopfyldt behov]
- enhed: values [AND=Procent af befolkningen, 16+ år, ANT=Antal personer, 16+ år (1.000 personer), STD=Standardfejl (pct.)]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- sporg selects the type of healthcare: PH050=læge (doctor), PH070=tandlæge (dentist). Always filter to one sporg — combining them would mix two different surveys.
- svar (GR1–GR8) represent reasons for unmet need. GR8="Ingen uopfyldt behov" (88%+ of population) dominates — to get % with unmet need for a specific reason, filter svar to GR1–GR7. Reasons are survey-level categories and should sum to ~100% (each respondent gives one primary reason, or GR8 if no unmet need).
- enhed: AND=Procent af befolkningen (16+), ANT=Antal (1.000), STD. Always filter enhed.
- No bagopl breakdown — this table only has sporg, svar, enhed, tid. It gives the national picture only.
- For % unable to see a dentist due to cost: WHERE sporg='PH070' AND svar='GR1' AND enhed='AND'.
