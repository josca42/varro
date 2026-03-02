table: fact.scene01a
description: Produktioner og opførelser på danske teatre (egen scene) efter teaterkategori, aktivitet, genre og tid
measure: indhold (unit Antal)
columns:
- teattyp: values [100=Teatre i alt, 105=Alle statsstøttede teatre og statsligt godkendte, 115=Det Kgl. Teater, 120=Teatre i Det Københavnske Teatersamarbejde, 122=Landsdelscener, nationale turnéteatre mv., 130=Små storbyteatre, 135=Egnsteatre, 140=Teatre støttet af Statens Kunstfond, 142=Refusions- og formidlingsordningen, 144=Øvrige scenekunstproducenter]
- aktivitet: values [145=Produktioner, egne scener, 150=Opførelser, egne scener]
- genre: values [160=Genrer i alt, 165=Skuespil, 320=Musical og Operette, 325=Opera, 330=Musikteater og Teaterkoncert, 335=Dans, 340=Ballet, 345=Animation og Dukketeater, 350=Performance, 355=Nycirkus, 360=Show, Revy, Stand-up og Cabaret, 365=Anden genre]
- tid: date range 2020/2021 to 2023/2024

notes:
- aktivitet has two distinct, incomparable measures: 145=Produktioner and 150=Opførelser. Always filter to one; never sum across both.
- teattyp is hierarchical: 100=alle teatre (total), 105=alle statsstøttede (aggregate of 115,120,122,130,135,140,142,144). Filter to a single code. Summing all teattyp values gives ~3× the true total.
- genre: 160=Genrer i alt is the aggregate. Individual genres: 165,320,...,365. Never mix aggregate with specific codes in a sum.
- Only 4 years of data (2020/2021–2023/2024). For longer series, use scene10a (from 2015/2016, but with a broader genre taxonomy).