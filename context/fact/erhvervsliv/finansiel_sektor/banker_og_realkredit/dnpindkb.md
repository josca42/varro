table: fact.dnpindkb
description: Indenlandsk indlån i pengeinstitutter efter datatype, branche og tid
measure: indhold (unit Mio. kr.)
columns:
- data: values [ULT=Ultimobalance (mio. kr.), VAL=Valutakursreguleringer (mio. kr.), NET=Nettotransaktioner (mio. kr.), KI=Indeks over nominelle beholdninger (indeks 201501=100)]
- branche: values [ALLE=Alle brancher i alt, AZZ=Landbrug, skovbrug og fiskeri, BZZ=Råstofindvinding, CZZ=Fremstillingsvirksomhed, DZZ=Energiforsyning ... RZZ=Kultur, forlystelser og sport, SZZ=Andre serviceydelser, TZZ=Varer og tjenester til eget brug samt private med ansat medhjælp, UZZ=Internationale organisationer og interesseorganisationer, YZZ=Lønmodtagere, pensionister mv.]
- tid: date range 2013-09-01 to 2025-09-01

notes:
- data is a measurement-type selector: ULT=end-of-period stock (mio. kr.), NET=net transactions, VAL=fx revaluation, KI=index. Filter to data='ULT' for balance amounts.
- branche uses NACE section-level codes (letter+ZZ format): ALLE=all sectors total, AZZ=Landbrug, BZZ=Råstofindvinding, CZZ=Fremstilling, DZZ=Energi, EZZ=Vandforsyning, FZZ=Byggeri, GZZ=Handel, HZZ=Transport, IZZ=Overnatning, JZZ=Information, KZZ=Finansiering, LZZ=Ejendomme, MZZ=Rådgivning, NZZ=Service, OZZ=Off.forvaltning, PZZ=Uddannelse, QZZ=Sundhed, RZZ=Kultur, SZZ=Andre service, TZZ=Privathusholdninger m. ansat, UZZ=Int.org, YZZ=Lønmodtagere/pensionister.
- These letter+ZZ codes do NOT join to dim.db (which has numeric DB07 codes). The dim link is incorrect; treat as inline values.
- For total across all sectors: branche='ALLE'.