table: fact.ligedi0
description: Ligestillingsindikator for opstillede og valgte kandidater til folketingsvalg efter kandidater, indikator og tid
measure: indhold (unit -)
columns:
- kandidat: values [OK=Opstillede kandidater, VK=Valgte kandidater]
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- tid: date range 1918-01-01 to 2022-01-01

notes:
- Three indikator values are not additive: LA1=share of men (%), LA2=share of women (%), LA3=LA1−LA2 (difference in percentage points). Never sum across indikator. Pick the one you need.
- LA1+LA2=100 by construction. LA3 is derived and can be negative (if more women than men).
- Longest historical series for gender of candidates: back to 1918. For age breakdown, use ligedi1 (from 2001 only).
- National level only (no omrade). Data covers all elections where Folketing composition data is available.
