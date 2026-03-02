table: fact.fro
description: Frøproduktion efter afgrøde, enhed og tid
measure: indhold (unit -)
columns:
- afgrode: values [1100=FRØ TIL UDSÆD I ALT, 1105=GRÆSMARKSBÆLGPLANTER I ALT, 1110=Rødkløver, halvsildig, 1115=Hvidkløver, 1120=Humlesneglebælg ... 1185=Almindeligt rapgræs, 1190=Engrapgræs, 1192=Rajsvingel, 1195=Andet græsfrø, 1200=ANDRE PLANTER TIL FRØ]
- maengde4: values [10=Areal (1000 hektar), 20=Gennemsnitsudbytte (hkg pr. hektar), 700=Produktion, tons]
- tid: date range 1989-01-01 to 2024-01-01

notes:
- maengde4 is a measurement selector — 10=Areal (1000 ha), 20=Gennemsnitsudbytte (hkg/ha), 700=Produktion (tons). All three appear for the same afgrode/tid. Always filter to one: e.g. WHERE maengde4=700 for production tonnage.
- afgrode has aggregate codes mixed with specific crops: 1100=FRØ TIL UDSÆD I ALT (grand total), 1105=GRÆSMARKSBÆLGPLANTER I ALT (legume sub-total), 1200=ANDRE PLANTER TIL FRØ (other plants sub-total). The specific species codes (1110-1195) are children of these aggregates. Never sum across all afgrode — pick one level.
- No regional breakdown. National-level data only.