table: fact.nglk
description: Udvalgte kommunale regnskabstal efter område, nøgletal, brutto-/nettoudgifter, prisenhed og tid
measure: indhold (unit Kr.)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- bnogle: values [DRI=Kommunale driftsudgifter pr. indbygger, ÆLD=Ældreudgifter pr. ældre, FOL=Folkeskoleudgifter pr. folkeskoleelev, DAG=Dagtilbudsudgifter pr. 0-10 årig, SUN=Sundhedsudgifter pr. indbygger, KUL=Kulturudgifter pr. indbygger, TRA=Transport- og infrastrukturudgifter pr. indbygger, ARB=Arbejdsmarkedsforanstaltningsudgifter pr. 16-64 årig, UDL=Udlignings- og tilskudsbeløb pr. indbygger, LAN=Langfristet gæld pr. indbygger, SER=Serviceudgifter pr. indbygger, ANL=Anlægsudgifter pr. indbygger]
- brutnetudg: values [NET=Nettoudgifter, BRUT=Bruttoudgifter]
- prisenhed: values [AARPRIS=Løbende priser, 08PRIS=Faste priser]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts on omrade=kode. niveau=1 gives 5 regioner, niveau=3 gives kommuner. omrade=0 = "Hele landet" (national aggregate — not in dim.nuts, query directly without join). Use ColumnValues("nuts", "titel", for_table="nglk") to see available codes.
- All 12 bnogle values are independent per-capita key figures with different denominators (DRI=pr. indbygger, ÆLD=pr. ældre, FOL=pr. folkeskoleelev, etc.). Do not sum across bnogle — they measure different things.
- brutnetudg is a measurement selector that doubles rows: NET=nettoudgifter, BRUT=bruttoudgifter. Always filter to one.
- prisenhed is a second measurement selector: AARPRIS=løbende priser, 08PRIS=faste 2008-priser. Always filter to one.
- Correct query requires four filters: bnogle, prisenhed, brutnetudg, and omrade level. Example — DRI by kommune 2023: SELECT omrade, indhold FROM fact.nglk JOIN dim.nuts ON omrade=kode AND niveau=3 WHERE bnogle='DRI' AND prisenhed='AARPRIS' AND brutnetudg='NET' AND tid='2023-01-01'.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
