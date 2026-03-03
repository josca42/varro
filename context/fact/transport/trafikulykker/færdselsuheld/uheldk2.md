table: fact.uheldk2
description: Tilskadekomne og dræbte i spiritusuheld efter område, personskade, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- uheld: values [0=Personskade i alt, 1=Dræbte, 2=Alvorligt tilskadekomne, 3=Lettere tilskadekomne]
- alder: values [9917=0-17 år, 1824=18-24 år, 2544=25-44 år, 4564=45-64 år, 6599=65 år og derover, 9999=Uoplyst alder]
- koen: values [1=Mænd, 2=Kvinder, 9=Uoplyst køn]
- tid: date range 1998-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- This table covers spiritusuheld ONLY (alcohol-related accidents). Do not use for general accident statistics.
- omrade joins dim.nuts on omrade=kode. The fact table has niveau 1 (5 regioner) and niveau 2 (11 landsdele) — coarser than uheldk1/uheldk7 which have kommuner (niveau 3). Filter d.niveau to avoid mixing levels.
- omrade='0' means Hele landet (national total) and is NOT in dim.nuts.
- uheld=0 (Personskade i alt) is an aggregate — always filter.
- alder and koen have no total codes; sum all values to get total.
- koen: values 1, 2, 9 — no I alt total.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.
