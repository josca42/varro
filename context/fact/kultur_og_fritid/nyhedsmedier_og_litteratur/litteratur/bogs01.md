table: fact.bogs01
description: Solgte bøger efter genre, format og tid
measure: indhold (unit Antal)
columns:
- genre: values [1000=Genre i alt, 1010=Børne- og ungelitteratur i alt, 1020=Bøger for de helt små, billedbøger, aktivitetsbøger mv., 1030=Fagbøger til børn og unge, 1040=Skønlitteratur for børn og unge ... 1240=Krimier, thrillere og spændingsromaner, 1250=Romantik og erotik, 1260=Science fiction, fantasy o.l., 1270=Skønlitteratur, øvrige, 1280=Uoplyst genre]
- format: values [1380=Formater i alt, 1390=Fysiske bøger i alt, 1400=Indbundet, hardback eller hæftet, 1410=Paperback og pocketbøger, 1420=Andet fysisk format (fx papbøger, spiralryg, anledningsalbums mv.), 1430=Uoplyst fysisk format, 1440=Digitalt format i alt, 1450=E-bøger, 1460=Lydbøger]
- tid: date range 2022-07-01 to 2024-04-01

notes:
- Tracks book SALES (not publications). Quarterly data from 2022 Q3.
- genre has a 3-level hierarchy — never sum across all codes. Level 0: 1000=Genre i alt. Level 1 subtotals: 1010=Børne- og ungelitteratur i alt, 1070=Faglitteratur i alt, 1200=Skønlitteratur i alt, 1280=Uoplyst. Level 2 leaf codes: 1020-1060 under 1010, 1080-1190 under 1070, 1210-1270 under 1200. Pick one level.
- format has a 3-level hierarchy — same rule. Level 0: 1380=Formater i alt. Level 1: 1390=Fysiske bøger i alt, 1440=Digitalt format i alt. Level 2: 1400-1430 under 1390, 1450-1460 under 1440.
- For a simple total: genre=1000, format=1380. To compare physical vs digital: genre=1000, format IN (1390, 1440). To see genre breakdown: genre IN (1010,1070,1200,1280), format=1380.