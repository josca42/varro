table: fact.aed08
description: Genoptræning/vedligeholdelsestræning, personer efter område, ydelsestype, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- ydelsestype: values [100=I alt, 200=Genoptræning, 300=Vedligeholdelsestræning, 400=Genoptræning og vedligeholdelsestræning]
- alder: values [50=Alder i alt, 100=Under 65 år, 200=65-66 år, 300=67-69 år, 850=67 år og derover, 400=70-74 år, 500=75-79 år, 600=80-84 år, 700=85-89 år, 800=90 år og derover]
- koen: values [100=Mænd og kvinder i alt, 200=Mænd, 300=Kvinder]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts niveau 3 only (98 kommuner, no regional breakdown). omrade=0 is national total (not in dim).
- ydelsestype overlaps: 100=i alt; 200=all genoptræning recipients (including those who also get vedligeholdelse); 300=all vedligeholdelsestræning recipients (including those in both); 400=persons receiving both. So 200+300 = 100+400 (double-counts those in both). Never sum 200+300. Use 100 for the total, and 400 to identify dual recipients.
- alder=50 is total; alder=850 is 67+ sub-total — do not mix with individual bands. koen=100 is total.
- Compare with rehab19 for rehabilitering (a separate intervention from genoptræning/vedligeholdelse).
- Map: /geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
