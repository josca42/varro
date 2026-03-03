table: fact.ejjord1
description: Ejerskab af dansk landbrugsjord efter region, enhed, land og tid
measure: indhold (unit -)
columns:
- region: join dim.nuts on region=kode; levels [1]
- tal: values [100=Ejerskab af landbrugsjord (antal), 110=Areal (ha)]
- land: values [0=Lande i alt, 10=Udlandet i alt, 12=EU, 15=Danmark, 20=Tyskland, 25=Nederlandene, 30=Europa uden for EU, 35=Verden udenfor Europa, 40=Asien, 45=Amerika, 50=Afrika og Oceanien, 55=Uoplyst]
- tid: date range 2020-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- tal is a measurement selector — always filter to one value: '100' (antal ejerskaber) or '110' (areal i ha). Never sum across both tal values.
- land hierarchy is non-additive. land=12 (EU) includes Denmark, so it overlaps with land=15 (Danmark). Safe standalone values: land='0' (alle), land='15' (kun danske ejere), land='10' (kun udenlandske ejere). For EU-excluding-Denmark: compute land=12 minus land=15 in SQL. land=0 = land=15 + land=10 + land=55 (Danmark + kendte udenlandske + uoplyst).
- region joins dim.nuts niveau 1 only — the 5 regioner (kode 81–85). Code '0' is the national total and is NOT in dim.nuts (LEFT JOIN returns NULL). To get all-Denmark totals, filter region='0' rather than summing the 5 regions.
- To get Danish-owned land by region (common query): WHERE tal='100' AND land='15' AND region != '0'. Replace land='15' with land='0' to include all owners regardless of origin.
- Map: /geo/regioner.parquet (niveau 1) — merge on region=dim_kode. Exclude region='0'.