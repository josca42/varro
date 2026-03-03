table: fact.isbu03
description: Iværksatte indsatser og støtte til børn og unge i året efter landsdel, indsats og tid
measure: indhold (unit Antal)
columns:
- landsdel: join dim.nuts on landsdel=kode; levels [2]
- indsatser: values [4=IVÆRKSATTE STØTTENDE INDSATSER I ALT, 5=TIDLIGT FOREBYGGENDE INDSATSER EFTER LOV OM SOCIAL SERVICE / BARNETS LOV, 6=INDSATSER OG STØTTE EFTER LOV OM SOCIAL SERVICE / BARNETS LOV, 7=INDSATSER EFTER LOV OM BEKÆMPELSE AF UNGDOMSKRIMINALITET]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- FLOW table (iværksatte = newly initiated interventions in the year), unlike isbu01/02 which are stock/active counts.
- indsatser has only 4 high-level categories (4=I alt, 5=Tidligt forebyggende, 6=SEL/BL, 7=Ungdomskriminalitetsloven). No detail codes — simplest indsatser table.
- landsdel joins dim.nuts at niveau 2 (11 landsdele). Code 0 = national total.
- No age or gender breakdown. For those use isbu04 (stock) or isbu01/02 (kommune level).
- Map: /geo/landsdele.parquet — merge on landsdel=dim_kode. Exclude landsdel=0.