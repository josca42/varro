table: fact.lbesk31
description: Lønmodtagere efter enhed, arbejdsstedslandsdel, branche (DB07 10-grp.) og tid
measure: indhold (unit Andel i pct.)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- arbejdslands: values [0=Hele landet, 84=Region Hovedstaden, 1=Landsdel Byen København, 2=Landsdel Københavns omegn, 3=Landsdel Nordsjælland, 4=Landsdel Bornholm, 85=Region Sjælland, 5=Landsdel Østsjælland, 6=Landsdel Vest- og Sydsjælland, 83=Region Syddanmark, 7=Landsdel Fyn, 8=Landsdel Sydjylland, 82=Region Midtjylland, 9=Landsdel Østjylland, 10=Landsdel Vestjylland, 81=Region Nordjylland, 11=Landsdel Nordjylland, 950=Uden for Danmark, 99=Uoplyst]
- branche0710: join dim.db on branche0710=kode::text; levels [2, 3]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/db.md
notes:
- IMPORTANT: measure is Andel i pct. (percentage share of national total), NOT absolute count. Values are percentages — do NOT sum across regions or branches to get totals.
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere.
- WARNING: dim.db join is incorrect. branche0710 uses numeric codes 1–11 (10-gruppe) — use dim.db_10 instead. Join: JOIN dim.db_10 d ON f.branche0710 = d.kode::text AND d.niveau = 1. TOT = alle brancher (filter out for branch-level analysis).
- arbejdslands is inline: 0=Hele landet, 81–85=regioner, 1–11=landsdele, 950=Uden for Danmark, 99=Uoplyst. Contains both regioner and landsdele — filter by range to pick one level.
- Use this table to compare the industrial structure (branch mix) across regions, not for absolute headcounts.
- Map: /geo/regioner.parquet (codes 81–85) or /geo/landsdele.parquet (codes 1–11) — merge on arbejdslands::int=dim_kode. Exclude 0, 950, 99.
