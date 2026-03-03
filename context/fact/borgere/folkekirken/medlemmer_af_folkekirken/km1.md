table: fact.km1
description: Befolkningen den 1. i kvartalet efter sogn, folkekirkemedlemsskab og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- fkmed: values [F=Medlem af Folkekirken, U=Ikke medlem af Folkekirken]
- tid: date range 2007-01-01 to 2025-07-01

notes:
- Simplest population snapshot by church membership. No dim joins — all columns inline.
- 2292 distinct sogns, including special codes: 0='Uden placerbar adresse', 9999='Uden fast bopæl'. Exclude these for geographic analysis: WHERE f.sogn NOT IN ('0', '9999').
- fkmed: F=Medlem, U=Ikke-Medlem. To get membership count only: WHERE fkmed='F'. To get total population by sogn, sum both values (or omit fkmed filter).
- Quarterly data — tid takes values 1 jan, 1 apr, 1 jul, 1 oct each year. For annual comparisons, filter WHERE EXTRACT(MONTH FROM tid)=1 to use January snapshots consistently.
- No age/gender breakdown here. Use km5 (by sogn) for age+gender+membership, or km6 (by kommune) for the same at municipality level.
- Map: /geo/sogne.parquet — merge on sogns=dim_kode. Exclude sogns IN (0, 9999).
