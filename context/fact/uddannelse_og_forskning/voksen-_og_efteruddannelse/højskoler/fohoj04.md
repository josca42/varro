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
- `enhed` and `tidspunkter` are measurement selectors — filter both to avoid doubling. Both are smallint.
- 2024 data only has tidspunkter=22 (Skoleår). For Kalenderår, the latest available year is 2023.
- `bopland` is landsdel codes (smallint): 0=Hele landet (total), 1–11=de 11 landsdele, 99=Uoplyst. These are NOT NUTS codes — they are DST's own landsdel numbering. Individual landsdele (1–11) plus uoplyst (99) sum to the total (0).
- `insti` institution codes differ from `insttyp` in veuhoj11/veuhoj21: fohoj04 uses 109=Folkehøjskoler (not 101=Almene og grundtvigske). 108=Seniorhøjskoler only has kursus=40 (Kort) and TOT — no Mellemlangt or Langt.
- `kursus`, `kon` are varchar; `bopland`, `insti`, `enhed`, `tidspunkter` are all smallint.
- This is the only table with geographic breakdown of participants by residence (bopland). The other tables have no regional dimension.
- Map: /geo/landsdele.parquet — merge on bopland=dim_kode. Exclude bopland=0 (Hele landet) and bopland=99 (Uoplyst). bopland codes 1–11 align with dim.nuts niveau 2 kode despite the non-NUTS labeling.