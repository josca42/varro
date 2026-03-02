table: fact.ivg3
description: International vejgodstransport med farligt gods efter enhed, kørselsart, godsart og tid
measure: indhold (unit -)
columns:
- maengde4: values [70=Pålæsset godsmængde (1000 ton), 80=Transportarbejde (1000 tonkm)]
- korart: values [1000=KØRSEL I ALT, 4000=Fra Danmark, 5000=Til Danmark]
- gods: values [700=FARLIGT GODS I ALT, 710=Eksplosive stoffer og genstande, 720=Komprimerede, flydende eller opløste gasser, 730=Brandfarlige flydende stoffer, 740=Brandfarlige faste stoffer, 750=Selvantændelige stoffer, 760=Stoffer, som ved kontakt med vand afgiver brandfarlige gasser, 770=Oxiderende (brandnærende) stoffer, 780=Organiske peroxyder, 790=Giftige stoffer, 800=Infektionsfremkaldende stoffer, 810=Radioaktive stoffer, 820=Ætsende stoffer, 830=Diverse farlige stoffer og genstande]
- tid: date range 1999-01-01 to 2024-01-01

notes:
- maengde4 is a measurement selector (70=tons, 80=tonkm). Filter to one.
- korart: 1000=KØRSEL I ALT, 4000=Fra Danmark, 5000=Til Danmark. Don't sum 1000 with its children.
- gods: 700=FARLIGT GODS I ALT (total). Categories 710–830 are individual hazard classes summing to 700.
- International dangerous goods only. For national dangerous goods by region use nvg33.