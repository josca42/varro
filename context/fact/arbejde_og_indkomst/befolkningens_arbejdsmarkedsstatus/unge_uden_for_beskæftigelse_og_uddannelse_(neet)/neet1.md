table: fact.neet1
description: Befolkningen (16-24 år) efter NEET-status, køn, bopælsområde, socioøkonomisk status og tid
measure: indhold (unit Antal)
columns:
- statusneet: values [0=Aktive og ikke-aktive i alt, 5=Aktive, 10=Ikke-aktive (NEET)]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- bopomr: join dim.nuts on bopomr=kode; levels [1, 2, 3]
- socio: values [TOT=I alt, 05=Selvstændige, 10=Medarbejdende ægtefæller, 15=Lønmodtager med ledelsesarbejde, 20=Lønmodtagere på højeste niveau ... 156=Kursister, 158=Produktionsskoleelever, 160=Udenlandske studerende, 170=Børn og unge (ikke under uddannelse), 175=Øvrige uden for arbejdsstyrken]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- statusneet has 3 values: 0=total, 5=aktive, 10=NEET. Value 0 = 5+10. Always filter to the value you want (e.g. statusneet='10' for NEET counts) — mixing all three triples every row.
- bopomr joins dim.nuts. bopomr='0' is the national total and is NOT in dim.nuts (audit shows it as the only unmatched code). Joining to dim drops those rows. Three hierarchy levels: niveau=1 (5 regioner), niveau=2 (11 landsdele), niveau=3 (99 kommuner). Filter by d.niveau to stay at one geographic level and avoid double-counting across levels.
- Use ColumnValues("nuts", "titel", for_table="neet1") to see the 115 geographic codes available in this table.
- kon: TOT=total, M=mænd, K=kvinder. TOT = M+K.
- socio: 27 values total — TOT plus 26 mutually exclusive socioøkonomisk categories. TOT equals the sum of all individual codes. Filter to socio='TOT' for overall counts, or a specific code for a breakdown.
- To get a clean NEET count: filter statusneet='10', kon='TOT' (or specific gender), socio='TOT' (or specific category), and a single bopomr or d.niveau. Forgetting any total filter inflates the result.
- Sample: NEET by region 2023 → JOIN dim.nuts WHERE d.niveau=1 AND statusneet='10' AND kon='TOT' AND socio='TOT' AND tid='2023-01-01'.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.