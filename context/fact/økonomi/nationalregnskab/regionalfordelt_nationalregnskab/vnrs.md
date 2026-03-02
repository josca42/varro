table: fact.vnrs
description: Versionstabel NRS - Husholdningernes indkomst efter version, område, transaktion, prisenhed og tid
measure: indhold (unit -)
columns:
- version: values [V2024_JUN=Juniversion 2021-2024, V2023_JUN=Juniversion 1993-2023 (Hovedrevision 2024), V2022_SEP=Septemberversion 2020-2022, V2021_SEP=Septemberversion 2019-2021, V2020_SEP=Septemberversion 2018-2020, V2019_SEP=Septemberversion 2017-2019, V2018_NOV=Novemberversion 2016-2018, V2017_NOV=Novemberversion 2015-2017, V2017_MAR=Martsversion 2014-2017, V2016_NOV=Novemberversion 2014-2016, V2015_NOV=Novemberversion 2004-2015 (Datarevision 2016), V2014_NOV=Novemberversion 2012-2014, V2013_NOV=Novemberversion 2011-2013, V2013_SEP=Septemberversion 1966-2013 (Hovedrevision 2014)]
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- transakt: values [B2A3GK=B.2g+B.3g Bruttooverskud af produktionen og blandet indkomst, P51CD=P.51c Forbrug af fast realkapital, B2A3NK=B.2n+B.3n Nettooverskud af produktion og blandet indkomst, D1K=D.1 Modtaget aflønning af ansatte, D4K=D.4 Modtaget formueindkomst, D4D=D.4 Betalt formueindkomst, B5GD=B.5g Primær bruttoindkomst, D62K=D.62 Modtaget sociale ydelser, undtagen sociale overførsler i naturalier, D7K=D.7 Modtaget andre løbende overførsler, D5D=D.5 Betalt løbende indkomst- og formueskatter mv., D61D=D.61 Betalt nettobidrag til sociale ordninger, D7D=D.7 Betalt andre løbende overførsler, B6GD=B.6g Disponibel bruttoindkomst]
- prisenhed: values [V_T=Løbende priser, (mio. kr.), V_C=Pr. indbygger, løbende priser, (1000 kr.)]
- tid: date range 2000-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- version is a critical filter — all 14 versions heavily overlap. Always filter to one version: V2024_JUN. Omitting inflates values by 14x.
- omrade joins dim.nuts but codes 0 and 999 are not in the dim. Exclude for regional analysis. Levels 1 (regioner) and 2 (landsdele).
- prisenhed is a measurement selector (V_T or V_C only — no chain index). Filter to one.
- transakt values are household income account items. Pick the specific transaction needed (B6GD for disponibel bruttoindkomst).
- Prefer nrs for standard analysis. Use vnrs only for vintage revision comparisons.