table: fact.ejen99
description: Nøgletal for andelsboligsalg efter område, vurderingsprincip og tid
measure: indhold (unit Pct.)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- vurdering: values [30=Valuarvurdering, 35=Offentlig vurdering, 40=Anskaffelsespris, 50=Uoplyst vurderingsprincip, 55=Indekseret offentlig vurdering]
- tid: date range 2015-01-01 to 2025-04-01
dim docs: /dim/nuts.md

notes:
- `vurdering` is a valuation-principle selector: 30=Valuarvurdering, 35=Offentlig vurdering, 40=Anskaffelsespris, 50=Uoplyst, 55=Indekseret offentlig vurdering. Always filter to one value — omitting this multiplies results 5x.
- `omrade` joins dim.nuts at niveau 1 (regioner), niveau 2 (landsdele), and niveau 3 (kommuner, kode 101+). Two codes don't join: 0 = "Hele landet" (national total) and 95 = "Resten af landet" (hele landet minus Region Hovedstaden) — both are custom aggregates. Filter `d.niveau` when joining to avoid mixing hierarchy levels.
- Deepest geographic breakdown in this subject: goes down to individual kommuner (niveau 3). Use ColumnValues("nuts", "titel", for_table="ejen99") to see which kommuner are covered.
- Values are percentages (Pct.) — nøgletal for andelsbolig sales (price as % of valuation). This is not raw counts or absolute prices; it cannot be summed across omrade.
- Andelsboliger only. For all property types, use ejen77. Quarterly from 2015.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0 and omrade=95.