table: fact.skib35
description: Krydstogtskibe på danske havne efter havn, enhed og tid
measure: indhold (unit -)
columns:
- havn: values [0=HAVNE I ALT, 25=Københavns Havn, 45=Helsingør Havn, 120=Kalundborg Havn, 315=Rønne Havn, 535=Fredericia Havn, 665=Aarhus Havn, 730=Aalborg Havn, 790=Skagen Havn, 999=Øvrige havne]
- maengde4: values [9000=Anløb af krydstogtskibe, 9005=Påstigende terminalpassagerer, 1000, 9010=Afstigende terminalpassagerer, 1000, 9015=Gennemgående passagerer, 1000]
- tid: date range 2002-01-01 to 2024-01-01

notes:
- maengde4 is a measurement selector with 4 distinct metrics in different units (ship calls as count, three passenger categories in 1.000 persons). Always filter to exactly one maengde4 value. Do not sum across maengde4.
- havn=0 (HAVNE I ALT) is the pre-computed total across all ports. Exclude when summing individual ports.
- Annual data. Cruise ships only — for regular ferry traffic see skib31–34.
