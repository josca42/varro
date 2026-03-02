table: fact.lbesk63
description: Lønmodtagere efter enhed, arbejdsstedslandsdel, køn, alder og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- arbejdslands: values [0=Hele landet, 84=Region Hovedstaden, 1=Landsdel Byen København, 2=Landsdel Københavns omegn, 3=Landsdel Nordsjælland, 4=Landsdel Bornholm, 85=Region Sjælland, 5=Landsdel Østsjælland, 6=Landsdel Vest- og Sydsjælland, 83=Region Syddanmark, 7=Landsdel Fyn, 8=Landsdel Sydjylland, 82=Region Midtjylland, 9=Landsdel Østjylland, 10=Landsdel Vestjylland, 81=Region Nordjylland, 11=Landsdel Nordjylland, 950=Uden for Danmark, 99=Uoplyst]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder, UDK=Uoplyst køn, uden bopæl i Danmark]
- alder: values [TOT=Alder i alt, U15=Under 15 år, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6064=60-64 år, 6574=65-74 år, 75OV=75 år og derover, UDK=Uoplyst alder, uden bopæl i Danmark]
- tid: date range 2008-01-01 to 2025-04-01
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- arbejdslands is inline (no dim join). Contains both regioner (81–85) and landsdele (1–11) plus 0=Hele landet, 950=Uden for Danmark, 99=Uoplyst. Filter by range: regioner WHERE arbejdslands::int BETWEEN 81 AND 85; landsdele WHERE arbejdslands::int BETWEEN 1 AND 11.
- arbejdssteds (workplace) dimension — workers counted where they work, not where they live. Use lbesk44 for bopælslandsdel (residence region).
- Filter kon and alder (TOT codes are aggregate rows — exclude when summing individual categories).
- Map: context/geo/regioner.parquet (codes 81–85) or context/geo/landsdele.parquet (codes 1–11) — merge on arbejdslands::int=dim_kode. Exclude 0, 950, 99.
