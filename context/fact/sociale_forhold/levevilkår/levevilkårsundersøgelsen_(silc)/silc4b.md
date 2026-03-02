table: fact.silc4b
description: Boligbyrde: Andel personer efter indkomstgruppe, køn, i hvor høj grad husstanden synes boligudgiften er en byrde og tid
measure: indhold (unit Pct.)
columns:
- indkomgrp: values [KVTOT=I alt, 1K=1. kvintil, 2K=2. kvintil, 3K=3. kvintil, 4K=4. kvintil, 5K=5. kvintil]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- svaerhed1: values [100=I alt, 115=En tung byrde, 120=Noget af en byrde, 125=Ikke noget problem]
- tid: date range 2004-01-01 to 2024-01-01
notes:
- Housing cost burden by income quintile and gender. Same series as silc1b (2004–2024), percentages only.
- svaerhed1=100 is always indhold=100 (dummy total). Use svaerhed1 IN (115, 120, 125) for real distribution.
- indkomgrp: KVTOT=I alt, 1K–5K = income quintiles (1K = lowest, 5K = highest). Note: 1K (lowest income) has by far the highest housing burden.
- Note column name: this table uses kon (not koen like silc1b/silc2b). Values are still TOT, M, K.
