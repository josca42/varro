table: fact.bevil01b
description: Offentlige kulturbevillinger efter kulturemne, formål, finansieringskilde, finansieringsart og tid
measure: indhold (unit Mio. kr.)
columns:
- kulturemne: join dim.kulturemner on kulturemne::text=kode [approx: Dimension uses K prefix for niveau-2 codes (K09 vs 9)]; levels [1]
- formal: values [1000=Alle formål, 1005=Departementet - Almindelig virksomhed (FL 21110110), 1010=Slots- og Kulturstyrelsen - Almindelig virksomhed (FL 21111110), 1015=Slots- og Kulturstyrelsen - Sekretariatet for DDB (FL 21111122), 1020=Slots- og Kulturstyrelsen - Slots- og ejendomsvirksomhed (FL 21111140) ... 2405=Fælles formål - teatre (KB 34583), 2410=Fælles formål - andet (KB 34583), 2415=Fælles formål - folkeoplysning (KB 34583), 2420=Fælles formål - folkebibliotek (KB 34583), 2425=Fælles formål - biograf (KB 34583)]
- finans: values [405=OFFENTLIG I ALT, 401=Kommuner, 404=STATEN I ALT, 400=Finanslov - Kulturministeriet, 406=Finanslov - Øvrige ministerier, 402=Udlodningsmidler (Tips), 403=Licensmidler]
- finansart: values [0=I alt, 40=Anlæg, 41=Distribution, 43=Drift, 39=Personlig, 42=Projekt]
- tid: date range 2020-01-01 to 2025-01-01
dim docs: /dim/kulturemner.md

notes:
- `kulturemne` stores smallint codes: 0=I alt, 1–6=niveau-1 subjects (match dim directly), 7–34=niveau-2 subjects (need K-prefix join), 99=Uoplyst. The documented join `kulturemne::text = kode` only resolves codes 1–6. For niveau-2 use: `JOIN dim.kulturemner d ON 'K' || LPAD(f.kulturemne::text, 2, '0') = d.kode`. Codes 0 and 99 are not in the dim.
- `formal` has 1000=Alle formål as an aggregate. Filter `formal=1000` for totals, or use ColumnValues("bevil01b", "formal") to browse specific budget lines.
- `finans` has hierarchical aggregates: 405=all public (includes 401+404+402+403+406), 404=all state. Filter to exactly one level to avoid double-counting. For total public bevillinger use `finans=405`.
- `finansart=0` is I alt. Filter to 0 for total or pick a specific type.
- This table only goes back to 2020. For a longer series use bevil02 (from 2007) which lacks the `formal` breakdown.