table: fact.off29
description: Offentlig forvaltning og service, funktionel fordeling af udgifter (COFOG) efter funktion og tid
measure: indhold (unit Mio. kr.)
columns:
- funktion: join dim.cofog on funktion=kode::text [approx]; levels [1]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/cofog.md

notes:
- funktion uses a 2-level dotted notation (77 values: TOTAL, 1–10 at niveau=1, plus 1.1–10.9 at niveau=2) that only partially matches dim.cofog's concatenated codes.
- For niveau=1 (codes '1'–'10'): join works directly — `JOIN dim.cofog d ON f.funktion = d.kode::text AND d.niveau = 1`.
- For niveau=2 (codes like '1.1', '10.9'): remove the dot to get the dim code — `JOIN dim.cofog d ON REPLACE(f.funktion, '.', '') = d.kode::text AND d.niveau = 2`. E.g. '1.1'→'11', '10.1'→'101'.
- TOTAL is the grand aggregate with no dim match — filter it out or handle separately.
- Do not mix niveau=1 and niveau=2 rows when aggregating — they represent the same expenditure at different granularities (double-counting).