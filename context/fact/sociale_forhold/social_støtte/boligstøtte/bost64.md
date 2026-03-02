table: fact.bost64
description: Boligstøtte efter alder, ydelsestype, måned, enhed og tid
measure: indhold (unit -)
columns:
- alder: values [TOT2=Alle aldre, 1824=18-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6064=60-64 år, 6569=65-69 år, 7074=70-74 år, 7579=75-79 år, 8089=80-89 år, 9000=90 år og derover]
- ydelsestype: values [1000=Alle typer boligstøtte, 1010=Boligsikring, alle boligformer, 1020=Boligsikring, almindelig lejer, 1030=Boligsikring, andelshaver, 1040=Boligsikring, ejer, 1050=Boligsikring, særlig boligform, 1060=Førtidpensionister, alle boligformer, 1070=Førtidpensionister, almindelig lejer, 1080=Førtidpensionister, andelshaver, 1090=Førtidpensionister, ejer, 1100=Førtidpensionister, særlig boligform, 1110=Førtidpensionister, ældrebolig, 1120=Boligydelse, alle boligformer, 1130=Boligydelse, almindelig lejer, 1140=Boligydelse, andelshaver, 1150=Boligydelse, ejer, 1160=Boligydelse, særlig boligform, 1170=Boligydelse, ældrebolig]
- mnd: values [1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December]
- enhed: values [3000=Antal husstande, 3010=Gennemsnitlig af udbetalt beløb (kr), 3020=Nedre kvartil af udbetalt beløb (kr), 3030=Median af udbetalt beløb (kr), 3040=Øvre kvartil af beløb (kr)]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- enhed is a measurement selector: 3000=Antal husstande, 3010=Gennemsnitlig udbetalt beløb (kr), 3020=Nedre kvartil (kr), 3030=Median (kr), 3040=Øvre kvartil (kr). Every dimension combination appears 5 times — always filter to one enhed.
- ydelsestype is hierarchical — same structure as bost63. 1000 = 1010 + 1060 + 1120. Never sum all ydelsestype codes; use 1000 for a grand total.
- alder: 14 five-year age groups (1824 through 9000) plus TOT2 (alle aldre). TOT2 is slightly larger than the sum of age groups (difference ~200 for 2024-01 national level), likely due to a small "uoplyst alder" category not exposed as a separate code. Use TOT2 for totals rather than summing the groups.
- Age groups start at 18 (boligstøtte requires adult household head). There is no under-18 category.
- mnd is the month (1–12). Filter to one month for point-in-time analysis; do not sum.
- To get the age distribution of housing-support recipients: filter ydelsestype='1000', enhed='3000', a specific mnd and tid, and exclude TOT2 from the result set (keep it for reference/cross-check).