table: fact.naio1f
description: Input-output tabel. Tilgang fra brancher fordelt på anvendelse og prisenhed. (69-gruppering) efter tilgangstype, tilgang fra branche, anvendelse, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- tilgang1: values [P1_BP=Dansk produktion, P7AD2121=Import inkl. told, D2121=Told]
- tilgang2: join dim.nr_branche on tilgang2=kode [approx]
- anvendelse: join dim.nr_branche on anvendelse=kode [approx]
- prisenhed: values [V=Løbende priser, Y=Foregående års priser]
- tid: date range 1966-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- Same structure as naio1 but limited to the 69-groupering (niveau 4 = 5-digit codes). Codes in `tilgang2` are T-prefixed 5-digit (T01000, T06090, etc.) and letter codes (T, TA, TCA…). All match dim.nr_branche after stripping the T prefix: `SUBSTRING(f.tilgang2, 2) = d.kode`. Same applies to `anvendelse` with A-prefix.
- **prisenhed must be filtered** (V or Y) and **tilgang1 must be filtered** (P1_BP, P7AD2121, D2121). See naio1 notes for semantics.
- Use naio1f over naio1 when the 69-groupering detail is sufficient — it covers a longer series (to 2024 vs 2022) and has no out-of-dim codes.
- For `tilgang2` at the 69-group level: `WHERE LENGTH(f.tilgang2) = 6` selects only the 69 industry codes (level 4). Filter `d.niveau = 4` after joining for clean results.