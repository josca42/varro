table: fact.bevil02
description: Offentlige kulturbevillinger efter kulturemne, finansieringskilde, finansieringsart og tid
measure: indhold (unit Mio. kr.)
columns:
- kulturemne: join dim.kulturemner on kulturemne::text=kode [approx: Dimension uses K prefix for niveau-2 codes (K09 vs 9)]; levels [1]
- finans: values [405=OFFENTLIG I ALT, 401=Kommuner, 404=STATEN I ALT, 400=Finanslov - Kulturministeriet, 406=Finanslov - Øvrige ministerier, 402=Udlodningsmidler (Tips), 403=Licensmidler]
- finansart: values [0=I alt, 40=Anlæg, 41=Distribution, 43=Drift, 39=Personlig, 42=Projekt]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/kulturemner.md

notes:
- Same kulturemne coding as bevil01b: smallint codes 0=I alt, 1–6=niveau-1 (match dim), 7–34=niveau-2 (use `'K'||LPAD(f.kulturemne::text, 2, '0') = d.kode`), 99=Uoplyst.
- `finans` has hierarchical aggregates: 405=all public, 404=all state. Pick one level. For total public spending use `finans=405 AND finansart=0`.
- `finansart=0` is I alt (aggregate). Filter to 0 for total.
- Longest time series for public cultural funding in this subject (2007–2025). Use for trend analysis. Lacks `formal` detail — use bevil01b if you need specific budget line breakdowns.