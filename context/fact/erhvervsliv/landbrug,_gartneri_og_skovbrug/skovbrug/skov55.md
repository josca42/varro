table: fact.skov55
description: Hugsten i skove og plantager i Danmark efter område, træsort og tid
measure: indhold (unit 1.000 m3)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2]
- traesort: values [00010=Hugst i alt, 00020=Gavntræ i alt, 00030=Brænde i alt, 00090=Energitræ som flis i alt, 00100=Energitræ som rundtræ i alt ... 00086=Nåletræ - Industritræ, 00088=Nåletræ - Andet gavntræ, NALBRAEND=Nåletræ - Brænde, 00170=Nåletræ - Energitræ som flis, 00180=Nåletræ - Energitræ som rundtræ]
- tid: date range 2006-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts, but codes 0 (Hele landet) and 15 (combined Copenhagen/Sjælland landsdel aggregate) are not in dim.nuts — same structure as skov11. Code 15 only appears in years 2006–2015; from 2016 onward only omrade=0 and regions 81–85 are available. See skov11 notes for full omrade details.
- traesort has two orthogonal hierarchy dimensions — pick one and filter to that level only. By product type: 00020=Gavntræ i alt, 00030=Brænde i alt, 00090=Energitræ som flis i alt, 00100=Energitræ som rundtræ i alt. These four sum to 00010=Hugst i alt. By species: 00110=Løvtræ i alt, 00080=Nåletræ i alt. These two also sum to 00010.
- Within species groups: Løvtræ subcodes are 00050=Bøg, 00060=Eg, 00070=Andet løvtræ. Nåletræ subcodes are 00082–00088. Species×product detail codes (BOGGAVN, BOGBRAEND, NALGAVN, NALBRAEND, etc.) are the most granular level.
- Summing all traesort codes together massively overcounts because aggregate and detail codes all coexist in the table. Always pick exactly one level: 00010 (total), or one of the two product/species breakdowns, or individual species codes.
- skov55 has more traesort codes than skov55a (which lacks energitræ breakdowns). For trend analysis combining both tables, use the common codes: 00010, 00020, 00030, 00050, 00060, 00070, 00080.
- Map: context/geo/landsdele.parquet (niveau 2) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade IN (0, 15).