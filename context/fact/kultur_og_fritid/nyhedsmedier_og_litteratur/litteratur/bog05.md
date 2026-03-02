table: fact.bog05
description: Bogtitler efter emne, publiceringstype, medie og tid
measure: indhold (unit Antal)
columns:
- boger: values [100=Bøger i alt, 101=Digte. Antologier, 102=Digte. Værker af enkelte forfattere, 103=Skuespil. Antologier, 104=Skuespil. Værker af enkelte forfattere ... 286=Nordens historie, 287=Danmarks historie, 288=Andre europæiske landes historie, 289=Andre verdensdeles historie, 290=Personalhistorie. Genealogi]
- oplag1: values [500=Danske oplag, 510=Danske årsskrifter, 530=Udenlandske årsskrifter, 520=Udenlandske oplag, 540=Udenlandsk kommission bøger nye udgaver]
- medie: values [660=Alle medier, 670=Fysisk bog, 680=E-bog, online, 681=E-bog, cd-rom, 686=Multimedie, online, 684=Multimedie, cd-rom]
- tid: date range 2012-01-01 to 2024-01-01

notes:
- boger=100 is "Bøger i alt" (total). Same subject hierarchy as bog02-04: 101-118 skønlitteratur, 201-290 faglitteratur, no subtotals.
- oplag1 has NO aggregate/total code. The 5 values are mutually exclusive publication types: 500=Danske oplag, 510=Danske årsskrifter, 520=Udenlandske oplag, 530=Udenlandske årsskrifter, 540=Udenlandsk kommission bøger nye udgaver. To get total Danish domestic titles: filter oplag1=500 (or 500+510 if annuals should be included).
- medie=660 ("Alle medier") is the aggregate of all media codes. Filter to 660 for totals.
- Annual data, 2012-2024 (shorter series than bog02-04).