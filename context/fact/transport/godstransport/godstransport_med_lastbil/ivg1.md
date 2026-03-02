table: fact.ivg1
description: International vejgodstransport efter enhed, vogntype/totalvægt, bilens alder, turlængde og tid
measure: indhold (unit -)
columns:
- maengde4: values [10=Ture i alt, 1000, 20=Ture med læs, 1000, 30=Ture uden læs, 1000, 40=Kørte km i alt, 1000 km, 50=Kørte km med læs, 1000 km, 60=Kørte km uden læs, 1000 km, 70=Pålæsset godsmængde (1000 ton), 80=Transportarbejde (1000 tonkm)]
- typevaegt: values [0=I ALT, 10=Solovogn, total, 11=Solovogn, 6001 - 12000 kg, 12=Solovogn, 12001 - 18000 kg, 13=Solovogn, 18001 - 24000 kg, 14=Solovogn, større end 24000 kg, 20=Påhængsvogntog, total, 21=Påhængsvogntog, mindre end 40001 kg, 22=Påhængsvogntog, 40001 - 44000 kg, 23=Påhængsvogntog, større end 44000 kg, 30=Sættevognstog, total, 31=Sættevognstog, mindre end 40001 kg, 32=Sættevognstog, 40001 - 44000 kg, 33=Sættevognstog, større end 44000 kg]
- bilalder: values [IALT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år, 5=5 år, 6=6 år, 7=7 år, 8=8 år, 9=9 år, 10OV=10 år eller mere]
- turkm: values [00=Ture i alt, 00-49=Mindre end 50 km, 50-99=50-99 km, 100-149=100-149 km, 150-199=150-199 km, 200-249=200-249 km, 250-299=250-299 km, 300-349=300-349 km, 350-399=350-399 km, 400-449=400-449 km, 450-499=450-499 km, 500-599=500-599 km, 600-699=600-699 km, 700-799=700-799 km, 800-899=800-899 km, 900-999=900-999 km, 1000-1499=1000-1499 km, 1500-1999=1500-1999 km, 2000OV=2000 km eller mere]
- tid: date range 1999-01-01 to 2024-01-01

notes:
- maengde4 is a measurement selector (8 options). Filter to one.
- typevaegt has same 2-level hierarchy as nvg1: 0=I ALT, 10/20/30=vehicle type subtotals, 11-14/21-23/31-33=weight subcategories. Filter to one level only.
- bilalder: IALT=total, plus individual years 0–10OV.
- turkm bands are much finer and longer than nvg1: from <50km to 2000km+. 00=Ture i alt aggregates all distances.
- For a simple total: maengde4='70', typevaegt='0', bilalder='IALT', turkm='00'.
- International equivalent of nvg1 for vehicle/age/distance breakdown.