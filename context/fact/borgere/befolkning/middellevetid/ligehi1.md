table: fact.ligehi1
description: Ligestillingsindikator for middellevetid for 0-årige efter indikator og tid
measure: indhold (unit -)
columns:
- indikator: values [M2=Mænd (år), K2=Kvinder (år), F2=Forskel mellem mænd og kvinder (år)]
- tid: date range 1901 to 2025

notes:
- indikator encodes three separate metrics: M2 and K2 are life expectancy in years; F2 = M2 − K2 (negative, because men live shorter — e.g. F2=−3.8 means women live 3.8 years longer). Never sum across indikator values.
- tid is a 2-year rolling range (e.g. [2023,2025), [2022,2024), ...). Use lower(tid) for the start year. Long series back to 1901 makes this good for historical gender gap analysis.
- F2 is pre-computed, so no need to join or subtract manually. For just men vs women, hisb7 has the same series back to 1840 with individual-year (non-rolling) tid.
