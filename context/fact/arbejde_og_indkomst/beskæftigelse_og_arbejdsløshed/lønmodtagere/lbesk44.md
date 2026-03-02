table: fact.lbesk44
description: Lønmodtagere efter enhed, bopælslandsdel, køn, alder og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- boplandk: join dim.nuts on boplandk=kode [approx]; levels [1, 2]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder, UDK=Uoplyst køn, uden bopæl i Danmark]
- alder: values [TOT=Alder i alt, U15=Under 15 år, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6064=60-64 år, 6574=65-74 år, 75OV=75 år og derover, UDK=Uoplyst alder, uden bopæl i Danmark]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/nuts.md
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- boplandk joins dim.nuts correctly (89% match). Unmatched: 0=Hele landet, 950=Uden for Danmark. Contains both niveau 1 (regioner: 81–85) and niveau 2 (landsdele: 1–11). Use WHERE d.niveau=1 for regioner or d.niveau=2 for landsdele to avoid summing across hierarchy levels. Join: JOIN dim.nuts d ON f.boplandk = d.kode WHERE d.niveau IN (1,2).
- Filter kon and alder to avoid overcounting: kon=TOT sums all genders; alder=TOT sums all ages.
- bopæls (residence) dimension — workers counted at home municipality, not workplace. Use lbesk63 for arbejdsstedslandsdel (workplace region).
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on boplandk=dim_kode. Exclude boplandk IN (0, 950).
