table: fact.bygv22
description: Fuldført byggeri (ikke korrigeret for forsinkelser) efter område, enhed, påbegyndelsesår, byggesagstype, anvendelse og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- tal: values [46=Boliger (antal), 51=Samlet etageareal (m2)]
- aar: values [0=Samme år, 1=1 år tidligere, 2=2 år tidligere, 3=3 eller flere år tidligere]
- byggesag: values [1=Nybyggeri, 2=Tilbygning, 3=Ombygning]
- anvendelse: join dim.byganv on anvendelse=kode::text [approx]; levels [2, 3]
- tid: date range 2006-01-01 to 2025-07-01
dim docs: /dim/byganv.md, /dim/nuts.md
notes:
- tal is a measurement selector: 46=Boliger (antal), 51=Samlet etageareal (m2). Always filter to one value — failing to do so doubles all counts. indhold unit changes depending on tal.
- aar indicates lag from påbegyndelse to fuldførelse. To count buildings completed in a given year regardless of when started, sum across all aar values (or filter aar for lag analysis).
- byggesag covers three mutually exclusive types (nybyggeri, tilbygning, ombygning). Filter to byggesag='1' for new construction only.
- omrade joins dim.nuts but code '0' (Denmark total) is not in the dim. All three nuts levels (1, 2, 3) are present — filter `WHERE d.niveau=3` for kommuner to avoid double-counting.
- anvendelse joins dim.byganv at niveauer 2 and 3. Code 'UOPL' is not in the dim.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
