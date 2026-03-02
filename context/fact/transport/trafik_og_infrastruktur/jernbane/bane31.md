table: fact.bane31
description: Trafikarbejde med tog efter transporttype og tid
measure: indhold (unit 1.000 togkm)
columns:
- transport: values [10010=BANENETTET I ALT, 10020=BANEDANMARKS NET  I ALT, 10025=Persontog i alt, 10040=S-tog, 10050=Landsdækkende trafik, i alt, 10060=Øst for Storebælt, 10070=Vest for Storebælt, 10080=Over Storebælt, 10090=International trafik i alt, 10100=Øresundstog, 10110=Andre internationale tog, 10115=Godstog, 10130=METROEN, 10120=ANDRE BANER, 10140=LETBANE]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- transport is hierarchical — do NOT sum all codes. Top level: 10010 (I ALT) = 10020 (BANEDANMARKS NET) + 10120 (ANDRE BANER) + 10130 (METROEN) + 10140 (LETBANE). Within BANEDANMARKS NET: 10025 (Persontog) + 10115 (Godstog). Within Persontog: 10040 (S-tog) + 10050 (Landsdækkende) + 10090 (International). Pick exactly one hierarchy level.
- No enhed column — each (transport, tid) pair is a single row. Table is simple once you pick the right transport code.
- Not all transport codes span the full 1990–2024 range: METROEN starts 2002, LETBANE starts 2017, Øresundstog/Andre internationale start 2014. Expect NULLs for earlier years on those codes.
- indhold unit is 1.000 togkm (thousands of train-km). Multiply by 1000 for absolute km if needed.