table: fact.scene07a
description: Danske teatres turne i udlandet efter teaterkategori, aktivitet, genre, land og tid
measure: indhold (unit Antal)
columns:
- teattyp: values [100=Teatre i alt, 105=Alle statsstøttede teatre og statsligt godkendte, 115=Det Kgl. Teater, 120=Teatre i Det Københavnske Teatersamarbejde, 122=Landsdelscener, nationale turnéteatre mv., 130=Små storbyteatre, 135=Egnsteatre, 140=Teatre støttet af Statens Kunstfond, 142=Refusions- og formidlingsordningen, 144=Øvrige scenekunstproducenter]
- aktivitet: values [300=Produktioner, 310=Opførelser]
- genre: values [160=Genrer i alt, 165=Skuespil, 320=Musical og Operette, 325=Opera, 330=Musikteater og Teaterkoncert, 335=Dans, 340=Ballet, 345=Animation og Dukketeater, 350=Performance, 355=Nycirkus, 360=Show, Revy, Stand-up og Cabaret, 365=Anden genre]
- land: values [5145=Finland, 5120=Sverige, 5130=Frankrig, 5150=Italien, 5164=Spanien, 5315=Storbritannien, 5355=Tyskland, 5260=Norge, 5997=Europa udenfor Finland, Sverige, Frankrig, Italien, Spanien, Storbritannien, Tyskland og Norge, 5314=Canada, 5390=USA, 5471=Asien, 5502=Australien og New Zealand, 5999=Verden udenfor Europa, Canada, USA, Asien, Australien og New Zealand]
- tid: date range 2020/2021 to 2023/2024

notes:
- aktivitet has two distinct, incomparable measures: 300=Produktioner and 310=Opførelser. Always filter to one.
- land: same 14-code geographic scheme as scene06a's nation2 (8 specific countries + 2 rest-of-region + Asien, Australien/NZ, Canada, USA). No "world total" aggregate code; sum all land codes to get a total.
- teattyp is hierarchical: 100=alle teatre, 105=alle statsstøttede (aggregate of 115–144). Filter to a single code.
- genre: 160=Genrer i alt is the aggregate. Never mix with specific genre codes in a sum.
- No audience (tilskuere) count in this table — only produktioner and opørelser for Danish tours abroad. For foreign tours in Denmark with audience, use scene06a.