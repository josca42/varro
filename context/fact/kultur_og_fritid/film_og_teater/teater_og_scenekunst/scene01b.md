table: fact.scene01b
description: Tilskuere på danske teatre (egen scene) efter teaterkategori, aktivitet, genre og tid
measure: indhold (unit Antal)
columns:
- teattyp: values [100=Teatre i alt, 105=Alle statsstøttede teatre og statsligt godkendte, 115=Det Kgl. Teater, 120=Teatre i Det Københavnske Teatersamarbejde, 122=Landsdelscener, nationale turnéteatre mv., 130=Små storbyteatre, 135=Egnsteatre, 140=Teatre støttet af Statens Kunstfond, 142=Refusions- og formidlingsordningen, 144=Øvrige scenekunstproducenter]
- aktivitet: values [103=Tilskuere i alt, 375=Solgte billetter under rabatordning til voksne, egen scene, 380=Solgte billetter under rabatordning til børn og unge u. 25 år, egen scene, 385=Fribilletter, inkl. inviterede (gratisbilletter), 390=Løssalg]
- genre: values [160=Genrer i alt, 165=Skuespil, 320=Musical og Operette, 325=Opera, 330=Musikteater og Teaterkoncert, 335=Dans, 340=Ballet, 345=Animation og Dukketeater, 350=Performance, 355=Nycirkus, 360=Show, Revy, Stand-up og Cabaret, 365=Anden genre]
- tid: date range 2020/2021 to 2023/2024

notes:
- aktivitet: 103=Tilskuere i alt is the total; 375,380,385,390 are ticket subcategories (rabat voksne, rabat børn/unge, fribilletter, løssalg) that sum to the total. Always filter to one aktivitet value.
- teattyp is hierarchical: 100=alle teatre, 105=alle statsstøttede (aggregate of 115–144). Filter to a single code to avoid double-counting.
- genre: 160=Genrer i alt is the aggregate. Never mix with specific genre codes in a sum.
- This table is scoped to "egen scene" only. For audience split by stationær vs. turné i Danmark, use scene04a.