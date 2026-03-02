table: fact.kmsta009
description: Befolkningen 1. januar (15 år+) efter sogn, folkekirkemedlemsskab, pendling og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- fkmed: values [F=Medlem af Folkekirken, U=Ikke medlem af Folkekirken]
- pendling: values [10=Natbefolkning, 20=Indpendling, 30=Udpendling, 40=Dagbefolkning]
- tid: date range 2016-01-01 to 2024-01-01

notes:
- pendling is a MEASUREMENT SELECTOR — the 4 values are alternative views of the same population, not additive categories. NEVER sum across all pendling values.
- 10=Natbefolkning (residents at night = ordinary resident count), 20=Indpendling (workers commuting IN to this sogns), 30=Udpendling (residents commuting OUT), 40=Dagbefolkning (workers present during day). Nationally: Natbefolkning total = Dagbefolkning total; Indpendling total = Udpendling total. Differences appear at geographic level.
- For standard "how many members live in this sogns" question: filter pendling='10' (Natbefolkning).
- Covers only population aged 15+. Available 2016–2024.
- fkmed: F=Medlem, U=Ikke-Medlem. Both rows present for each combination.
- Map: context/geo/sogne.parquet — merge on sogns=dim_kode. Exclude sogns IN (0, 9999).
