<fact tables>
<table>
id: dnpi
description: Porteføljeinvesteringer - danske porteføljeinvesteringer i udlandet efter datatype, instrument, indenlandsk sektor, valuta, land og tid
columns: data, instrument, indsek, valuta, land, tid (time), indhold (unit Mio. kr.)
tid range: 2005-01-01 to 2025-09-01
</table>
<table>
id: dniip
description: Kapitalbalancen - beholdning af Danmarks aktiver og passiver overfor udlandet efter balance, instrument, indenlandsk sektor, valuta, land, udenlandsk sektor og tid
columns: balanc, instrument, indsek, valuta, land, udsek, tid (time), indhold (unit Mio. kr.)
tid range: 2005-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- For the full Danish international investment position (aktiver vs. passiver across all financial instruments): use dniip. It has alle finansielle poster (direkte investeringer, portefølje, derivater, andre, reserveaktiver) with aktiver/passiver/nettoaktiver breakdown, but only 4 geographic aggregates — no individual country detail.
- For portfolio investments broken down by individual country: use dnpi. It has 10 specific countries + 4 geographic aggregates, and separates beholdninger (stocks) from transaktioner (flows) via the data column.
- Both tables cover 2005–present and share the same indsek sector hierarchy (1000=total, 1100/1200/1300/1400 as sub-sectors, 12FP as sub-component of 1200).
- Both tables require filtering valuta to avoid double-counting: Z01=Alle valutaer is the currency-aggregate total; DKK is a subset.
- dniip: always filter balanc to a single value (A, P, or N) — N is derived and not independent.
- dnpi: always filter data to a single value (1=beholdninger or 2=transaktioner).