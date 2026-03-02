table: fact.bog02
description: Udkomne bøger efter emne, omfang, udgave, medie og tid
measure: indhold (unit Antal)
columns:
- boger: values [100=Bøger i alt, 101=Digte. Antologier, 102=Digte. Værker af enkelte forfattere, 103=Skuespil. Antologier, 104=Skuespil. Værker af enkelte forfattere ... 286=Nordens historie, 287=Danmarks historie, 288=Andre europæiske landes historie, 289=Andre verdensdeles historie, 290=Personalhistorie. Genealogi]
- bogtype: values [610=Bøger mellem 17 og 47 sider, 620=Bøger over 48 sider, 622=Uoplyst]
- udgave: values [630=Alle udgaver, 640=Første udgave, 650=Nye udgaver, 999=Uoplyst]
- medie: values [660=Alle medier, 670=Fysisk bog, 680=E-bog, online, 681=E-bog, cd-rom, 686=Multimedie, online, 684=Multimedie, cd-rom]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- boger=100 is "Bøger i alt" (total). 101-118 are skønlitteratur subjects, 201-290 are faglitteratur subjects. There is no skønlitteratur/faglitteratur subtotal code — 100 is the only aggregate.
- bogtype has NO aggregate/total code. The 3 values (610=17-47 sider, 620=over 48 sider, 622=Uoplyst) must be summed manually for a grand total. Always filter or SUM all three explicitly when you want total books.
- udgave=630 ("Alle udgaver") is the aggregate of 640 (første udgave) + 650 (nye udgaver) + 999 (uoplyst). Filter to 630 for totals.
- medie=660 ("Alle medier") is the aggregate of 670 (fysisk bog), 680/681 (e-bog), 684/686 (multimedie). Filter to 660 for totals.
- Annual data, 2007-2024. To get total books published in a year by subject: filter boger to a specific code (or 100 for all), SUM across all bogtype values, udgave=630, medie=660.