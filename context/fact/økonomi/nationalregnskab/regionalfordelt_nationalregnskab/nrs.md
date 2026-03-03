table: fact.nrs
description: Husholdningernes indkomst efter område, transaktion, prisenhed og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- transakt: values [B2A3GK=B.2g+B.3g Bruttooverskud af produktionen og blandet indkomst, P51CD=P.51c Forbrug af fast realkapital, B2A3NK=B.2n+B.3n Nettooverskud af produktion og blandet indkomst, D1K=D.1 Modtaget aflønning af ansatte, D4K=D.4 Modtaget formueindkomst, D4D=D.4 Betalt formueindkomst, B5GD=B.5g Primær bruttoindkomst, D62K=D.62 Modtaget sociale ydelser, undtagen sociale overførsler i naturalier, D7K=D.7 Modtaget andre løbende overførsler, D5D=D.5 Betalt løbende indkomst- og formueskatter mv., D61D=D.61 Betalt nettobidrag til sociale ordninger, D7D=D.7 Betalt andre løbende overførsler, B6GD=B.6g Disponibel bruttoindkomst]
- prisenhed: values [V_T=Løbende priser, (mio. kr.), V_C=Pr. indbygger, løbende priser, (1000 kr.)]
- tid: date range 2000-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts but codes 0 (hele landet) and 999 (ikke regionalfordelt) are NOT in the dim. Exclude both when doing regional analysis.
- omrade uses levels 1 (5 regioner: 81–85) and 2 (11 landsdele: 1–11). Filter WHERE d.niveau=1 or d.niveau=2.
- prisenhed is a measurement selector (V_T or V_C — no volume/chain index available for household income). Always filter to one prisenhed.
- transakt codes follow the household income account: B6GD (disponibel bruttoindkomst) is the bottom-line disposable income. D1K=modtaget aflønning, D62K=sociale ydelser, D5D=betalt skat, etc. These are additive components in the account but do not sum meaningfully without knowing the sign convention (K=modtaget/received, D=betalt/paid). Pick the specific transaction needed.
- Only covers from 2000 (not 1993 like nrhp/nrbb10). No branche breakdown — purely regional household income flows.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade IN (0, 999).