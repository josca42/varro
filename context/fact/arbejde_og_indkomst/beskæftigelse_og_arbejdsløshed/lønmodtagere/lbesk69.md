table: fact.lbesk69
description: Lønmodtagere efter enhed, bopælskommune, køn og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- bopkom: values [0=Hele landet, 84=Region Hovedstaden, 1=Landsdel Byen København, 101=København, 147=Frederiksberg ... 840=Rebild, 787=Thisted, 820=Vesthimmerlands, 851=Aalborg, 950=Uden for Danmark]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder, UDK=Uoplyst køn, uden bopæl i Danmark]
- tid: date range 2008-01-01 to 2025-04-01
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- bopkom contains ALL geographic levels in one column: 0=Hele landet, 81–85=regioner, 1–11=landsdele, 101–999=kommuner (100 kommuner), 950=Uden for Danmark. ALWAYS filter to one level to avoid summing across the hierarchy.
- For kommune-level analysis: WHERE bopkom::int >= 100 AND bopkom::int < 950. For regional: WHERE bopkom::int BETWEEN 81 AND 85. For landsdele: WHERE bopkom::int BETWEEN 1 AND 11. bopkom values match dim.nuts kode — can join for gemeente names: JOIN dim.nuts d ON f.bopkom::int = d.kode.
- Only table in this subject with kommune (municipality) level granularity. Use ColumnValues("lbesk69", "bopkom") to browse all 117 geographic codes.
- Map: /geo/kommuner.parquet (bopkom 100–949) or /geo/landsdele.parquet (bopkom 1–11) or /geo/regioner.parquet (bopkom 81–85) — merge on bopkom::int=dim_kode. Exclude 0, 950.
