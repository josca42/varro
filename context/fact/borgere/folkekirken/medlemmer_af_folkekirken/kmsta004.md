table: fact.kmsta004
description: Befolkningens udvikling efter provsti, bevægelser og tid
measure: indhold (unit Antal)
columns:
- provsti: values [101=1-01 Københavns Vor Frue Provsti, 102=1-02 Københavns Holmens Provsti, 103=1-03 Østerbro Provsti, 104=1-04 Nørrebro Provsti, 105=1-05 Vesterbro Provsti ... 1004=10-04 Fredericia Provsti, 1005=10-05 Kolding Provsti, 1006=10-06 Vejle Provsti, 1007=10-07 Hedensted Provsti, 9999=99-99 Uoplyst provsti]
- kirkebev: values [B01A=Befolkningen ultimo forrige år, B02=Levendefødte, B03=Døde, B04=Fødselsoverskud, B05=Tilflyttede, B06=Fraflyttede, B07=Nettotilflyttede, B08AA=Indvandrede i alt, B08A=Indvandret i indeværende år, B08B=Indvandret før indeværende år, B09BA=Udvandrede i alt, B09A=Udvandret i indeværende år, B09B=Udvandret før indeværende år, B10=Nettoindvandrede, B12=Korrektioner, B11=Befolkningstilvækst, B20A=Befolkningen ultimo indeværende år]
- tid: date range 2015-01-01 to 2024-01-01

notes:
- Provsti-level equivalent of kmsta003. Same kirkebev structure and caveats apply.
- NEVER sum across kirkebev values. Always filter to ONE. Derived codes: B04=B02-B03, B07=B05-B06, B08AA=B08A+B08B, B09BA=B09A+B09B, B10=B08AA-B09BA, B11=total growth.
- Annual data. No fkmed column.
