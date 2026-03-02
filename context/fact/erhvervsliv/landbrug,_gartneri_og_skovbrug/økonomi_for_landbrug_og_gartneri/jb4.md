table: fact.jb4
description: Jordbrugets faste bruttoinvesteringer efter investeringstype, beløb og tid
measure: indhold (unit Mio. kr.)
columns:
- invest: values [0=Bruttoinvesteringer i alt, 810=Driftsbygninger i alt, 820=Kvægstalde, 830=Svinestalde, 840=Andre driftsbygninger, 850=Maskiner og inventar, 860=Plantager og grundforbedring]
- belob: values [1000=Løbende priser (mio. kr.), 1006=Faste priser 2015 (mio. kr.), 1008=Faste priser 2020 (mio. kr.)]
- tid: date range 2010-01-01 to 2024-01-01
notes:
- belob is a measurement selector (3 price bases): 1000=løbende priser, 1006=faste priser 2015, 1008=faste priser 2020. Always filter to ONE belob — every invest/tid combination appears three times.
- invest is hierarchical: 0=Bruttoinvesteringer i alt = 810+820+830+840+850+860. Don't sum all invest rows.
- For real/volume comparisons use 1006 or 1008 (chain-linked); note the two fixed-price bases are not directly comparable across years if both are included.
