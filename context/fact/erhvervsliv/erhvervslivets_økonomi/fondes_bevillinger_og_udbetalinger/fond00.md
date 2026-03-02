table: fact.fond00
description: Bevilligede fondsmidler efter fondstype, bevillingsniveau, nøgletal og tid
measure: indhold (unit -)
columns:
- fondstype: values [1000=Alle fonde, 1005=Erhvervsdrivende fonde, 1010=Almene fonde og fondslignende foreninger]
- bevilling2: values [2100=50 mio. kr. og derover, 2105=10.0-49.9 mio. kr., 2110=Under 10 mio. kr. , 2115=0 kr. ]
- aktp: values [1103=Fonde (antal), 1105=Bevilgede midler (mio. kr.), 1110=Udbetalte midler (mio. kr.)]
- tid: date range 2016-01-01 to 2023-01-01

notes:
- aktp is a measurement selector — always filter to one value: 1103=antal fonde, 1105=bevilgede midler (mio. kr.), 1110=udbetalte midler (mio. kr.). Forgetting this triples row counts and mixes counts with amounts.
- fondstype=1000 is the aggregate total of 1005+1010. Filter to 1005 or 1010 when comparing fund types; use 1000 for an overall figure only.
- bevilling2 has no total row — all four size brackets are leaf values and can be summed freely.
- This is the only table with bevilling2 (grant size bracket). Use it for "how much comes from large vs. small grants" questions.