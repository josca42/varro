table: fact.ivg41
description: International vejgodstransport efter enhed, kørselsart, lasttype, godsart og tid
measure: indhold (unit -)
columns:
- maengde4: values [70=Pålæsset godsmængde (1000 ton), 80=Transportarbejde (1000 tonkm)]
- korart: values [1000=KØRSEL I ALT, 4000=Fra Danmark, 5000=Til Danmark, 6000=Tredjelandskørsel, 7000=Cabotagekørsel]
- lasttype: values [0=I ALT, 40=Container/veksellad, 45=Anden lasttype]
- gods: values [100=GODS I ALT, 840=Landbrugs-, skovbrugs-og fiskeriprodukter, 842=Kul, 844=Malme,jern og andet metal, 846=Grus, sten, sand, ler, salt, asfalt ... 870=Brev-og pakkepost, 872=Tomme containere og veksellad, 874=Flyttegods, 876=Stykgods, blandet gods, 878=Ukendt godsart, fx i containere]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- maengde4 is a measurement selector (70=tons, 80=tonkm). Filter to one value.
- korart=1000 (KØRSEL I ALT) is the aggregate of 4000+5000+6000+7000. Don't sum 1000 with its children.
- lasttype: 0=I ALT, 40=Container, 45=Anden lasttype. Code 0 = 40+45 total.
- gods: 100=GODS I ALT is the aggregate. Individual codes (840–878) sum to 100. Same NST-2000 goods classification as nvg41.
- International equivalent of nvg41 with the same lasttype and goods structure.