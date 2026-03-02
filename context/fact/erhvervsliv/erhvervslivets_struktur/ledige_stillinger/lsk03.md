table: fact.lsk03
description: Ledige stillinger (sæsonkorrigeret) efter enhed, sæsonkorrigering og tid
measure: indhold (unit -)
columns:
- enhed: values [LS=Ledige stillinger (antal), ALS=Andel ledige stillinger (procent)]
- saeson: values [10=Sæsonkorrigeret, 20=Faktiske tal]
- tid: date range 2010-01-01 to 2025-04-01

notes:
- Quarterly data. The only table in this subject with seasonally adjusted figures.
- Both enhed AND saeson are measurement selectors — every data point appears twice (once as Sæsonkorrigeret, once as Faktiske tal) and also twice as LS/ALS. Always filter both columns to a single value.
- saeson=10 (seasonally adjusted) removes seasonal patterns; saeson=20 (actual) matches raw survey counts.
- No industry or regional breakdown — for that use lsk01 (branche/storrelse) or lsk02 (region).
- Simple query: WHERE enhed='LS' AND saeson=20 for actual quarterly vacancy counts, or saeson=10 for trend analysis.