table: fact.scene05a
description: Danske teatre efter teaterkategori, teatrets primære publikum og tid
measure: indhold (unit Antal)
columns:
- teattyp: values [100=Teatre i alt, 105=Alle statsstøttede teatre og statsligt godkendte, 115=Det Kgl. Teater, 120=Teatre i Det Københavnske Teatersamarbejde, 122=Landsdelscener, nationale turnéteatre mv., 130=Små storbyteatre, 135=Egnsteatre, 140=Teatre støttet af Statens Kunstfond, 142=Refusions- og formidlingsordningen, 144=Øvrige scenekunstproducenter]
- teater: values [100=Teatre i alt, 260=Børneteatre, 265=Ungdomsteatre, 255=Voksenteatre, 270=Blandet]
- tid: date range 2020/2021 to 2023/2024

notes:
- This table counts the number of theatres (antal teatre), not productions or audience.
- teattyp and teater both have 100=i alt (aggregate). They are separate dimensions: teattyp is the funding/support category; teater is the primary audience type of the theatre (børn/unge/voksne/blandet).
- teattyp is hierarchical: 100=alle teatre, 105=alle statsstøttede (aggregate of 115–144). Filter to a single teattyp code.
- teater: 100=Teatre i alt is the aggregate of 260,265,255,270. Filter to one.
- Simple table: to count all theatres in a category, filter teattyp to the desired category and teater=100.