table: fact.fohoj04
description: Antallet af højskolekursister efter kursustype, bopælsområde, køn, institution, enhed, tidsangivelse og tid
measure: indhold (unit Antal)
columns:
- kursus: values [TOT=I alt, 40=Kort kursus, 50=Mellemlangt kursus, 60=Langt kursus]
- bopland: values [0=Hele landet, 1=Landsdel Byen København, 2=Landsdel Københavns omegn, 3=Landsdel Nordsjælland, 4=Landsdel Bornholm, 5=Landsdel Østsjælland, 6=Landsdel Vest- og Sydsjælland, 7=Landsdel Fyn, 8=Landsdel Sydjylland, 9=Landsdel Østjylland, 10=Landsdel Vestjylland, 11=Landsdel Nordjylland, 99=Uoplyst]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- insti: values [0=Højskoler i alt, 102=Ungdomshøjskoler, 108=Seniorhøjskoler, 109=Folkehøjskoler]
- enhed: values [11=Kursister, 13=Årselever]
- tidspunkter: values [22=Skoleår, 11=Kalenderår]
- tid: date range 2016-01-01 to 2024-01-01
notes:
- CRITICAL: enhed and tidspunkter are both measurement selectors. Always filter both to a single value.
- bopland=0 is national total; bopland=99 is unspecified. The 11 landsdele (1–11) are the geographic breakdown.
- bopland uses the same numeric landsdel codes as dim.nuts niveau=2, but with no leading zeros (1–11). Join: f.bopland::text = d.kode WHERE d.niveau = 2 AND f.bopland NOT IN (0, 99).
- insti=0 is total across all institution types; filter when comparing ungdomshøjskoler vs seniorhøjskoler vs folkehøjskoler.
- kursus=TOT and kon=TOT are totals.
- Map: context/geo/landsdele.parquet — merge on bopland=dim_kode. Exclude bopland IN (0, 99).
