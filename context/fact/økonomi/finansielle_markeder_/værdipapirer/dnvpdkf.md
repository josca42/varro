table: fact.dnvpdkf
description: Værdipapirstatistik (markedsværdi) efter ISIN_NAVN, investorsektor og tid
measure: indhold (unit Mio. kr.)
columns:
- isninavn: values [1=BSP951331318, 2=CH0018386240, 3=CH0018386968, 7268=CH0236907504, 9910=CH1111227810 ... 10511=SE0009888738, 9051=SE0011452127, 9672=SE0014957049, 9673=SE0014957064, 3039=XS0216009547]
- invsektor: values [0000=0.0.0 Udestående, total, 1000=... 1.0.0 Alle indenlandske sektorer (DK), 1100=...... 1.1.0 Ikke-finansielle selskaber, 1254=...... 1.2.0 MFIer og andre finansielle formidlere, B6510=............ 1.2.1 Nationalbanken og pengeinstitutter ... 1410=......... 1.5.1 Personligt ejede virksomheder, 1430=......... 1.5.2 Lønmodtagere, 1500=......... 1.5.3 NPISHer (non-profit institutioner rettet mod husholdninger), 1ZX0=...... 1.6.0 Ufordelt indenlandsk, 2000=... 2.0.0 Udlandet]
- tid: date range 2005-01-01 to 2025-09-01

notes:
- isninavn is an integer surrogate key mapping to ISIN strings (10,661 unique securities). Use ColumnValues("dnvpdkf", "isninavn", fuzzy_match_str="<partial_isin>") to find specific securities by ISIN code.
- invsektor uses numeric codes — inline coded, not joinable to dim.esa. 0000="Udestående, total" (all investors combined). For investor breakdown, avoid mixing hierarchy levels: 1000=alle indenlandske is a parent of 1100, 1254, etc.
- No vaerdian or data measurement selectors — indhold is always markedsværdi. No overcounting risk from selectors.
- Very high cardinality: not suitable for broad aggregations. Best used when querying a specific ISIN or a small set of securities.