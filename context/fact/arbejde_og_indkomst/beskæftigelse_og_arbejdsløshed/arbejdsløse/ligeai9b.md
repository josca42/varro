table: fact.ligeai9b
description: Ligestillingsindikator for fuldtidsledige (sæsonkorrigeret) efter indikator og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- tid: date range 2007-01-01 to 2025-09-01

notes:
- indikator selects between LA1/LA2/LA3. Never sum across indikator values — these are pre-computed rates and differences.
- Seasonally adjusted monthly series. Most current gender indicator table (to 2025-09). No regional or age breakdown. For those use ligeai9a (annual) or ligeai10 (long-term unemployed).