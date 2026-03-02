table: fact.skib74
description: Godsomsætning på større havne efter landegrupper, godsart og tid
measure: indhold (unit 1.000 ton)
columns:
- landgrp: values [0=I ALT, 10=Danmark, 40=Øvrige Europa, 90=Andre område]
- gods: values [100=GODS I ALT, 260=Indgående gods i alt, 262=Indgående flydende bulk, 264=Indgående fast bulk, 266=Indgående stykgods, 268=Indgående færgegods, 270=Udgående gods i alt, 272=Udgående flydende bulk, 274=Udgående fast bulk, 276=Udgående stykgods, 278=Udgående færgegods]
- tid: date range 2000-01-01 to 2025-04-01
notes:
- gods encodes BOTH direction AND cargo type in a single column — this is unusual. Code 100=GODS I ALT (grand total). Then: 260=Indgående gods i alt → 262 flydende bulk + 264 fast bulk + 266 stykgods + 268 færgegods; 270=Udgående gods i alt → 272 flydende bulk + 274 fast bulk + 276 stykgods + 278 færgegods. Never sum across all gods codes — they form a two-level hierarchy within the column.
- landgrp has 4 values: 0=I ALT, 10=Danmark, 40=Øvrige Europa, 90=Andre område. Filter to avoid double-counting (0 is the total of 10+40+90).
- Simplest table in the subject for an overview by origin/destination region with cargo category. Current through 2025. Use when you only need broad geographic groups + cargo category; use skib44/skib50 for country-level detail.
