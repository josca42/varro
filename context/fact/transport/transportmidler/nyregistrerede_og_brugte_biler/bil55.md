table: fact.bil55
description: Nyregistrerede personbiler efter registreringsform og tid
measure: indhold (unit Antal)
columns:
- regbil: values [4000101002=Personbiler i alt, 4000101107=Tilgang af personbiler i alt, sæsonkorrigeret, 4000101003=Tilgang til husholdningerne, 4000101104=Tilgang til husholdningerne, sæsonkorrigeret, 4000101004=Personbiler i husholdningerne, 40001050002=Privatleasing, 40001050004=Tilgang til erhvervene, 4000101105=Tilgang til erhvervene, sæsonkorrigeret, 40001050006=Erhvervenes køb af personbiler, 40001050008=Erhvervsleasing, 40001050010=Leasingbiler i alt]
- tid: date range 2007-01-01 to 2025-09-01
notes:
- regbil is a measurement selector encoding totals, subcategories, and seasonally-adjusted series. Values are not additive — 4000101002=Personbiler i alt already includes husholdningerne + erhvervene subcategories. Never sum across all regbil codes.
- Seasonally-adjusted codes (4000101107, 4000101104, 4000101105) are paired with raw codes. Filter to one or the other for time-series analysis.
- Leasing breakdown: 40001050010=Leasingbiler i alt = 40001050002 (privatleasing) + 40001050008 (erhvervsleasing). Use this table specifically for leasing vs. direct-ownership split of new personbil registrations.
