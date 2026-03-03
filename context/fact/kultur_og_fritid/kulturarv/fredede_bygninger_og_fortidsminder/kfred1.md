table: fact.kfred1
description: Fredede bygninger efter område, bygningstype, opførelsesår og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- bygtyp: values [0=Ejendomme i alt, 110=Stuehuse, 120=Parcelhuse, 130=Række-, kæde- og dobbelthuse, 140=Etageboligbebyggelse ... 540=Kolonihavehuse, 590=Andre fritidsformål, 910=Garager, 920=Carporte, 930=Udhuse]
- opforelsesar: values [0=Alle opførelsesår, 1150=1150-1199, 1200=1200-1249, 1250=1250-1299, 1300=1300-1349, 1350=1350-1399, 1400=1400-1449, 1450=1450-1499, 1500=1500-1549, 1550=1550-1599, 1600=1600-1649, 1650=1650-1699, 1700=1700-1749, 1750=1750-1799, 1800=1800-1849, 1850=1850-1899, 1900=1900-1949, 1950=1950-1999, 2000=2000-, 0=Uoplyst]
- tid: date range 2012-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau=1 only (5 regioner: 81–85). Code 0 = landstal (national total) — not in dim, use WHERE f.omrade='0' to get the national figure without joining.
- bygtyp='0' means "Ejendomme i alt" (all building types), opforelsesar='0' means "Alle opførelsesår". Both must be filtered to avoid overcounting. To get simple regional totals: WHERE bygtyp='0' AND opforelsesar='0'.
- opforelsesar codes are 50-year bands (e.g. '1850' = 1850–1899). Code '0' also appears separately meaning "Uoplyst" per the values list, but in the data '0' serves as the all-years total — confirm with the actual value distribution before filtering by era.
- Sample: total protected buildings per region in 2024: SELECT d.titel, f.indhold FROM fact.kfred1 f JOIN dim.nuts d ON f.omrade=d.kode WHERE f.bygtyp='0' AND f.opforelsesar='0' AND f.tid='2024-01-01'
- Map: /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.