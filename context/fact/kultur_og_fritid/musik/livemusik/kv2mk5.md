table: fact.kv2mk5
description: Forbrug af koncerter efter hovedgenre, hyppighed, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- hovedgenre: values [42100=Klassisk koncert eller musikfestival, 42110=Rytmisk koncert eller musikfestival]
- hyp: values [110200=1 eller flere gange om ugen, 110500=1-3 gange om måneden, 110600=1-2 gange inden for 3 måneder, 110700=2-3 gange inden for de seneste 12 måneder, 110800=1 gang inden for de seneste 12 måneder, 111000=Det har jeg ikke gjort inden for de seneste 12 måneder, 111100=Ønsker ikke at svare, 111200=Ved ikke]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey percentages (single year 2024). Frequency categories (hyp) within each genre sum to ~100% — they are mutually exclusive (each respondent falls into one frequency bucket per genre).
- The two genres (klassisk/rytmisk) are NOT mutually exclusive — a person can attend both. Never sum indhold across hovedgenre.
- kon='10' and alder='TOT' give the overall totals. Filter these out when breaking down by gender or age.
- To ask "how often do Danes go to rhythmic concerts?": filter kon='10', alder='TOT', hovedgenre='42110', then read the hyp breakdown directly.