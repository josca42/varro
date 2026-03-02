table: fact.laby30
description: Beskæftigede lønmodtagere i offentlig forvaltning og service (ultimo november) efter kommunegruppe, branche (DB07), sektor, alder og tid
measure: indhold (unit Antal)
columns:
- komgrp: values [0=Hele landet, 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner, 950=Uden for Danmark]
- branche07: join dim.db on branche07=kode
- sektor: values [1015=Stat, 1020=Regioner, 1025=Kommuner, 1030=Sociale kasser og fonde]
- alder: values [TOT=Alder i alt, 029=29 år og derunder, 3044=30-44 år, 4559=45-59 år, 6099=60 år og derover, 9999=Uoplyst alder]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- branche07 covers only public sector branches: 84001=Offentlig administration, 84002=Forsvar/politi mv., 85001=Grundskoler, 85002=Gymnasier og erhvervsfaglige skoler, 85003=Videregående uddannelsesinstitutioner, 85004=Voksenundervisning mv., 86001=Hospitaler, 86002=Læger/tandlæger mv., 87000=Plejehjem mv., 88000=Daginstitutioner og dagcentre mv., 999=Øvrige brancher. Does NOT join dim.db. Use ColumnValues("laby30", "branche07").
- sektor covers only the public sector: 1015=Stat, 1020=Regioner, 1025=Kommuner, 1030=Sociale kasser og fonde. No total sector code.
- komgrp: 0=Hele landet, 1-5=municipality groups, 950=Uden for Danmark.
- alder has TOT plus 4 coarse groups (029, 3044, 4559, 6099) plus 9999=Uoplyst.
