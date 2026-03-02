table: fact.scene06a
description: Udenlandske gæstespil på danske scener efter teaterkategori, aktivitet, genre, nationalitet og tid
measure: indhold (unit Antal)
columns:
- teattyp: values [100=Teatre i alt, 105=Alle statsstøttede teatre og statsligt godkendte, 115=Det Kgl. Teater, 120=Teatre i Det Københavnske Teatersamarbejde, 122=Landsdelscener, nationale turnéteatre mv., 130=Små storbyteatre, 135=Egnsteatre, 140=Teatre støttet af Statens Kunstfond, 142=Refusions- og formidlingsordningen, 144=Øvrige scenekunstproducenter]
- aktivitet: values [145=Produktioner, egne scener, 150=Opførelser, egne scener, 155=Tilskuere, egne scener]
- genre: values [160=Genrer i alt, 165=Skuespil, 320=Musical og Operette, 325=Opera, 330=Musikteater og Teaterkoncert, 335=Dans, 340=Ballet, 345=Animation og Dukketeater, 350=Performance, 355=Nycirkus, 360=Show, Revy, Stand-up og Cabaret, 365=Anden genre]
- nation2: values [5145=Finland, 5120=Sverige, 5130=Frankrig, 5150=Italien, 5164=Spanien, 5315=Storbritannien, 5355=Tyskland, 5260=Norge, 5997=Europa udenfor Finland, Sverige, Frankrig, Italien, Spanien, Storbritannien, Tyskland og Norge, 5314=Canada, 5390=USA, 5471=Asien, 5502=Australien og New Zealand, 5999=Verden udenfor Europa, Canada, USA, Asien, Australien og New Zealand]
- tid: date range 2020/2021 to 2023/2024

notes:
- aktivitet mixes three fundamentally incomparable measures in one column: 145=Produktioner (count of productions), 150=Opførelser (count of performances), 155=Tilskuere (audience count). Always filter to exactly one aktivitet.
- nation2: 14 geographic codes — 8 specific countries + 2 "rest of region" buckets (5997, 5999) + Asien, Australien og New Zealand, Canada, USA. No overall total/aggregate code; sum all to get world total.
- teattyp is hierarchical: 100=alle teatre, 105=alle statsstøttede (aggregate of 115–144). Filter to a single code.
- genre: 160=Genrer i alt is the aggregate. Never mix with specific genre codes in a sum.
- This table covers foreign guest performances in Denmark. For Danish tours abroad, use scene07a.