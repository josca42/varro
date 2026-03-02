table: fact.kv2fr2
description: Frivilligt arbejde efter arbejdsområde, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- arbom: values [42980=Idrætsområdet, 42990=Fritid og hobby, 43000=Det sociale område, 43010=Skole og daginstitutioner, 43020=Kulturområdet, 43030=Boligforening, 43040=Lokalsamfundet, 43050=Sundhedsområdet, 43060=Fagforening, 43070=Idébaseret eller politisk forening, 43080=Natur- eller miljøområdet, 43090=Andre arbejdsområder]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- Each arbom row gives the percentage of people who do voluntary work in that area. A person can volunteer in multiple areas, so arbom categories are NOT mutually exclusive — DO NOT sum across arbom values.
- For the national rate per area: filter kon='10' AND alder='TOT'. Single 2024 annual observation.
