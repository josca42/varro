table: fact.km5
description: Befolkningen 1. januar efter sogn, køn, alder, folkekirkemedlemsskab og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år ... 80-84=80-84 år, 85-89=85-89 år, 90-94=90-94 år, 95-99=95-99 år, 100OV=100 år og derover]
- fkmed: values [F=Medlem af Folkekirken, U=Ikke medlem af Folkekirken]
- tid: date range 2007-01-01 to 2025-01-01

notes:
- Annual snapshot (1. januar). 4 dimension columns (sogns, kon, alder, fkmed) — to get one number per sogns, sum or filter all non-target dimensions explicitly.
- alder uses 5-year bands stored as strings like '[0,5)', '[5,10)', ..., '[95,100)', '[100,)' — 21 bands total, no IALT total row. Sum across all alder values to get total by sogns. Use CASE expressions for custom age groupings.
- kon: 1=Mænd, 2=Kvinder. No TOT row — sum both for combined total.
- fkmed: F=Medlem, U=Ikke-Medlem. Both rows present for each combination — filter to one or sum both explicitly.
- 2292 distinct sogns including 0='Uden placerbar adresse' and 9999='Uden fast bopæl'. Exclude for geographic analysis.
- Map: /geo/sogne.parquet — merge on sogns=dim_kode. Exclude sogns IN (0, 9999).
