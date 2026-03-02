table: fact.bane21
description: Jernbanetransport af passagerer efter enhed, transporttype og tid
measure: indhold (unit -)
columns:
- enhed: values [150=1000 passagerer, 160=Mio. personkm]
- transport: values [10010=BANENETTET I ALT, 10020=BANEDANMARKS NET  I ALT, 10040=S-tog, 10050=Landsdækkende trafik, i alt, 10060=Øst for Storebælt, 10070=Vest for Storebælt, 10080=Over Storebælt, 10090=International trafik i alt, 10100=Øresundstog, 10110=Andre internationale tog, 10130=METROEN, 10120=ANDRE BANER, 10140=LETBANE]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- enhed is a measurement selector — always filter to exactly one value (150 for passagerer, 160 for personkm). Never aggregate across enhed.
- transport is hierarchical. Top: 10010 (BANENETTET I ALT) = 10020 (BaneDanmarks net) + 10130 (Metro) + 10120 (Andre baner) + 10140 (Letbane). Within BaneDanmarks net: 10020 = 10040 (S-tog) + 10050 (Landsdækkende) + 10090 (International). Landsdækkende: 10050 = 10060 + 10070 + 10080. International: 10090 = 10100 + 10110.
- For total rail: use transport=10010. For S-tog only: transport=10040. For Metro: transport=10130.
- Annual data from 1990. For quarterly data use bane25 (same codes, from 2006).
