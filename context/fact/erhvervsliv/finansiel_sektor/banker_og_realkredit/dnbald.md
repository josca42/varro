table: fact.dnbald
description: MFI-sektorens balance, ekskl. Nationalbanken efter disaggregerede balanceposter, datatype, rapporterende institut og tid
measure: indhold (unit Mio. kr.)
columns:
- disaggbalpost: values [A0001000A1Z01ALLE=Aktiver i alt, AK001000A1Z01ALLE=- Kontantbeholdning, AL001000A1Z01ALLE=- Udlån, AL001000A1Z01M1A=- - Udlån med oprindelig løbetid op til og med 1 år, AL001000A1Z01S1A=- - Udlån med oprindelig løbetid over 1 år ... PV001000A1Z012A=- - - Udstedte gældsinstrumenter med oprindelig løbetid over 1 år og op til og med 2 år, PV001000A1Z01S2A=- - - Udstedte gældsinstrumenterr med oprindelig løbetid over 2 år, PD001000A1Z01ALLE=- Derivater (passiver), PE001000A1Z01ALLE=- Kapital og reserver, PA001000A1Z01ALLE=- Andre passiver]
- data: values [ULT=Ultimobalance (mio. kr.), VAESUM=Værdireguleringer (mio. kr.), NET=Nettotransaktioner (mio. kr.)]
- rapinst: values [MFIEXDNALLE=MFI-sektoren i alt ekskl. Nationalbanken - ukonsolideret, MFIEXDNKONSALLE=MFI-sektoren i alt ekskl. Nationalbanken - konsolideret for sektorinterne mellemværender]
- tid: date range 2003-01-01 to 2025-09-01

notes:
- disaggbalpost codes are composite strings encoding instrument+sector+country+currency+maturity. E.g. 'AL001000A1Z01M1A' = loans, all sectors, all countries, all currencies, maturity ≤1 year.
- These are hierarchical: AL001000A1Z01ALLE (total loans) = AL001000A1Z01M1A (≤1yr) + AL001000A1Z01S1A (>1yr). Don't sum parent and child codes.
- data: filter to data='ULT' for balance sheet amounts (VAESUM and NET are adjustment flows).
- rapinst: MFIEXDNKONSALLE=consolidated (preferred), MFIEXDNALLE=unconsolidated. Don't sum both.
- dnbald vs dnbala: dnbald has more disaggregated line items (maturity breakdowns within each instrument type); dnbala has the top-level summary. Use dnbald when you need e.g. loans by maturity.