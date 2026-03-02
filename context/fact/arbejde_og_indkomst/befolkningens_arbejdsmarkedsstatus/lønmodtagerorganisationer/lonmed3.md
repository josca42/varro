table: fact.lonmed3
description: Lønmodtagerorganisationernes medlemstal pr. 31.12 (Enkelte organisationer) efter medlemsorganisationer, køn og tid
measure: indhold (unit Antal)
columns:
- medorg: values [0.0=Medlemmer i alt, 0.0=2B - Bedst og Billigst - Det Faglige Hus (2009 - ), 5.0=Arkitektforbundet, 10.0=ASE Lønmodtagere (2011 -), 15.0=Kultur og Information - KI (Tidl. Bibliotekarforbundet) ( -2022) ... 545.0=Teknisk Landsforbund, 550.0=Trafikforbundet, 555.0=Uddannelsesforbundet, 560.0=Viften - Ansatte i Folketingsansatte (-2023), 565.0=Ophørte foreninger]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- CRITICAL: medorg code '0' is used for TWO different entities — "Medlemmer i alt" (grand total) AND "2B - Bedst og Billigst - Det Faglige Hus" (individual org, from 2009). This means WHERE medorg='0' returns 2 rows per (koen, tid) from 2009 onwards. Do not use medorg='0' to get totals — use lonmed2 instead.
- Individual organizations have varying time coverage. Many only appear for part of the 2007–2024 range (e.g., some start 2009, 2011; some end before 2024 when they ceased or merged). Use MIN(tid)/MAX(tid) per org to check coverage.
- 115 distinct medorg codes covering individual unions and associations. Use ColumnValues("lonmed3", "medorg") to see the full list with names.
- Always filter koen to avoid overcounting: koen='TOT' for totals, 'M'/'K' for gender.
- To get membership for a specific union, match by name using ColumnValues("lonmed3", "medorg", fuzzy_match_str="<union name>") to find the right medorg code, then filter accordingly.
- Summing across medorg values will double-count: individual organizations roll up into the main umbrella bodies, and medorg=0 is a grand total — never sum indhold across all medorg values.