table: fact.bygv02
description: Landstal for fuldført byggeri (ikke korrigeret for forsinkelser) efter påbegyndelsesår, enhed, byggesagstype, anvendelse og tid
measure: indhold (unit -)
columns:
- ar: values [0=Samme år, 1=1 år tidligere, 2=2 år tidligere, 3=3 eller flere år tidligere]
- tal: values [46=Boliger (antal), 51=Samlet etageareal (m2)]
- byggesag: values [1=Nybyggeri, 2=Tilbygning, 3=Ombygning]
- anvendelse: join dim.byganv on anvendelse=kode::text [approx]; levels [2, 3]
- tid: date range 1998-01-01 to 2024-01-01
dim docs: /dim/byganv.md
notes:
- tal is a measurement selector: 46=Boliger (antal), 51=Samlet etageareal (m2). Always filter to one — failing to do so doubles all counts. indhold unit changes depending on tal.
- aar indicates lag from påbegyndelse to fuldførelse. To count all completions in a year regardless of start year, sum across all aar values.
- byggesag covers three mutually exclusive types — filter to byggesag='1' for new construction only.
- National totals only (no regional breakdown). The regional equivalent is bygv22 (from 2006).
- anvendelse joins dim.byganv at niveauer 2 and 3. Code 'UOPL' is not in the dim.
