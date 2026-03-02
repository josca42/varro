table: fact.barlov3
description: Samboende forældre på barselsorlov i barnets første leveår (børn født 2. august - 31. december) efter enhed, berettigelse, område, uger og tid
measure: indhold (unit Antal)
columns:
- tal: values [225=Mor - i alt, 226=Mor - øremærket orlov, 227=Mor - ikke øremærket orlov, 228=Mor - uspecificeret orlov, 325=Far - i alt, 326=Far - øremærket orlov, 327=Far - ikke øremærket orlov, 328=Far - uspecificeret orlov]
- beret: values [203=Far holdt barselsorlov, 330=Mor holdt barselsorlov, 633=Både mor og far holdt barseslsorlov, 635=Mor holdt barselsorlov, far holdt ikke barselsorlov, 639=Mor holdt barselsorlov, far er ikke berettiget til barselsdagpenge, 653=Mor holdt ikke barselsorlov, far holdt barselsorlov, 793=Mor er ikke berettiget, far holdt barselsorlov]
- omr20: join dim.nuts on omr20=kode [approx: Missing codes 0, 99 (likely total/unknown)]; levels [2, 3]
- uger: values [U00=Uge 0, U01=Uge 1, U02=Uge 2, U03=Uge 3, U04=Uge 4 ... U48=Uge 48, U49=Uge 49, U50=Uge 50, U51=Uge 51, U52=Uge 52]
- tid: date range AUG - DEC 2019 to AUG - DEC 2023
dim docs: /dim/nuts.md

notes:
- Same structure as barlov2 but with region (`omr20`) instead of education (morud/farud). Trade-off: use barlov2 for education × week detail, barlov3 for region × week detail.
- `tal` is a measurement selector (same 8 values as barlov2). Always filter to one.
- `omr20` joins dim.nuts via `f.omr20 = d.kode`. Code `0` = national total (not in dim). niveau 2 = 11 landsdele, niveau 3 = 98 kommuner. Filter `d.niveau` to avoid mixing levels.
- `uger` same caveats as barlov2.
- `beret` has no "all parents" total — only took-leave codes. Do not sum across beret.
- Coverage: Aug–Dec birth cohorts 2019–2023 only.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/landsdele.parquet (niveau 2) — merge on omr20=dim_kode. Exclude omr20=0.