table: fact.kmsta003
description: Befolkningens udvikling efter sogn, bevægelser og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- kirkebev: values [B01A=Befolkningen ultimo forrige år, B02=Levendefødte, B03=Døde, B04=Fødselsoverskud, B05=Tilflyttede, B06=Fraflyttede, B07=Nettotilflyttede, B08AA=Indvandrede i alt, B08A=Indvandret i indeværende år, B08B=Indvandret før indeværende år, B09BA=Udvandrede i alt, B09A=Udvandret i indeværende år, B09B=Udvandret før indeværende år, B10=Nettoindvandrede, B12=Korrektioner, B11=Befolkningstilvækst, B20A=Befolkningen ultimo indeværende år]
- tid: date range 2015-01-01 to 2024-01-01

notes:
- kirkebev codes are the same B-code scheme as bev107/bev22: some codes are derived from others (B04=B02-B03, B11=B04+B07+B10+B12, B08AA includes B08A+B08B, B09BA includes B09A+B09B). Never sum all kirkebev — pick the specific component or use aggregate codes.
- B01A=population start of year, B20A=population end of year; the difference equals B11 (Befolkningstilvækst).
- 0=Uden placerbar adresse and 9999=Uden fast bopæl are non-geographic catch-alls.
- Shortest time range of all movement tables (2015–2024). Parish-level movement data — for commune/region level use bev107 (annual) or bev22 (quarterly).
- Map: context/geo/sogne.parquet — merge on sogn=dim_kode. Exclude sogn IN (0, 9999).