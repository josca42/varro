table: fact.ligedi12
description: Ligestillingsindikator for bestyrelsesmedlemmer og direktører efter indikator, type, virksomhedsstørrelse og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- type: values [20=Bestyrelse, 30=Direktører]
- virkstr: values [3001=I alt, 3005=Ingen ansatte, 3010=Under 10 årsværk, 3020=10-49 årsværk, 3030=50-249 årsværk, 3040=250 årsværk og derover]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- indhold is a percentage or procentpoint (same as ligedi11). Never sum across indikator. Select one: LA1=mænd pct, LA2=kvinder pct, LA3=forskel.
- type only has 20=Bestyrelse and 30=Direktører — no I alt type.
- virkstr='3001' is the total. Filter to virkstr='3001' unless you need size-class breakdown.