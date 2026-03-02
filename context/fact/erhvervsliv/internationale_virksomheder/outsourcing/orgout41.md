table: fact.orgout41
description: Firmaers motiver for international outsourcing efter branche (DB07 10-grp.), motiver, betydning og tid
measure: indhold (unit Pct.)
columns:
- branche0710: values [TOT=TOT Erhverv i alt, 2=2 Industri, råstofindvinding og forsyningsvirksomhed, 3=3 Bygge og anlæg, 4=4 Handel og transport mv., 5=5 Information og kommunikation, 6=6 Finansiering og forsikring, 7=7 Ejendomshandel og udlejning, 8=8 Erhvervsservice]
- motiv: values [REDLC=Lavere lønomkostninger, REDOC=Lavere omkostninger (udover lønomkostninger), ACCESS=Adgang til nye markeder, ISLACK=Mangel på kvalificeret arbejdskraft, KNOW=Adgang til specialiseret viden og teknologi, QUAL=Forbedret kvalitet eller introduktion af nye produkter, CORE=Fokus på virksomhedens kerneaktivitet, REDDEL=Kortere leveringstid, REG=Mindre lovgivning/regulering, ISSTRAT=Strategisk beslutning taget af moderselskabet]
- betyd: values [VERYIMP=Meget vigtig, IMP=Vigtig, NOTIMP=Ikke vigtig, NA=Ikke relevant]
- tid: date range 2009 to 2024

notes:
- tid is int4range (survey waves). Filter with: WHERE tid = '[2021,2024)'::int4range
- indhold is Pct. — for each motiv+branche+tid combination, betyd distributes 100% across importance levels. To get "% rating X as very important", filter WHERE betyd='VERYIMP'. Never sum across betyd (would yield ~300% due to rounding).
- betyd: the NA (Ikke relevant) category is stored as an empty string '' in the database, not as 'NA'. Filter with: WHERE betyd = '' to isolate non-respondents.
- motiv: 10 independent outsourcing motives — each firm rates all 10 separately. Do not sum across motiv values.
- branche0710: sectors 2–8 sum to TOT. Filter to TOT for national total, or exclude TOT when grouping by sector.