table: fact.bog04
description: Skolebøger og børnebøger efter emne, bogtype, udgave, medie og tid
measure: indhold (unit Antal)
columns:
- boger: values [100=Bøger i alt, 101=Digte. Antologier, 102=Digte. Værker af enkelte forfattere, 103=Skuespil. Antologier, 104=Skuespil. Værker af enkelte forfattere ... 286=Nordens historie, 287=Danmarks historie, 288=Andre europæiske landes historie, 289=Andre verdensdeles historie, 290=Personalhistorie. Genealogi]
- btype: values [810=Skole- og børnebøger i alt, 820=Skolebøger, 830=Børnebøger]
- udgave: values [630=Alle udgaver, 640=Første udgave, 650=Nye udgaver, 999=Uoplyst]
- medie: values [660=Alle medier, 670=Fysisk bog, 680=E-bog, online, 681=E-bog, cd-rom, 686=Multimedie, online, 684=Multimedie, cd-rom]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- This table is scoped to children's books and school books only. boger=100 ("Bøger i alt") here reflects the total within that scope.
- btype=810 ("Skole- og børnebøger i alt") is the aggregate of 820 (skolebøger) + 830 (børnebøger). Filter to 810 for totals, or 820/830 to compare the two types.
- udgave=630 ("Alle udgaver") is the aggregate of 640 + 650 + 999. Filter to 630 for totals.
- medie=660 ("Alle medier") is the aggregate of all media codes. Filter to 660 for totals.
- Annual data, 2007-2024.