table: fact.kmsta005
description: Befolkningen 1. januar (15 år+) efter sogn, socioøkonomisk status, folkekirkemedlemsskab og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- socio: join dim.socio on socio=kode; levels [1]
- fkmed: values [F=Medlem af Folkekirken, U=Ikke medlem af Folkekirken]
- tid: date range 2016-01-01 to 2024-01-01
dim docs: /dim/socio.md

notes:
- Covers only population aged 15+. Sum of all socio values does NOT equal total population of a sogns — children (under 15) are excluded.
- socio joins dim.socio cleanly (100% match, 4 codes at niveau 1): 1=Erhvervsaktive, 2=Midlertidigt ikke erhvervsaktive, 3=Ikke erhvervsaktive, 4=Andre og børn. JOIN dim.socio d ON f.socio=d.kode.
- These 4 socio codes are exhaustive within the 15+ population — sum all for 15+ total.
- fkmed: F=Medlem, U=Ikke-Medlem. Both rows present for each combination.
- Available 2016–2024 only (shorter range than most other km-tables).
- Map: context/geo/sogne.parquet — merge on sogns=dim_kode. Exclude sogns IN (0, 9999).
