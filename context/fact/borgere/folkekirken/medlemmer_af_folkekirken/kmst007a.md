table: fact.kmst007a
description: Befolkningen 1. oktober (15 år+) efter sogn, folkekirkemedlemsskab, højest fuldførte uddannelse og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- fkmed: values [F=Medlem af Folkekirken, U=Ikke medlem af Folkekirken]
- uddannelsef: values [H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H35=H35 Adgangsgivende uddannelsesforløb, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser, H90=H90 Uoplyst mv.]
- tid: date range 2015-01-01 to 2024-01-01

notes:
- Reference date is 1. oktober (not 1. januar like most other tables in this subject). tid values are stored as yyyy-01-01 but represent October of the prior year (e.g. tid='2015-01-01' = 1. oktober 2015). Verify before mixing with January-referenced tables.
- Covers only population aged 15+. uddannelsef (highest completed education) has 9 inline codes — H10 to H90, mutually exclusive, exhaustive within 15+ population. Sum all for 15+ total.
- H90='Uoplyst mv.' captures those with unknown/unregistered education — include or exclude depending on analysis intent.
- fkmed: F=Medlem, U=Ikke-Medlem. Both rows present for each combination. Filter to one or sum both.
- Available 2015–2024. For membership by education analysis, compare H70 (LVU) vs H10 (Grundskole) membership rates.
- Map: /geo/sogne.parquet — merge on sogns=dim_kode. Exclude sogns IN (0, 9999).
