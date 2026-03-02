table: fact.mreg21
description: Grønne afgifter efter miljøkategori og tid
measure: indhold (unit Mio. kr.)
columns:
- miljokat: values [100=I alt inkl. skat på ressourcerente (1+2+3+4+5), 101=I alt ekskl. skat på ressourcerente (1+2+3+4), 200=1. Forureningsafgifter i alt, 201=1.1 Affald, 202=1.2 Kvælstof ... 502=4.2 Råstofindvinding og -import, 600=5. Skat på ressourcerente , 601=5.1 Kulbrinte skat, 602=5.2 Selskabsskat af kulbrintevirksomhed, 603=5.3 Olierørledningsafgift]
- tid: date range 1995-01-01 to 2024-01-01

notes:
- miljokat is hierarchical: 100 = grand total inkl. skat på ressourcerente, 101 = total ekskl. skat på ressourcerente. Main categories: 200 = Forureningsafgifter, 300 = Energiafgifter, 400 = Transportafgifter, 500 = Ressourceafgifter, 600 = Skat på ressourcerente. Sub-codes (201, 202, etc.) are breakdowns within each main category. Filter to one level — mixing levels in a SUM will double-count.
- Simple national total: WHERE miljokat = '100'. To split into the 5 main tax types: WHERE miljokat IN ('200','300','400','500','600').
- This is the aggregate table (no branche breakdown). For tax revenue by industry, use mrs1.