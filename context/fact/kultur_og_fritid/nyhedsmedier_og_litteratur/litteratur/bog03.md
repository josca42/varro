table: fact.bog03
description: Bogproduktion efter emne, originalsprog, udgivet på, medie og tid
measure: indhold (unit Antal)
columns:
- boger: values [100=Bøger i alt, 101=Digte. Antologier, 102=Digte. Værker af enkelte forfattere, 103=Skuespil. Antologier, 104=Skuespil. Værker af enkelte forfattere ... 286=Nordens historie, 287=Danmarks historie, 288=Andre europæiske landes historie, 289=Andre verdensdeles historie, 290=Personalhistorie. Genealogi]
- sprog: values [690=Alle sprog, 700=Dansk, 710=Svensk, 720=Norsk, 730=Engelsk/amerikansk, 740=Tysk, 750=Fransk, 760=Andre sprog]
- oversat: values [690=Alle sprog, 700=Dansk, 760=Andre sprog]
- medie: values [660=Alle medier, 670=Fysisk bog, 680=E-bog, online, 681=E-bog, cd-rom, 686=Multimedie, online, 684=Multimedie, cd-rom]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- boger=100 is "Bøger i alt" (total). Same subject hierarchy as bog02: 101-118 skønlitteratur, 201-290 faglitteratur, no intermediate subtotals.
- sprog=690 ("Alle sprog") is the aggregate of all original-language codes. 700=Dansk, 710=Svensk, 720=Norsk, 730=Engelsk/amerikansk, 740=Tysk, 750=Fransk, 760=Andre sprog.
- oversat=690 ("Alle sprog") is the aggregate of 700 (Dansk) + 760 (Andre sprog). Note: "oversat" means the language the book is *published in* (udgivet på), not literally "translated". Filter to oversat=700 for books published in Danish.
- medie=660 ("Alle medier") is the aggregate of all media codes. Filter to 660 for totals.
- Annual data, 2007-2024. To get books published in Danish by subject: boger=subject, sprog=690, oversat=700, medie=660.