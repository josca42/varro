table: fact.skovrg03
description: Skovareal (Kyoto) (fysisk balance) efter balanceposter, region og tid
measure: indhold (unit Km2)
columns:
- balpost: values [FS1=Beholdningen (primo), FS10=Skovrejsning, FS11=Afskovning, FS8=Beholdningen (ultimo), SK3=Ændring (netto)]
- regi07: join dim.nuts on regi07=kode; levels [1]
- tid: date range 1990-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- regi07 joins dim.nuts niveau 1 (5 regioner: 81–85). Code 0 = national total, not in dim.nuts (left join returns NULL for regi07=0). Use WHERE regi07='0' for the national figure, or LEFT JOIN and handle NULL.
- balpost mixes stock and flow types: FS1 (primo) and FS8 (ultimo) are area stocks in km2; FS10 (skovrejsning) and FS11 (afskovning) are annual flows; SK3 (ændring netto) = FS10 - FS11. Never sum stocks and flows together.
- FS1/FS8 rows exist for almost all years; FS10/FS11/SK3 only appear for years where changes were recorded (fewer rows). Safe to query primo/ultimo across the full 1990–2024 range.
- Covers Kyoto-definition forest only. No breakdown below region level.
- Map: /geo/regioner.parquet (niveau 1) — merge on regi07=dim_kode. Exclude regi07=0.