table: fact.nvg41
description: National vejgodstransport efter enhed, lasttype, godsart og tid
measure: indhold (unit -)
columns:
- enhed: values [20=Ture med læs, 1000, 50=Kørte km med læs, 1000 km, 70=Pålæsset godsmængde (1000 ton), 80=Transportarbejde (1000 tonkm)]
- lasttype: values [0=I ALT, 40=Container/veksellad, 45=Anden lasttype]
- gods: values [100=GODS I ALT, 840=Landbrugs-, skovbrugs-og fiskeriprodukter, 842=Kul, 844=Malme,jern og andet metal, 846=Grus, sten, sand, ler, salt, asfalt ... 870=Brev-og pakkepost, 872=Tomme containere og veksellad, 874=Flyttegods, 876=Stykgods, blandet gods, 878=Ukendt godsart, fx i containere]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- enhed is a measurement selector (20/50/70/80). Filter to one value.
- lasttype: 0=I ALT, 40=Container/veksellad, 45=Anden lasttype. Code 0 is the total of 40+45. Don't sum 0 with its children.
- gods: 100=I ALT is the aggregate. Individual goods codes (840–878) sum to code 100. The goods classification here (NST-2000, codes 840+) is a different scheme from nvg121 (codes 115–155).
- For load-type split of total freight: WHERE lasttype IN ('40','45') AND gods='100' AND enhed='70'.