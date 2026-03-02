table: fact.kv2ai2
description: Brug af kunstig intelligens efter formål, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- formaaal: values [42900=I min dagligdag til private formål eller til løsning af private opgaver, 42910=Til at skrive jobansøgninger og CV, 42920=I forbindelse med arbejde, 42930=I forbindelse med skole eller uddannelse, 42940=Som hobby eller interesse, 42950=I andre situationer]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- kon='10' = køn i alt; alder='TOT' = alder i alt. Filter to these for national totals.
- formaaal (note: triple 'a' in column name) values are NOT mutually exclusive — AI users can use AI for multiple purposes. Never sum across formaaal values.
- 2024 data only.
