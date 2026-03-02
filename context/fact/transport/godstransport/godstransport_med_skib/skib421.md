table: fact.skib421
description: Godsomsætning på danske havne efter havn, enhed og tid
measure: indhold (unit 1.000 ton)
columns:
- havn: values [0=HAVNE I ALT, 1000=LANDSDEL BYEN KØBENHAVN, 25=Københavns Havn, 2000=LANDSDEL KØBENHAVNS OMEGN, 10=Avedøreværkets Havn ... 790=Skagen Havn, 720=Thisted Havn, 795=Vesterø Havn, 730=Aalborg Havn, 735=Aalborg Portland Havn]
- enhed: values [1000=GODSMÆNGDE I ALT, 1010=FRAGTSKIBSGODS I ALT, 1030=Fragtskibsgods, udenrigs, 1020=Fragtskibsgods, indenrigs, 1040=FÆRGEGODS IALT, 1060=Færgegods, udenrigs, 1050=Færgegods, indenrigs, 1070=INDGÅENDE FRAGTSKIBSGODS I ALT, 1080=Indgående fragtskibsgods fra udland, 1090=Indgående fragtskibsgods fra indland, 1100=UDGÅENDE FRAGTSKIBSGODS IALT, 1110=Udgående fragtskibsgods til udland, 1120=Udgående fragtskibsgods til indland, 1130=INDGÅENDE FÆRGEGODS I ALT, 1140=Indgående  færgegods fra udland, 1150=Indgående  færgegods fra indland, 1160=UDGÅENDE FÆRGEGODS I ALT, 1170=Udgående  færgegods til udland, 1180=Udgående  færgegods til indland]
- tid: date range 2007-01-01 to 2024-01-01
notes:
- enhed is a hierarchical measurement selector — every havn+tid combination appears 19 times. Always filter to a single enhed. Never sum across enhed values.
- enhed hierarchy: 1000=GODSMÆNGDE I ALT (grand total) → 1010=Fragtskibsgods i alt + 1040=Færgegods i alt. Under fragtskibe: 1020 indenrigs, 1030 udenrigs; 1070 indgående i alt → 1080 fra udland + 1090 fra indland; 1100 udgående i alt → 1110 til udland + 1120 til indland. Parallel structure under færger (1130–1180).
- havn mixes aggregate codes with individual ports: 0=HAVNE I ALT, 1000=LANDSDEL BYEN KØBENHAVN, 2000=LANDSDEL KØBENHAVNS OMEGN, etc. are aggregates. Do not sum individual ports along with LANDSDEL rows — use havn='0' for the national total or list only individual port codes. Use ColumnValues("skib421", "havn") to see all codes with labels.
