table: fact.van5m
description: Asylansøgninger efter statsborgerskab, asyltype og tid
measure: indhold (unit Antal)
columns:
- statsb: values [5122=Albanien, 5124=Andorra, 5706=Belarus, 5126=Belgien, 5754=Bosnien-Hercegovina ... 5275=Vanuatu, 5532=Østtimor, 5599=Øer i Stillehavet, 5103=Statsløs, 5999=Uoplyst]
- asyltype: values [BRU=Bruttoansøgertallet, SPO=Registreringstallet, UDL=Fra udlandet]
- tid: date range 2014-01-01 to 2025-09-01

notes:
- asyltype is a counting-method selector — ALWAYS filter to one value. BRU=Bruttoansøgertallet (broadest count, includes duplicates), SPO=Registreringstallet (official count for statistics). Summing across asyltype gives nonsense. Note: UDL=Fra udlandet is in the metadata but has no rows in the database.
- statsb has no total code — SUM across all statsb values to get the national asylum application count.
- tid is monthly. This table goes back to 2014.
- For gender/age breakdown of asylum applications use van5rkam (which is exclusively SPO/registreringstallet).