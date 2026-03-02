table: fact.nvg1
description: National vejgodstransport efter enhed, kørselsart, vogntype/totalvægt, bilens alder, turlængde og tid
measure: indhold (unit -)
columns:
- enhed: values [10=Ture i alt, 1000, 20=Ture med læs, 1000, 30=Ture uden læs, 1000, 40=Kørte km i alt, 1000 km, 50=Kørte km med læs, 1000 km, 60=Kørte km uden læs, 1000 km, 70=Pålæsset godsmængde (1000 ton), 80=Transportarbejde (1000 tonkm)]
- korart: values [1000=KØRSEL I ALT, 2000=Vognmandskørsel, 3000=Firmakørsel]
- typevaegt: values [0=I ALT, 10=Solovogn, total, 11=Solovogn, 6001 - 12000 kg, 12=Solovogn, 12001 - 18000 kg, 13=Solovogn, 18001 - 24000 kg, 14=Solovogn, større end 24000 kg, 20=Påhængsvogntog, total, 21=Påhængsvogntog, mindre end 40001 kg, 22=Påhængsvogntog, 40001 - 44000 kg, 23=Påhængsvogntog, større end 44000 kg, 30=Sættevognstog, total, 31=Sættevognstog, mindre end 40001 kg, 32=Sættevognstog, 40001 - 44000 kg, 33=Sættevognstog, større end 44000 kg]
- bilalder: values [IALT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år, 5=5 år, 6=6 år, 7=7 år, 8=8 år, 9=9 år, 10OV=10 år eller mere]
- turkm: values [00=Ture i alt, 00-14=Mindre end 15 km, 15-29=15-29 km, 30-49=30-49 km, 50-74=50-74 km, 75-99=75-99 km, 100-124=100-124 km, 125-149=125-149 km, 150-199=150-199 km, 200-249=200-249 km, 250-299=250-299 km, 300OV=300 km eller mere]
- tid: date range 1999-01-01 to 2024-01-01
notes:
- enhed is a measurement selector — every dimension combination repeats once per enhed value. Always filter to one: e.g. enhed='70' (tons) or enhed='80' (tonkm).
- typevaegt has a 2-level hierarchy: 0=I ALT, then 10/20/30 are vehicle-type subtotals, then 11-14/21-23/31-33 are weight subcategories. Only filter to one level. 0=I ALT or one vehicle group (10/20/30) gives clean non-overlapping totals.
- bilalder has IALT=total plus individual years 0–10OV. Filter bilalder='IALT' to get all ages.
- turkm has 00=Ture i alt plus distance bands. Filter turkm='00' to get totals across all distances.
- korart has 1000=KØRSEL I ALT (total), 2000=Vognmandskørsel, 3000=Firmakørsel. These sum: 2000+3000=1000. Never sum 1000 with its children.
- For a simple total: WHERE korart='1000' AND typevaegt='0' AND bilalder='IALT' AND turkm='00' AND enhed='70' gives total national freight tonnage per year.
