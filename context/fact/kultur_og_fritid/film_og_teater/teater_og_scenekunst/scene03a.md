table: fact.scene03a
description: Opførelser på danske teatre efter teaterkategori, publikumsgruppe, scene, genre og tid
measure: indhold (unit Antal)
columns:
- teattyp: values [100=Teatre i alt, 105=Alle statsstøttede teatre og statsligt godkendte, 115=Det Kgl. Teater, 120=Teatre i Det Københavnske Teatersamarbejde, 122=Landsdelscener, nationale turnéteatre mv., 130=Små storbyteatre, 135=Egnsteatre, 140=Teatre støttet af Statens Kunstfond, 142=Refusions- og formidlingsordningen, 144=Øvrige scenekunstproducenter]
- pubgrup: values [216=Publikumsgrupper i alt, 410=Voksne (25 år og derover), 415=Unge (16-24 år), 420=Børn (0-15 år) og familier]
- scene: values [102=Opførelser i alt, 195=Stationært på egen scene, 200=Turné i Danmark]
- genre: values [160=Genrer i alt, 165=Skuespil, 320=Musical og Operette, 325=Opera, 330=Musikteater og Teaterkoncert, 335=Dans, 340=Ballet, 345=Animation og Dukketeater, 350=Performance, 355=Nycirkus, 360=Show, Revy, Stand-up og Cabaret, 365=Anden genre]
- tid: date range 2020/2021 to 2023/2024

notes:
- scene: 102=Opførelser i alt is the aggregate of 195 (stationær, egen scene) + 200 (turné i Danmark). Filter to one value.
- pubgrup: 216=Publikumsgrupper i alt is the aggregate; 410,415,420 are non-overlapping subcategories. Filter to one.
- teattyp is hierarchical: 100=alle teatre, 105=alle statsstøttede (aggregate of 115–144). Filter to a single code.
- genre: 160=Genrer i alt is the aggregate. Never mix with specific genre codes in a sum.
- This table counts performances (opførelser), not productions or audience. For produktioner use scene02a, for tilskuere use scene04a.