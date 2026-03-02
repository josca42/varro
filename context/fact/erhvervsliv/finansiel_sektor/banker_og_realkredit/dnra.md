table: fact.dnra
description: Reserveaktiver - beholdninger overfor udlandet efter datatype, instrument, valuta og tid
measure: indhold (unit Mio. kr.)
columns:
- data: values [1=Beholdninger ]
- instrument: values [600=6.0: Reserveaktiver, 610=6.1: Guld og fordringer på IMF, 620=6.2: Lån og indskud mv., 630=6.3: Værdipapirer i alt, 640=6.4: Finansielle derivater]
- valuta: values [Z01=Alle valutaer, XDD=Valutaer i SDR-kurven (USD, EUR, GBP, JPY, CNY), OTH=Øvrige valutaer og guld]
- tid: date range 2015-01-01 to 2025-08-01

notes:
- Simple table: reserveaktiver (Danmarks Nationalbanks foreign reserves) by instrument and currency group, from 2015.
- data only has one value ('1'=beholdninger) — no selector needed.
- instrument: 600=reserveaktiver i alt (total); 610/620/630/640 are sub-components (gold+IMF, deposits, securities, derivatives). Don't sum sub-components with 600.
- valuta: Z01=alle valutaer (total), XDD=SDR basket currencies (USD+EUR+GBP+JPY+CNY), OTH=other currencies and gold. These 3 values partition the total.
- Unit is mio. kr. (millions). Note: dnintval uses mia. kr. (billions) for the same underlying data — be careful with unit comparisons.
- For total foreign reserves: instrument='600', valuta='Z01'.