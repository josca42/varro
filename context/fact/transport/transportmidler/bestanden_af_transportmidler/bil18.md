table: fact.bil18
description: Bestanden af lastbiler efter drivmiddel, antal aksler, totalvægt og tid
measure: indhold (unit Antal)
columns:
- driv: values [20200=Drivmidler i alt, 20205=Benzin, 20210=Diesel, 20256=Metanol, 20258=Ætanol, 20235=Øvrige drivmidler]
- aksler: values [9050=Antal aksler i alt, 9052=2 aksler, 9054=3 aksler eller flere]
- tvaegt: values [0=Totalvægt i alt, 165=3.501-4.000 kg, 170=4.001-5.000 kg, 180=5.001-6.000 kg, 185=6.001-7.000 kg ... 355=39.001-40.000 kg, 360=40.001-41.000 kg, 365=41.001-42.000 kg, 370=Over 42.000 kg, 375=Uoplyst]
- tid: date range 1993-01-01 to 2025-01-01