table: fact.lbesk33
description: Lønmodtagere efter enhed, arbejdsstedslandsdel, sektor og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- arbejdslands: join dim.nuts on arbejdslands=kode [approx]; levels [1, 2]
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1035=Offentlige virksomheder, 1040=Private virksomheder, 1045=Private nonprofit-organisationer, 1050=Uoplyst]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/nuts.md
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- arbejdslands joins dim.nuts correctly (84% match). Unmatched special codes: 0=Hele landet, 99=Uoplyst, 950=Uden for Danmark — exclude these from dim join. Contains both niveau 1 (regioner: 81–85) and niveau 2 (landsdele: 1–11). Filter d.niveau=1 for regioner or d.niveau=2 for landsdele to avoid summing both levels.
- sektor is inline (correct — no broken join here). Values: 1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1035=Offentlige virksomheder, 1040=Private virksomheder, 1045=Private nonprofit-organisationer, 1050=Uoplyst.
- Example: lønmodtagere per region by sector: filter tal=1020, sektor != 1000, AND d.niveau=1.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on arbejdslands=dim_kode. Exclude arbejdslands IN (0, 99, 950).
