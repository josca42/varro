table: fact.scene09a
description: Danske teatres turne i Danmark efter område, teaterkategori, aktivitet, genre og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2]
- teattyp: values [100=Teatre i alt, 105=Alle statsstøttede teatre og statsligt godkendte, 115=Det Kgl. Teater, 120=Teatre i Det Københavnske Teatersamarbejde, 122=Landsdelscener, nationale turnéteatre mv., 130=Små storbyteatre, 135=Egnsteatre, 140=Teatre støttet af Statens Kunstfond, 142=Refusions- og formidlingsordningen, 144=Øvrige scenekunstproducenter]
- aktivitet: values [300=Produktioner]
- genre: values [160=Genrer i alt, 165=Skuespil, 320=Musical og Operette, 325=Opera, 330=Musikteater og Teaterkoncert, 335=Dans, 340=Ballet, 345=Animation og Dukketeater, 350=Performance, 355=Nycirkus, 360=Show, Revy, Stand-up og Cabaret, 365=Anden genre]
- tid: date range 2020/2021 to 2023/2024
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau=2 only (11 landsdele). Code 0 = Danmark i alt (aggregate, not in dim.nuts). To get the national total use WHERE omrade='0'; to get regional breakdown join dim.nuts and exclude omrade='0'.
- ColumnValues("nuts", "titel", for_table="scene09a") returns the 11 landsdele plus the unmatched aggregate code 0.
- aktivitet only has 300=Produktioner — no opørelser or tilskuere. This is the only table with regional breakdown of turné productions.
- teattyp is hierarchical: 100=alle teatre, 105=alle statsstøttede (aggregate of 115–144). Filter to a single code.
- genre: 160=Genrer i alt is the aggregate. Never mix with specific genre codes in a sum.
- Map: /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.