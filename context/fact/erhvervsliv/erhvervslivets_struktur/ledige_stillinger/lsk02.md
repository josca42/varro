table: fact.lsk02
description: Ledige stillinger efter region, enhed og tid
measure: indhold (unit -)
columns:
- region: join dim.nuts on region=kode [approx]; levels [1, 2]
- enhed: values [LS=Ledige stillinger (antal), ALS=Andel ledige stillinger (procent)]
- tid: date range 2010-01-01 to 2025-04-01
dim docs: /dim/nuts.md

notes:
- Quarterly data (tid steps are Jan/Apr/Jul/Oct). For annual data, use ls02.
- enhed is a measurement selector: LS=antal, ALS=procent. Always filter to one. ALS must never be summed.
- region joins dim.nuts but code 1 in this table is the national total, NOT Landsdel Byen København (same issue as ls02 — verified by summing). Only codes 81-85 join correctly to dim.nuts niveau 1 (the 5 Danish regions).
- Code 135 is unmatched in dim.nuts — a small residual/special category.
- For regional quarterly vacancy series: WHERE region IN ('81','82','83','84','85') AND enhed='LS', JOIN dim.nuts ON region=kode.
- Map: context/geo/regioner.parquet — merge on region=dim_kode. Filter to region IN ('81','82','83','84','85') only (exclude code 1 and 135).
