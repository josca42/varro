table: fact.lbesk30
description: Lønmodtagere (sæsonkorrigeret) efter enhed, arbejdsstedslandsdel og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- arbejdslands: values [0=Hele landet, 84=Region Hovedstaden, 1=Landsdel Byen København, 2=Landsdel Københavns omegn, 3=Landsdel Nordsjælland, 4=Landsdel Bornholm, 85=Region Sjælland, 5=Landsdel Østsjælland, 6=Landsdel Vest- og Sydsjælland, 83=Region Syddanmark, 7=Landsdel Fyn, 8=Landsdel Sydjylland, 82=Region Midtjylland, 9=Landsdel Østjylland, 10=Landsdel Vestjylland, 81=Region Nordjylland, 11=Landsdel Nordjylland, 950=Uden for Danmark, 99=Uoplyst]
- tid: date range 2008-01-01 to 2025-04-01
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- arbejdslands is inline (no dim join). Contains both regioner (81–85) and landsdele (1–11) plus 0=Hele landet, 950=Uden for Danmark, 99=Uoplyst. Filter by value range to pick a level: regioner WHERE arbejdslands::int BETWEEN 81 AND 85; landsdele WHERE arbejdslands::int BETWEEN 1 AND 11.
- Sæsonkorrigeret. For ukorrigeret version with same structure, there is no equivalent single-column variant — see lbesk33 (which adds sektor).
- Map: context/geo/regioner.parquet (codes 81–85) or context/geo/landsdele.parquet (codes 1–11) — merge on arbejdslands::int=dim_kode. Exclude 0, 950, 99.
