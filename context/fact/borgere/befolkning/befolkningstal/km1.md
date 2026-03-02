table: fact.km1
description: Befolkningen den 1. i kvartalet efter sogn, folkekirkemedlemsskab og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- fkmed: values [F=Medlem af Folkekirken, U=Ikke medlem af Folkekirken]
- tid: date range 2007-01-01 to 2025-07-01

notes:
- Quarterly population snapshot at parish (sogn) level with Church of Denmark membership. Only two fkmed values (F/U) — no total. Sum F+U to get total parish population.
- Over 2000 distinct sogns. 0=Uden placerbar adresse and 9999=Uden fast bopæl are non-geographic catch-all codes — exclude them for geographic analysis.
- No age or sex breakdown. For age/sex by parish use sogn1 (annual). km1 is the only quarterly parish-level population series.
- Useful for tracking Folkekirke membership trends over time at fine geographic level (back to Q1 2007).
- Map: context/geo/sogne.parquet — merge on sogn=dim_kode. Exclude sogn IN (0, 9999).