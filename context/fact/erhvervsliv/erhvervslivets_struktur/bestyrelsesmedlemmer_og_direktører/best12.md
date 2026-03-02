table: fact.best12
description: Bestyrelsesmedlemmer og direktører efter type, virksomhedsstørrelse, køn og tid
measure: indhold (unit Antal)
columns:
- type: values [10=I alt, 20=Bestyrelse, 30=Direktører, 40=Uoplyst]
- virkstr: values [3001=I alt, 3005=Ingen ansatte, 3010=Under 10 årsværk, 3020=10-49 årsværk, 3030=50-249 årsværk, 3040=250 årsværk og derover]
- kon: values [100=Køn i alt, 200=Mænd, 300=Kvinder, 400=Uoplyst køn]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- All columns have total rows: type='10', virkstr='3001', kon='100'. Filter all non-target dimensions to their total to get a single aggregate count.
- virkstr size classes are mutually exclusive and sum to virkstr='3001'. Exclude 3001 when aggregating across size classes.
