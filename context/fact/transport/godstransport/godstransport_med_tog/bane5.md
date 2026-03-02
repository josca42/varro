table: fact.bane5
description: Jernbanetransport af farligt gods efter transporttype, godsart, enhed og tid
measure: indhold (unit -)
columns:
- transport: values [1000=KØRSEL I ALT, 1500=National kørsel, 1600=International kørsel , 4000=Fra Danmark, 5000=Til Danmark, 8000=Transit kørsel]
- gods: values [700=FARLIGT GODS I ALT, 710=Eksplosive stoffer og genstande, 720=Komprimerede, flydende eller opløste gasser, 730=Brandfarlige flydende stoffer, 740=Brandfarlige faste stoffer, 750=Selvantændelige stoffer, 760=Stoffer, som ved kontakt med vand afgiver brandfarlige gasser, 770=Oxiderende (brandnærende) stoffer, 780=Organiske peroxyder, 790=Giftige stoffer, 800=Infektionsfremkaldende stoffer, 810=Radioaktive stoffer, 820=Ætsende stoffer, 830=Diverse farlige stoffer og genstande]
- maengde4: values [75=1000 ton, 76=Mio. tonkm]
- tid: date range 2004-01-01 to 2024-01-01

notes:
- maengde4 is a measurement selector (same values as enhed in other bane tables): 75=1000 ton, 76=Mio. tonkm. Always filter to one.
- transport: 1000=total, 1500=national, 1600=international, 4000=fra Danmark, 5000=til Danmark, 8000=transit. Same aggregate/detail pattern as other bane tables.
- gods: 700=FARLIGT GODS I ALT is the aggregate. Codes 710–830 are the individual hazard categories (explosives, gases, flammables, etc.). Do not sum all gods values — pick total (700) or specific categories.
- Annual data from 2004. Exclusively for dangerous goods — for total freight use bane1 or bane9a.