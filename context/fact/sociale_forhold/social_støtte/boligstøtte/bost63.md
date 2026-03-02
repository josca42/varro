table: fact.bost63
description: Boligstøtte efter område, ydelsestype, måned, enhed og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- ydelsestype: values [1000=Alle typer boligstøtte, 1010=Boligsikring, alle boligformer, 1020=Boligsikring, almindelig lejer, 1030=Boligsikring, andelshaver, 1040=Boligsikring, ejer, 1050=Boligsikring, særlig boligform, 1060=Førtidpensionister, alle boligformer, 1070=Førtidpensionister, almindelig lejer, 1080=Førtidpensionister, andelshaver, 1090=Førtidpensionister, ejer, 1100=Førtidpensionister, særlig boligform, 1110=Førtidpensionister, ældrebolig, 1120=Boligydelse, alle boligformer, 1130=Boligydelse, almindelig lejer, 1140=Boligydelse, andelshaver, 1150=Boligydelse, ejer, 1160=Boligydelse, særlig boligform, 1170=Boligydelse, ældrebolig]
- mnd: values [1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December]
- enhed: values [3000=Antal husstande, 3010=Gennemsnitlig af udbetalt beløb (kr), 3020=Nedre kvartil af udbetalt beløb (kr), 3030=Median af udbetalt beløb (kr), 3040=Øvre kvartil af beløb (kr)]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- enhed is a measurement selector: 3000=Antal husstande, 3010=Gennemsnitlig udbetalt beløb (kr), 3020=Nedre kvartil (kr), 3030=Median (kr), 3040=Øvre kvartil (kr). Every dimension combination appears 5 times — always filter to one enhed or results will be wrong.
- ydelsestype is hierarchical. 1000 (alle typer) = 1010 (Boligsikring, alle boligformer) + 1060 (Førtidpensionister, alle boligformer) + 1120 (Boligydelse, alle boligformer). Each of those three sums its own subtypes (e.g. 1010 = 1020+1030+1040+1050). Never sum across all 18 ydelsestype codes — use 1000 for a grand total, or pick either the three mid-level aggregates or leaf codes.
- omrade joins dim.nuts at niveau 3 only (99 kommuner). Code '0' is the national aggregate (hele landet) — it is NOT in dim.nuts so the join drops it. For national totals, use omrade='0' directly without a dim join. Sum of alle kommuner equals omrade='0' value.
- mnd is the month (1–12). These are stock figures (modtagere pr. måned), not flows — do not sum across months. Filter to a specific month for point-in-time comparisons.
- To get a simple municipal count of housing-support recipients: filter ydelsestype='1000', enhed='3000', and pick a specific mnd and tid. Join omrade to dim.nuts WHERE d.niveau=3 for kommune names. Exclude omrade='0' from the join or handle it separately.
- ColumnValues("nuts", "titel", for_table="bost63") shows the 99 kommuner actually present in the table.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.