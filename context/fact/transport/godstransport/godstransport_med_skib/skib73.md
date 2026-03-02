table: fact.skib73
description: Omsætning af container- og ro-ro-enheder på større danske havne efter retning, lasteenhed, transport enhed og tid
measure: indhold (unit -)
columns:
- ret: values [1184=INDGÅENDE OG UDGÅENDE GODS I ALT, 1186=Indgående gods, 1188=Udgående gods]
- last: values [400=CONTAINERE I ALT, 425=LASTEDE CONTAINERE I ALT, 450=TOMME CONTAINERE I ALT, 475=RO-RO-ENHEDER]
- transport1: values [73=Antal, 1000, 74=1000 TEU (kun containere)]
- tid: date range 2000-01-01 to 2025-04-01
notes:
- transport1 is a unit selector — every ret+last combination appears twice (73=Antal 1000, 74=1000 TEU). Always filter to one unit. Note: 74 (TEU) only makes sense for containers (last=400/425/450), not ro-ro (last=475).
- last has 4 aggregate-level codes only: 400=CONTAINERE I ALT, 425=LASTEDE CONTAINERE I ALT, 450=TOMME CONTAINERE I ALT, 475=RO-RO-ENHEDER. No size breakdown (use skib49 for 20/40/40+ fod split).
- ret: filter to one value (1184 total, 1186 indgående, 1188 udgående).
- No havn dimension — national total for larger ports only. For port-level container/ro-ro data use skib49. Current through 2025.
