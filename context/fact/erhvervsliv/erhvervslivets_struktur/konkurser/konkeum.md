table: fact.konkeum
description: Nyregistrerede virksomheder og konkurser efter indikator, branche (DB07) og tid
measure: indhold (unit Antal)
columns:
- indikator: values [BURE=Nyregistrerede virksomheder , BUBA=Konkurser]
- branche07: values [BTSXO_S94=Brancher i alt, BTE=(B+C+D+E) Råstofindvinding + fremstillingsvirksomhed + el-, gas- og fjernvarmeforsyning + vandforsyning, kloakvæsen, affaldshåndtering mv., F=F Bygge og anlæg, G=G Handel, H=H Transport, I=I Hoteller og restauranter, J=J Information og kommunikation, KTN=(K+L+M +N) Pengeinstitut- og finansvirksomhed mv. + fast ejendom + liberale, videnskabelige og tekniske tjenesteydelser + administrative tjenesteydelser og hjælpetjenester, PTSXS94=(P+Q+R+95+96) Undervisning + sundhedsvæsen og sociale foranstaltninger + kultur, forlystelser og sport + reparation af husholdningsudstyr + frisører, vaskerier og andre serviceydelser]
- tid: date range 2009-01-01 to 2025-09-01

notes:
- indikator is a measurement selector: BURE=nyregistrerede virksomheder, BUBA=konkurser. Both series are in the same table. Always filter to one — this table is specifically designed to compare new registrations vs. bankruptcies, but don't sum them.
- branche07 here is an inline code (not dim.db). BTSXO_S94=national total; the remaining 7 codes are broad DB07 sector aggregates. No dim join needed or possible.
- This is the only table combining new company registrations and bankruptcies — useful for net business formation analysis. Use WHERE indikator='BUBA' for bankruptcies, 'BURE' for new registrations.