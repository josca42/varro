table: fact.uheldk1
description: Tilskadekomne og dræbte i færdselsuheld efter område, personskade, indblandede transportmidler, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- uheld: values [0=Personskade i alt, 1=Dræbte, 2=Alvorligt tilskadekomne, 3=Lettere tilskadekomne]
- indbland: values [11=Almindelig personbil, 12=Taxi, 13=Køretøj 0-3.500 kg under udrykning, 21=Varebil 0-3.500 kg., 31=Lastbil over 3.500 kg., 33=Bus, 41=Motorcykel, 45=Knallert 45, 50=Knallert, 61=Cykel, 71=Fodgænger, 99=Andre]
- alder: values [9917=0-17 år, 1824=18-24 år, 2544=25-44 år, 4564=45-64 år, 6599=65 år og derover, 9999=Uoplyst alder]
- kon: values [1=Mænd, 2=Kvinder, 9=Uoplyst køn]
- tid: date range 1998-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts on omrade=kode. The fact table has niveau 1 (5 regioner) and niveau 3 (98 kommuner) — filter d.niveau to pick one level.
- omrade='0' means Hele landet (national total) and is NOT in dim.nuts. Use ColumnValues("uheldk1", "omrade") to see id=0 listed as "Hele landet".
- uheld=0 (Personskade i alt) is an aggregate — always filter.
- alder, kon, and indbland have no total codes; all values are specific.
- kon: values are 1, 2, 9 — NO 0=I alt total. Sum all three (or just 1+2) to get total.
- indbland describes the involved vehicle type. 11 specific types, no "I alt". Sum all to get total injured by any vehicle type.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
- alder codes here are 4-digit without leading zeros in both ColumnValues and DB (9917, 1824, etc.) — no mismatch.
