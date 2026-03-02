table: fact.naio1
description: Input-output tabel. Tilgang fra brancher fordelt på anvendelse og prisenhed efter tilgangstype, tilgang fra branche, anvendelse, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- tilgang1: values [P1_BP=Dansk produktion, P7AD2121=Import inkl. told, D2121=Told]
- tilgang2: join dim.nr_branche on tilgang2=kode [approx]
- anvendelse: join dim.nr_branche on anvendelse=kode [approx]
- prisenhed: values [V=Løbende priser, Y=Foregående års priser]
- tid: date range 1966-01-01 to 2022-01-01
dim docs: /dim/nr_branche.md

notes:
- **prisenhed is a measurement selector** — V=løbende priser, Y=foregående års priser. Always filter to one value or you silently double all counts. Use `WHERE prisenhed = 'V'` for current prices.
- **tilgang1 must be filtered** — P1_BP=Dansk produktion, P7AD2121=Import inkl. told, D2121=Told. For most analyses, filter to `P1_BP` (domestic production). Summing all three overcounts.
- **The dim join uses a prefix-stripping pattern.** `tilgang2` codes have a T-prefix (TA, T01000, T010000); `anvendelse` codes have an A-prefix (AA, A01000). The documented join `f.tilgang2=d.kode` does NOT work — use `SUBSTRING(f.tilgang2, 2) = d.kode` and `SUBSTRING(f.anvendelse, 2) = d.kode` instead.
- `tilgang2` (supply from industries): hierarchy: `T` = i alt total, `TA`-`TU` = niveau 1–2 letter codes, `TCA` etc = niveau 3, `T10120` = niveau 4 (5-digit, 69-group), `T100010` = niveau 5 (6-digit). naio1 also contains 98 additional 6-digit codes beyond dim.nr_branche niveau 5 (a more detailed grouping not in the dim). Filter by `d.niveau` to avoid double-counting across hierarchy levels.
- `anvendelse` (demand side): A-prefixed industry codes for intermediate consumption (AI00000=forbrug i produktionen i alt, AA00000=anvendelse i alt), PLUS special final demand codes not in dim.nr_branche (ACP=privat forbrug, ABI=investeringer, AIAE=endelig anvendelse, AE6000=eksport, AL5253=lagerforøgelser). Use ColumnValues("naio1", "anvendelse") to see all 447 codes.
- For a typical "which industries produce the most" query: filter `tilgang1='P1_BP'`, `prisenhed='V'`, `anvendelse='AA00000'` (total demand), then group `tilgang2` at desired `d.niveau`.