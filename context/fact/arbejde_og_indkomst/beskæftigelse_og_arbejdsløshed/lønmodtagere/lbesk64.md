table: fact.lbesk64
description: Lønmodtagere efter enhed, arbejdsstedslandsdel, køn, herkomst og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- arbejdslands: values [0=Hele landet, 84=Region Hovedstaden, 1=Landsdel Byen København, 2=Landsdel Københavns omegn, 3=Landsdel Nordsjælland, 4=Landsdel Bornholm, 85=Region Sjælland, 5=Landsdel Østsjælland, 6=Landsdel Vest- og Sydsjælland, 83=Region Syddanmark, 7=Landsdel Fyn, 8=Landsdel Sydjylland, 82=Region Midtjylland, 9=Landsdel Østjylland, 10=Landsdel Vestjylland, 81=Region Nordjylland, 11=Landsdel Nordjylland, 950=Uden for Danmark, 99=Uoplyst]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder, UDK=Uoplyst køn, uden bopæl i Danmark]
- herkomst: join dim.herkomst on herkomst=kode::text [approx]; levels [1]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/herkomst.md
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- arbejdslands is inline (no dim join). Contains regioner (81–85) and landsdele (1–11) plus 0=Hele landet, 950=Uden for Danmark, 99=Uoplyst — filter by range to pick a level.
- WARNING: dim.herkomst join is mostly broken. herkomst uses: 1=Dansk, 24=Indvandrere vestlige, 25=Indvandrere ikke-vestlige, 34=Efterkommere vestlige, 35=Efterkommere ikke-vestlige, TOT=I alt, UDK=Uoplyst. Treat as inline.
- Workplace-based regional breakdown combined with herkomst. Pair with lbesk45 (bopæl + herkomst) to compare commuting patterns by origin.
- Map: context/geo/regioner.parquet (codes 81–85) or context/geo/landsdele.parquet (codes 1–11) — merge on arbejdslands::int=dim_kode. Exclude 0, 950, 99.
