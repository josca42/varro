table: fact.silc1a
description: Økonomisk sårbare: Andel personer efter afsavnsmål, køn og alder og tid
measure: indhold (unit Pct.)
columns:
- afsavn: values [A0=Økonomisk sårbare (mindst 3 af 5 afsavnsmål), A1=1. Svært/meget svært at få pengene til at slå til, A2=2. Ubetalte regninger det seneste år, A3=3. Kan ikke betale uforudset udgift på 10.000 kr., A4=4. Har af økonomiske grunde ingen bil, A5=5. Har ikke råd til en uges årlig ferie væk fra hjemmet]
- koal: values [1000=Køn og alder i alt, 1010=Mænd, 1020=Kvinder, 1030=Under 20 år, 1040=20-39 år, 1050=40-64 år, 1060=65 år og derover]
- tid: date range 2011-01-01 to 2024-01-01
notes:
- Simplest and longest-running economic vulnerability table (2011–2024). Values are percentages only — no enhed selector, no overcounting risk.
- koal combines gender and age in one column: 1000=total, 1010=Mænd, 1020=Kvinder, 1030=Under 20 år, 1040=20-39 år, 1050=40-64 år, 1060=65+. Cannot cross gender by age here — use silc10 for richer breakdowns.
- afsavn: A0 is the composite indicator (≥3 of 5 deprivations). A1–A5 are independent individual items. Never sum across them.
- For trend analysis of overall economic vulnerability: WHERE afsavn='A0' AND koal='1000'. One row per year back to 2011.
