table: fact.lbesk68
description: Lønmodtagere efter enhed, bopælslandsdel, branche (DB07 19-grp), køn, alder og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- boplandk: values [0=Hele landet, 84=Region Hovedstaden, 1=Landsdel Byen København, 2=Landsdel Københavns omegn, 3=Landsdel Nordsjælland, 4=Landsdel Bornholm, 85=Region Sjælland, 5=Landsdel Østsjælland, 6=Landsdel Vest- og Sydsjælland, 83=Region Syddanmark, 7=Landsdel Fyn, 8=Landsdel Sydjylland, 82=Region Midtjylland, 9=Landsdel Østjylland, 10=Landsdel Vestjylland, 81=Region Nordjylland, 11=Landsdel Nordjylland, 950=Uden for Danmark]
- branchedb0738: join dim.db on branchedb0738=kode::text
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder, UDK=Uoplyst køn, uden bopæl i Danmark]
- alder: values [TOT=Alder i alt, U15=Under 15 år, 1524=15-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover, UDK=Uoplyst alder, uden bopæl i Danmark]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/db.md
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- boplandk is inline (no dim join). Contains regioner (81–85) and landsdele (1–11) plus 0=Hele landet, 950=Uden for Danmark — filter by range.
- WARNING: dim.db join for branchedb0738 is broken (0% match). branchedb0738 uses letter codes only (A–S, X, TOT) — NOT in dim.db. Treat as inline. Use ColumnValues("lbesk68", "branchedb0738") for labels.
- alder uses 10-year bands (1524, 2534, 3544, 4554, 5564, 6574, 75OV). TOT=sum of all ages.
- Data ends 2025-01. Very detailed cross (region × branch × gender × age) — useful for regional occupational structure analysis.
- Map: /geo/regioner.parquet (codes 81–85) or /geo/landsdele.parquet (codes 1–11) — merge on boplandk::int=dim_kode. Exclude 0, 950.
