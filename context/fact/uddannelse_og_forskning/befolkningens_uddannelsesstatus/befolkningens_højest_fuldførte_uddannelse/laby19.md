table: fact.laby19
description: Befolkningens højest fuldførte uddannelse (15-69 år) (antal) efter kommunegruppe, højest fuldførte uddannelse, alder og tid
measure: indhold (unit Antal)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode [approx]; levels [1, 2]
- hfudd2: join dim.ddu_udd on hfudd2=kode [approx: H prefix needs stripping]
- alder: values [TOT=Alder i alt, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/ddu_udd.md, /dim/kommunegrupper.md

notes:
- komgrp joins dim.kommunegrupper for codes 1-5 (niveau 1: de 5 kommunegruppe-typer) and 101-860 (niveau 2: individuelle kommuner). Code 0=national total (not in dim). Code 411=Christiansø (exists in dim.nuts but NOT in dim.kommunegrupper — exclude or label manually).
- hfudd2 does NOT join dim.ddu_udd — completely different coding scheme. The H-prefixed codes are a standalone classification with 92 values at multiple hierarchy levels: TOT > H10-H90 (10 top-level, 3-char codes) > H1001/H1010/H2010/... (detailed subcodes). Mixing levels causes double-counting.
- To avoid hfudd2 double-counting: filter WHERE LENGTH(hfudd2) = 3 to get the 10 top-level categories (H10-H90) that match other tables, plus TOT. The sub-codes (H1001, H3010, etc.) are subcategories of these.
- Use ColumnValues("laby19", "hfudd2") to browse all 92 education codes. The naming pattern: H10=Grundskole, H1001/H1010/H1020/H1030 are its subcategories.
- This table has individual municipality detail (unlike laby19a which has only the 5 kommunegrupper).
- Map: context/geo/kommuner.parquet — filter komgrp > 100 for individual municipalities, merge on komgrp=dim_kode. Exclude komgrp=0.