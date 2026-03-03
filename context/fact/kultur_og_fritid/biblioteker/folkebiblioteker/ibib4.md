table: fact.ibib4
description: Udlån og lånere efter område, afstand fra bopæl til folkebiblioteket, kategori og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- afstandbib: values [30=I alt, 90030=0-499m, 90035=500-999m, 90040=1000-1499m, 90045=1500-1999m, 90050=2000-2499m, 90055=2500-2999m, 90060=3000-3999m, 90065=4000-4999m, 90070=5000-7499m, 90075=7500-9999m, 90080=10000m og derover, 90090=Uoplyst]
- dyrkat: values [9015=Udlån, 9020=Lånere]
- tid: date range 2020-01-01 to 2025-04-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at all 3 levels + omrade=0.
- afstandbib: 30=I alt (total), then distance bands from 0-499m up to 10000m+, plus 90090=Uoplyst. Filter to 30 for totals, or specific distance bands for geographic access analysis. Don't sum distance bands with the total (30).
- dyrkat limited to 9015=Udlån and 9020=Lånere — no "persons in population" (9025) unlike ibib1–3.
- ibib4 (to 2025) vs ibib4a (archive, to 2024).
- Useful for analyzing access equity — areas with longer distances to libraries tend to show lower borrowing rates.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
