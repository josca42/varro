table: fact.bil5
description: Nyregistrerede motorkøretøjer efter køretøjstype og tid
measure: indhold (unit Antal)
columns:
- biltype: values [4000100001=Køretøjer i alt, 4000101002=Personbiler i alt, 4000101103=Personbiler i alt, sæsonkorrigeret, 4000101004=Personbiler i husholdningerne, 4000101106=Personbiler i husholdningerne, sæsonkorrigeret, 4000101005=Personbiler i erhverv, 4000101109=Personbiler i erhvervene, sæsonkorrigeret, 4000104001=Busser i alt, 4000102001=Vare- og lastbiler i alt, 4000102010=Varebiler, totalvægt 0-2.000 kg, 4000102020=Varebiler, totalvægt 2.001-3.000 kg, 4000102030=Varebiler, totalvægt 3.001-3.500 kg, 4000102040=Lastbiler, totalvægt over 3.500 kg, 4000106001=Motorcykler i alt, 4000000017=Knallert-30 i alt, 4000000016=Knallert-45 i alt, 4000103001=Campingvogne i alt]
- tid: date range 1992-01-01 to 2025-09-01

notes:
- biltype mixes regular and seasonally-adjusted series in the same column. Codes 4000101103, 4000101106, 4000101109 are the sæsonkorrigeret versions of 4000101002, 4000101004, 4000101005. Never sum across all biltype values — pick either raw or adjusted.
- 4000100001=Køretøjer i alt is the national total across all vehicle types. Filter to a single biltype for any time-series query.
- Hierarchy within biltype: 4000100001 → 4000101002 (personbiler) → 4000101004 (husholdninger) + 4000101005 (erhverv). Summing parent + children for the same tid will double/triple-count.
- No other dimensions beyond biltype × tid — queries are simple once you pick the right biltype code.