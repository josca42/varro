table: fact.rst04
description: Losning af råstoffer fra havet (1000 m3) efter område, råstoftype og tid
measure: indhold (unit 1.000 m3)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- rastoftype: values [TOTHAV=SAMLET INDVINDING PÅ HAV, SAND1=Sand, RAL=Ral og sten, GRUS=Grus, FYLD=Fyldsand, GRABSØ=Grabsten og søsten, SKALLER=Skaller, ANDET=Andet]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts but contains codes at THREE hierarchy levels: niveau 1 (5 regioner), niveau 2 (1 code: landsdel Byen København, kode='1'), and niveau 3 (98 kommuner). Querying without a niveau filter causes double-counting. Filter to one: `WHERE d.niveau = 3` for kommune-level, `WHERE d.niveau = 1` for regional.
- Several omrade codes fall outside dim.nuts: '0' = national total; '99' = legacy code present only in 2022 with all-zero values (ignore); '990'–'997' = 8 sea district codes with real data but no dim label. These sea districts appear to be special harvest zones at sea rather than administrative areas. They have no human-readable names in the data — values are small and partial. Exclude them when doing geographic rollups via NUTS, or handle separately.
- This table tracks LOSNING (offloading/landing) of sea-harvested materials by the administrative area where the ship docked, not the extraction location. For extraction by sea area, use rst3.
- rastoftype TOTHAV = aggregate total across all types. Filter `WHERE rastoftype != 'TOTHAV'` when summing across types. The 7 individual sea types are: SAND1, RAL, GRUS, FYLD, GRABSØ, SKALLER, ANDET.
- Use `ColumnValues("nuts", "titel", for_table="rst04")` to see the 104 dim-matched omrade codes (filters out the unmapped 990-997 sea districts).
- indhold unit is 1.000 m³.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade IN (0, 99) and omrade codes 990–997 (unmapped sea districts).