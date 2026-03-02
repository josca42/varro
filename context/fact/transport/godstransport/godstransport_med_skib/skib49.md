table: fact.skib49
description: Godsomsætning af container- og ro-ro-gods på større danske havne efter havn, retning, lasteenhed, enhed og tid
measure: indhold (unit -)
columns:
- havn: values [0=HAVNE I ALT, 25=Københavns Havn, 80=Køge Havn, 120=Kalundborg Havn, 315=Rønne Havn, 440=Aabenraa Havn, 515=Esbjerg Havn, 535=Fredericia Havn, 665=Aarhus Havn, 730=Aalborg Havn, 765=Hirtshals Havn]
- ret: values [1184=INDGÅENDE OG UDGÅENDE GODS I ALT, 1186=Indgående gods, 1188=Udgående gods]
- last: values [400=CONTAINERE I ALT, 405=Containere, 20 fod , 410=Containere, mellem 20 og 40 fod, 415=Containere, 40 fod , 420=Containere, over 40 fod, 425=LASTEDE CONTAINERE I ALT, 430=Lastede containere, 20 fod , 435=Lastede containere, mellem 20 og 40 fod, 440=Lastede containere, 40 fod , 445=Lastede containere, over 40 fod, 450=TOMME CONTAINERE I ALT, 455=Tomme containere, 20 fod , 460=Tomme containere, mellem 20 og 40 fod, 465=Tomme containere, 40 fod , 470=Tomme containere, over 40 fod, 475=RO-RO-ENHEDER]
- enhed: values [73=Antal, 1000, 74=1000 TEU (kun containere), 75=1000 ton]
- tid: date range 1997-01-01 to 2024-01-01
notes:
- Two selectors that independently multiply rows: last (container type) and enhed (unit). Every havn+ret+last+tid combination appears 3 times for enhed 73/74/75. Always filter to a single enhed.
- enhed semantics: 73=Antal (count in thousands), 74=1000 TEU (TEU equivalent, containers only), 75=1000 ton. Note: enhed=74 (TEU) does NOT apply to ro-ro (last=475) — those rows will be null or absent for TEU.
- last has aggregate codes: 400=CONTAINERE I ALT (= lastede + tomme), 425=LASTEDE CONTAINERE I ALT, 450=TOMME CONTAINERE I ALT, 475=RO-RO-ENHEDER. Individual sizes: 405/430/455=20 fod, 410/435/460=20-40 fod, 415/440/465=40 fod, 420/445/470=over 40 fod. Filter last to one level to avoid double-counting.
- havn is limited to 10 larger ports + 0=I ALT (no LANDSDEL aggregates in this table).
- For a simpler container/ro-ro overview without port breakdown and with only aggregate last codes, use skib73.
