table: fact.lbesk67
description: Lønmodtagere efter enhed, bopælslandsdel, sektor, køn, alder og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- boplandk: values [0=Hele landet, 84=Region Hovedstaden, 1=Landsdel Byen København, 2=Landsdel Københavns omegn, 3=Landsdel Nordsjælland, 4=Landsdel Bornholm, 85=Region Sjælland, 5=Landsdel Østsjælland, 6=Landsdel Vest- og Sydsjælland, 83=Region Syddanmark, 7=Landsdel Fyn, 8=Landsdel Sydjylland, 82=Region Midtjylland, 9=Landsdel Østjylland, 10=Landsdel Vestjylland, 81=Region Nordjylland, 11=Landsdel Nordjylland, 950=Uden for Danmark]
- sektor: join dim.esr_sekt on sektor::text=kode
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder, UDK=Uoplyst køn, uden bopæl i Danmark]
- alder: values [TOT=Alder i alt, U15=Under 15 år, 1524=15-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover, UDK=Uoplyst alder, uden bopæl i Danmark]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/esr_sekt.md
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- boplandk is inline here (no dim join — values listed directly). Contains regioner (81–85) and landsdele (1–11) plus 0=Hele landet, 950=Uden for Danmark. Filter by range to pick one geographic level.
- WARNING: dim.esr_sekt join for sektor is broken (0% match). Use ColumnValues("lbesk67", "sektor") — values match lbesk61/lbesk33 pattern: 1000=total, 1032=Offentlig, 1035=Offentlige virksomheder, 1040=Private, 1045=Private nonprofit, 1050=Uoplyst.
- alder here uses 10-year bands (1524, 2534, 3544, 4554, 5564, 6574, 75OV) — coarser than lbesk44 (5-year bands). TOT=sum of all ages.
- Data ends 2025-01.
- Map: context/geo/regioner.parquet (codes 81–85) or context/geo/landsdele.parquet (codes 1–11) — merge on boplandk::int=dim_kode. Exclude 0, 950.
