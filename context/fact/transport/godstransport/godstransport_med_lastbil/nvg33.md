table: fact.nvg33
description: National vejgodstransport med farligt gods efter enhed, pålæsningsregion, aflæsningsregion, godsart og tid
measure: indhold (unit -)
columns:
- enhed: values [20=Ture med læs, 1000, 50=Kørte km med læs, 1000 km, 70=Pålæsset godsmængde (1000 ton), 80=Transportarbejde (1000 tonkm)]
- paregion: join dim.nuts on paregion=kode; levels [2]
- afregion: join dim.nuts on afregion=kode; levels [2]
- gods: values [700=FARLIGT GODS I ALT, 710=Eksplosive stoffer og genstande, 720=Komprimerede, flydende eller opløste gasser, 730=Brandfarlige flydende stoffer, 740=Brandfarlige faste stoffer, 750=Selvantændelige stoffer, 760=Stoffer, som ved kontakt med vand afgiver brandfarlige gasser, 770=Oxiderende (brandnærende) stoffer, 780=Organiske peroxyder, 790=Giftige stoffer, 800=Infektionsfremkaldende stoffer, 810=Radioaktive stoffer, 820=Ætsende stoffer, 830=Diverse farlige stoffer og genstande]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- paregion and afregion join dim.nuts at niveau 2 only (11 landsdele), same as nvg23. Code 0 = total all regions, not in dim.nuts.
- enhed is a measurement selector — filter to one value. Only 4 enhed options here (20/50/70/80); trip totals (10/30/40/60) are absent.
- gods: 700=FARLIGT GODS I ALT (total dangerous goods). Individual hazard classes 710–830 sum to 700. Never sum 700 with its subcategories.
- This table only covers dangerous goods. For all goods between regions use nvg23.
- Map: context/geo/landsdele.parquet (niveau 2) — merge on paregion=dim_kode or afregion=dim_kode. Exclude code 0. OD table; aggregate by one dimension for choropleth.