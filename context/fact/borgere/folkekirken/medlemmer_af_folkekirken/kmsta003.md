table: fact.kmsta003
description: Befolkningens udvikling efter sogn, bevægelser og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- kirkebev: values [B01A=Befolkningen ultimo forrige år, B02=Levendefødte, B03=Døde, B04=Fødselsoverskud, B05=Tilflyttede, B06=Fraflyttede, B07=Nettotilflyttede, B08AA=Indvandrede i alt, B08A=Indvandret i indeværende år, B08B=Indvandret før indeværende år, B09BA=Udvandrede i alt, B09A=Udvandret i indeværende år, B09B=Udvandret før indeværende år, B10=Nettoindvandrede, B12=Korrektioner, B11=Befolkningstilvækst, B20A=Befolkningen ultimo indeværende år]
- tid: date range 2015-01-01 to 2024-01-01

notes:
- NEVER sum across kirkebev values — they represent different measures, some of which are derived from others. Summing all would be meaningless.
- Derived (aggregate) codes: B04=B02-B03 (Fødselsoverskud), B07=B05-B06 (Nettotilflyttede), B08AA=B08A+B08B (Indvandrede i alt), B09BA=B09A+B09B (Udvandrede i alt), B10=B08AA-B09BA (Nettoindvandrede), B11=B04+B07+B10+B12 (Befolkningstilvækst). Always filter to ONE kirkebev value.
- Stock codes: B01A=population end of prior year, B20A=population end of current year. Flow codes: all others.
- No fkmed column — covers all residents regardless of church membership.
- Annual data (tid: yearly). Available 2015–2024.
- Use B11 (Befolkningstilvækst) for total population change, or B20A for end-of-year stock. Use primary flows (B02, B03, B05, B06, B08A, B09A) to avoid double-counting with aggregate codes.
- Map: /geo/sogne.parquet — merge on sogns=dim_kode. Exclude sogns IN (0, 9999).
