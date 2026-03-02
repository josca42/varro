table: fact.scene10a
description: Aktivitet på danske teatre efter teaterkategori, publikumsgruppe, type, genre og tid
measure: indhold (unit Antal)
columns:
- teattyp: values [100=Teatre i alt, 105=Alle statsstøttede teatre og statsligt godkendte, 115=Det Kgl. Teater, 120=Teatre i Det Københavnske Teatersamarbejde, 122=Landsdelscener, nationale turnéteatre mv., 130=Små storbyteatre, 135=Egnsteatre, 140=Teatre støttet af Statens Kunstfond, 142=Refusions- og formidlingsordningen, 144=Øvrige scenekunstproducenter]
- pubgrup: values [216=Publikumsgrupper i alt, 220=Børn og unge under 25 år, 225=Voksne]
- type: values [101=Produktioner i alt, 101A=Produktioner, stationært på egen scene, 101B=Produktioner, turné i Danmark, 102=Opførelser i alt, 102A=Opførelser, stationært på egen scene, 102B=Opførelser, turné i Danmark, 215=Tilskuere i alt, 217=Tilskuere, stationært på egen scene, 218=Tilskuere, Turné i Danmark]
- genre: values [160=Genrer i alt, 165=Skuespil, 170=Musikdramatik/opera, 175=Ballet og dans, 180=Nycirkus, Performance mv., 190=Øvrige genrer, 192=Uoplyst genre]
- tid: date range 2015/2016 to 2023/2024

notes:
- type is a measurement selector mixing three incomparable measures in hierarchical form: 101=Produktioner i alt (= 101A stationær + 101B turné), 102=Opørelser i alt (= 102A + 102B), 215=Tilskuere i alt (= 217 stationær + 218 turné). Always filter to a single type. Summing 101+101A+101B triples the count.
- pubgrup: 216=Publikumsgrupper i alt is the aggregate of 220=Børn og unge u.25 + 225=Voksne. Filter to one.
- teattyp is hierarchical: 100=alle teatre, 105=alle statsstøttede (aggregate of 115–144). Filter to a single code.
- genre taxonomy here is DIFFERENT from scene01a–09a. scene10a uses 6 broader groups: 165=Skuespil, 170=Musikdramatik/opera, 175=Ballet og dans, 180=Nycirkus/Performance mv., 190=Øvrige genrer, 192=Uoplyst genre. These are broader aggregates — do not mix with the 11-genre codes used in other scene tables.
- Longest series of the activity tables: from 2015/2016. Use this table for historical trend analysis.