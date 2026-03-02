table: fact.bane25
description: Jernbanetransport af passagerer efter enhed, transporttype og tid
measure: indhold (unit -)
columns:
- enhed: values [150=1000 passagerer, 160=Mio. personkm]
- transport: values [10010=BANENETTET I ALT, 10020=BANEDANMARKS NET  I ALT, 10040=S-tog, 10050=Landsdækkende trafik, i alt, 10060=Øst for Storebælt, 10070=Vest for Storebælt, 10080=Over Storebælt, 10090=International trafik i alt, 10100=Øresundstog, 10110=Andre internationale tog, 10130=METROEN, 10120=ANDRE BANER, 10140=LETBANE]
- tid: date range 2006-01-01 to 2025-04-01

notes:
- Quarterly version of bane21 — identical transport codes and enhed selector, but quarterly data (Jan/Apr/Jul/Oct). Prefer bane25 when you need current or recent quarterly figures.
- enhed is a measurement selector — always filter to exactly one value (150=passagerer, 160=personkm).
- transport is hierarchical (same as bane21): 10010 (total) = 10020 (BaneDanmark) + 10130 (Metro) + 10120 (Andre baner) + 10140 (Letbane). Do not sum sub-codes with their parents.
- For long annual series back to 1990, use bane21 instead.
