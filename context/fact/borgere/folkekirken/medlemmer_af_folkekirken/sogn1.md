table: fact.sogn1
description: Befolkningen 1. januar efter sogn, køn, alder og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- tid: date range 2010-01-01 to 2025-01-01

notes:
- Total population by sogns — NO fkmed column. This covers all residents regardless of church membership. Use for total population denominators when calculating membership rates.
- alder uses individual years 0–125 (no IALT total, no 5-year bands). Sum across all alder rows to get total by sogns. Use CASE WHEN alder::int BETWEEN 0 AND 4 THEN '0-4' ... for age groupings.
- kon: 1=Mænd, 2=Kvinder. No TOT row — sum both for combined total.
- Starts from 2010 (later than km5 which starts 2007). Available annually (1. januar).
- Pair with km5 to compute membership share: km5 (fkmed='F') / sogns1 total by sogns/age/gender.
- Map: context/geo/sogne.parquet — merge on sogns=dim_kode. Exclude sogns IN (0, 9999).
