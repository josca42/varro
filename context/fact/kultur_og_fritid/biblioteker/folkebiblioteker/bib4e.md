table: fact.bib4e
description: Folkebibliotekernes bestand og brug af elektroniske ressourcer efter område, opgørelse, elektronisk materialetype og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- opgoer1: values [111=Bestand, 180=Visninger, 181=Søgninger (-2017)]
- matypelek: values [183=E-tidsskrifter og andre e-serier, 184=E-bøger og lydbøger, 186=E-multimedieoptagelser, 187=Databaser]
- tid: date range 2014-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (97 kommuner). omrade=0 = Hele landet.
- opgoer1 is a measurement type selector: 111=Bestand, 180=Visninger, 181=Søgninger (-2017). Always filter to one — Søgninger is historical only.
- matypelek: 4 electronic material types (e-journals, e-books, e-video, databases). 184=E-bøger og lydbøger is the largest category.
- No aggregate across matypelek — each type is an independent count.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
