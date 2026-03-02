table: fact.dnbala
description: MFI-sektorens balance, ekskl. Nationalbanken efter aggregerede balanceposter, datatype, rapporterende institut og tid
measure: indhold (unit Mio. kr.)
columns:
- aggbalpost: values [A0001000A1Z01ALLE=Aktiver i alt, AK001000A1Z01ALLE=- Kontantbeholdning, AL001000A1Z01ALLE=- Udlån, AV001000A1Z01ALLE=- Beholdning af gældsinstrumenter, AE001000A1Z01ALLE=- Beholdning af aktier og andre kapitalandele, AD001000A1Z01ALLE=- Derivater (aktiver), AA101000A1Z01ALLE=- Anlægsaktiver, AA201000A1Z01ALLE=- Andre aktiver, P0001000A1Z01ALLE=Passiver i alt, PL001000A1Z01ALLE=- Indlån, PV001000A1Z01ALLE=- Udstedte gældsinstrumenter, PD001000A1Z01ALLE=- Derivater (passiver), PE001000A1Z01ALLE=- Kapital og reserver, PA001000A1Z01ALLE=- Andre passiver]
- data: values [ULT=Ultimobalance (mio. kr.), VAESUM=Værdireguleringer (mio. kr.), NET=Nettotransaktioner (mio. kr.)]
- rapinst: values [MFIEXDNALLE=MFI-sektoren i alt ekskl. Nationalbanken - ukonsolideret, MFIEXDNKONSALLE=MFI-sektoren i alt ekskl. Nationalbanken - konsolideret for sektorinterne mellemværender]
- tid: date range 2003-01-01 to 2025-09-01

notes:
- aggbalpost codes are composite: each code encodes instrument, counterpart sector, country, currency, and maturity as a single string (e.g. 'AL001000A1Z01ALLE' = loans, all domestic sectors, all countries, all currencies, all maturities). These are pre-aggregated balance line items — not joinable to separate dimension tables.
- The balance sheet has a logical hierarchy: A0001000A1Z01ALLE=total assets (= sum of AK00+AL00+AV00+AE00+AD00+AA10+AA20); P0001000A1Z01ALLE=total liabilities. Don't sum all aggbalpost values — it would double-count.
- data: ULT=end-of-period stock. VAESUM=valuation changes. NET=net transactions. Filter to data='ULT' for balance sheet amounts.
- rapinst selects consolidation: MFIEXDNKONSALLE=consolidated (netting out intra-MFI positions, preferred for economy-wide analysis); MFIEXDNALLE=unconsolidated. Don't sum both — they're alternative views of the same balance sheet.
- For the consolidated MFI balance sheet total: rapinst='MFIEXDNKONSALLE', data='ULT'.
- dnbala (aggregated) vs dnbald (disaggregated): dnbala has ~14 top-level line items; dnbald breaks them down further by maturity, sector, currency within each instrument type.