table: fact.skib16
description: Danske skibe i udenlansk register efter flagstat, enhed og tid
measure: indhold (unit -)
columns:
- flag: join dim.lande_uhv on flag=kode [approx]; levels [4]
- enhed: values [6000=Skibe (antal), 6500=Bruttotonnage (BT)]
- tid: date range 2017-01-01 to 2025-01-01
dim docs: /dim/lande_uhv.md

notes:
- flag joins dim.lande_uhv (both varchar). Only niveau 4 (individual countries, 250 codes) is present in the dim table.
- flag='TOT' (total across all flag states) and flag='IM' (Isle of Man) are not in dim.lande_uhv. Use WHERE flag='TOT' for totals without joining the dim table. IM is a British Crown dependency missing from the country list.
- enhed is a unit selector: 6000=Skibe (antal), 6500=Bruttotonnage (BT). Always filter to one enhed.
- Covers only Danish ships in foreign registers (2017–2025). Covers same ships as skib15 but broken down by flag state.