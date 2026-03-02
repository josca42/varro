table: fact.sogn1
description: Befolkningen 1. januar efter sogn, køn, alder og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- tid: date range 2010-01-01 to 2025-01-01

notes:
- No total rows for kon (only 1=Mænd, 2=Kvinder) or alder (individual years 0–125). Sum both kon values and/or desired age range for totals.
- 0=Uden placerbar adresse and 9999=Uden fast bopæl are non-geographic — exclude for geographic analysis.
- Finest geographic level for age/sex population breakdown. Use ColumnValues("sogn1", "sogn") to search for specific parishes by name.
- Annual data only (back to 2010). For quarterly parish data (without age/sex) use km1.
- Map: context/geo/sogne.parquet — merge on sogn=dim_kode. Exclude sogn IN (0, 9999).