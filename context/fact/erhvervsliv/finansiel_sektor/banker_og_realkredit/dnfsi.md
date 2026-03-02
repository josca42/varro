table: fact.dnfsi
description: Financial Soundness Indikatorer efter indikator og tid
measure: indhold (unit Pct.)
columns:
- indikator: values [FSKRTC_PT=Kapitalgrundlag i forhold til risikovægtede eksponeringer, FSKA_PT=Kernekapital (tier 1) i forhold til aktiver, FSKRTCA_PT=Kapital i forhold til aktiver, FSKNL_PT=Non-performing lån efter nedskrivninger i forhold til kapital, FSANL_PT=Non-performing lån i forhold til udlån før nedskrivninger, FSERA_PT=Aktivernes afkastningsgrad, FSLS_PT=Likvide aktiver i forhold til kortfristede forpligtelser, FSREPRR_PC_CP_A_PT=Boligpriser, enfamilieshuse (år-til-år ændring i procent)]
- tid: date range 2005-01-01 to 2025-04-01

notes:
- Each indikator is an independent financial soundness ratio expressed as a percentage. Never sum or aggregate across indikator values — they measure completely different things (capital ratio, NPL ratio, liquidity, ROA, house prices).
- Simple table: only 2 dimensions (indikator + tid). Just filter to the indicator(s) you want.
- Quarterly/annual frequency depending on the indicator (FSREPRR_PC_CP_A_PT is annual house price growth; others are quarterly banking ratios).
- FSREPRR_PC_CP_A_PT (house prices) is an outlier in this table — it's a real estate price indicator included alongside banking soundness metrics.