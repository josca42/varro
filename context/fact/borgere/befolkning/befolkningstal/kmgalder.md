table: fact.kmgalder
description: Gennemsnitsalder efter sogn, køn og tid
measure: indhold (unit Gns.)
columns:
- sogn: values [0=Hele landet, 7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2025-01-01

notes:
- indhold is a mean (average age), not a count. Do NOT sum across sogne — use AVG() weighted by parish population if aggregating.
- kon has TOT, M, K — filter to kon='TOT' for overall average age per parish.
- sogn=0 is "Hele landet" (national average). 9999=Uden fast bopæl is a non-geographic code.
- Finest geographic granularity for average age (parish level, back to 2007). For commune/region level use galder.
- Map: context/geo/sogne.parquet — merge on sogn=dim_kode. Exclude sogn IN (0, 9999).