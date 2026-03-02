table: fact.kv2fr6
description: Forbrug af fritidsaktiviteter efter aktivitet, hyppighed, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- aktivitet: values [43320=Håndarbejde eller andre kreative ting, 43330=Arbejdet i eller på hus, lejlighed eller sommerhus eller lavet havearbejde, 43340=Arbejdet med mekanik eller teknik, 43350=Gået på jagt eller fisket, 43360=Spillet spil, ekskl. digitale spil]
- hyp: values [110100=1 eller flere gange om dagen, 110300=4-6 gange om ugen, 110400=1-3 gange om ugen, 110500=1-3 gange om måneden, 110600=1-2 gange inden for 3 måneder, 110900=Sjældnere end 1-2 gange inden for 3 måneder, 111000=Det har jeg ikke gjort inden for de seneste 12 måneder, 111100=Ønsker ikke at svare, 111200=Ved ikke]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- Cross-tabulation of 5 hobby/leisure activity types (aktivitet) × frequency (hyp) × kon × alder. For each aktivitet+kon+alder combination, hyp values are mutually exclusive and sum to ~100%.
- To get "% who do activity X at all": sum hyp 110100 through 110900 (exclude 111000=not done, 111100, 111200).
- Activities (håndarbejde, husarbejde, mekanik, jagt/fiskeri, brætspil) are independent — a person can do multiple. Do not sum across aktivitet.
- Single 2024 annual observation.
