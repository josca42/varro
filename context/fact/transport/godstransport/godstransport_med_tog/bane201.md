table: fact.bane201
description: Jernbanetransport af gods efter enhed, transporttype, godsart og tid
measure: indhold (unit -)
columns:
- enhed: values [75=1000 ton, 76=Mio. tonkm]
- transport: values [1000=KØRSEL I ALT, 1500=National kørsel, 1600=International kørsel , 4000=Fra Danmark, 5000=Til Danmark]
- gods: values [100=GODS I ALT, 105=Gods på banestyrelsens net, 840=Landbrugs-, skovbrugs-og fiskeriprodukter, 842=Kul, 845=Malme, grus, sten, sand, ler, salt, asfalt ... 872=Tomme containere og veksellad, 874=Flyttegods, 876=Stykgods, blandet gods, 878=Ukendt godsart, fx i containere, 665=Gods på andre jernbanenet]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- enhed is a measurement selector: 75=1000 ton, 76=Mio. tonkm. Always filter to one — summing both doubles the result.
- transport: same aggregate/detail pattern as bane1. 1000=total; 1500=national; 1600=international (with 4000=fra and 5000=til as sub-breakdown). No transit code in this table.
- gods has two distinct aggregate layers mixed together: 100=GODS I ALT is the grand total; 105=Gods på banestyrelsens net and 665=Gods på andre jernbanenet split by railway operator; the remaining codes (840–878) split by cargo type. Never sum gods across all values — pick either total (100), operator split (105+665), or cargo-type breakdown (840–878 series).
- Annual data from 2008. Use this table when breakdown by cargo type (godsart) is needed.