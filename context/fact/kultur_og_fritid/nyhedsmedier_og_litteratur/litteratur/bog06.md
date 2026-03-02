table: fact.bog06
description: Kommercielt udkomne bøger efter emne, omfang, udgave, medie, originalsprog og tid
measure: indhold (unit Antal)
columns:
- boger: values [100=Bøger i alt, 101=Digte. Antologier, 102=Digte. Værker af enkelte forfattere, 103=Skuespil. Antologier, 104=Skuespil. Værker af enkelte forfattere ... 286=Nordens historie, 287=Danmarks historie, 288=Andre europæiske landes historie, 289=Andre verdensdeles historie, 290=Personalhistorie. Genealogi]
- bogtype: values [610=Bøger mellem 17 og 47 sider, 620=Bøger over 48 sider, 622=Uoplyst]
- udgave: values [630=Alle udgaver, 640=Første udgave, 650=Nye udgaver, 999=Uoplyst]
- medie: values [660=Alle medier, 670=Fysisk bog, 680=E-bog, online, 681=E-bog, cd-rom, 686=Multimedie, online, 684=Multimedie, cd-rom]
- sprog: values [690=Alle sprog, 700=Dansk, 710=Svensk, 720=Norsk, 730=Engelsk/amerikansk, 740=Tysk, 750=Fransk, 760=Andre sprog]
- tid: date range 2009-01-01 to 2024-01-01

notes:
- Scoped to *kommercielt udkomne* (commercially published) books only — not the full book production in bog02.
- boger=100 is "Bøger i alt" (total within commercial scope). Same subject hierarchy as bog02: 101-118 skønlitteratur, 201-290 faglitteratur, no subtotals.
- bogtype has NO aggregate code. SUM across all 3 values (610, 620, 622) for totals — same as bog02.
- udgave=630 ("Alle udgaver") is the aggregate of 640 + 650 + 999. Filter to 630 for totals.
- medie=660 ("Alle medier") is the aggregate of all media codes. Filter to 660 for totals.
- sprog=690 ("Alle sprog") is the aggregate of all original-language codes (700=Dansk, 710=Svensk, 720=Norsk, 730=Engelsk/amerikansk, 740=Tysk, 750=Fransk, 760=Andre).
- Annual data, 2009-2024.