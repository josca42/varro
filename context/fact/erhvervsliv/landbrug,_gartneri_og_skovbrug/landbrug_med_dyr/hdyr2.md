table: fact.hdyr2
description: Landbrug med dyr efter enhed, besætningsstørrelse og tid
measure: indhold (unit Antal)
columns:
- tal: values [ANTAL=Bedrifter (antal), DYR=Dyr (antal)]
- besaet: values [H1=1 hest, H2=2 heste, H3=3-4 heste, H4=5-9 heste, H5=10-24 heste ... P8=4.000-4.999 pelsdyr, P9=5.000-7.499 pelsdyr, P10=7.500-9.999 pelsdyr, P11=10.000 pelsdyr og derover, P12=Alle bedrifter med pelsdyr]
- tid: date range 2012-01-01 to 2024-01-01

notes:
- tal is a measurement selector (ANTAL=bedrifter, DYR=dyr). Every besaet×tid combination appears for both tal values. Always filter to one.
- besaet has 166 herd-size group codes organized by animal type: H=heste (7 codes), T=tyre og tyrekalve (12), KV=kvier og kviekalve (11), and similarly for svin, søer, slagtesvin, pelsdyr, etc. Each animal type ends with an "Alle bedrifter med X" total code. Never sum across animal type prefix families.
- No geographic breakdown — national only.
- Use this table when you need the herd size distribution (e.g. how many farms have 100+ malkekøer). For geographic breakdown use hdyr07; for farm-size-by-areal use hdyr1.