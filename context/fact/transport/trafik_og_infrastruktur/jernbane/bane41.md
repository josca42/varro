table: fact.bane41
description: Jernbanenettet pr. 1. januar efter banenet, enhed og tid
measure: indhold (unit -)
columns:
- bane: values [10010=BANENETTET I ALT, 10020=BANEDANMARKS NET  I ALT, 10121=Hovedbaner, 10122=Regionalbaner, 10123=S-baner, 10124=Lokalbaner, 10125=Godsbaner, 10130=METROEN, 10120=ANDRE BANER, 10140=LETBANE]
- enhed: values [2010=Total, km, 2020=Med flere spor, km, 2030=Elektrificeret, km, 2040=Med hastigheds- og togstopkontrol, km, 2050=Med strækningssikringsanlæg. km, 2060=Overskæringer, antal, 2070=Standsningssteder, antal]
- tid: date range 1990-01-01 to 2025-01-01

notes:
- enhed is a measurement selector — MUST filter to exactly one value to avoid nonsensical sums. The 7 enhed values are incompatible units: 2010=Total km, 2020=Multi-track km, 2030=Electrified km, 2040=Safety/stop-control km, 2050=Track signalling km, 2060=Level crossings (antal), 2070=Stops (antal). Summing across enhed mixes km with counts.
- bane is hierarchical — do NOT sum all codes. Top level: 10010 (I ALT) = 10020 (BANEDANMARKS NET) + 10120 (ANDRE BANER) + 10130 (METROEN) + 10140 (LETBANE). Within BANEDANMARKS NET: 10121 (Hovedbaner) + 10122 (Regionalbaner) + 10123 (S-baner) + 10124 (Lokalbaner) + 10125 (Godsbaner).
- Example for 2025 total network (enhed=2010): 2615 km total — Banedanmarks net 1962 km, Andre baner 486 km, Metro 43 km, Letbane 124 km.
- Not all enhed/bane combos available for all years — some enhed values start from 1998 or later. Use enhed=2010 (total km) or enhed=2070 (standsningssteder) for the longest series back to 1990.