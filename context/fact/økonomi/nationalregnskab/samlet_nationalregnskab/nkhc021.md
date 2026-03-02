table: fact.nkhc021
description: Husholdningers forbrug på dansk område (15 grp) efter formål, prisenhed, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- formaaal: values [CPT=I alt, CPA=Fødevarer mv., CPB=Drikkevarer og tobak mv., CPC=Beklædning og fodtøj, CPD=Boligbenyttelse, CPE=Elektricitet, fjernvarme og andet brændsel, CPF=Boligudstyr, husholdningstjenester mv., CPG=Medicin, lægeudgifter o.l., CPH=Køb af køretøjer, CPI=Drift af køretøjer og transporttjenester, CPJ=Information og kommunikation, CPK=Fritid, sport og kultur, CPL=Undervisning, CPM=Restauranter og hoteller, CPN=Forsikring og finansielle tjenester, CPO=Andre varer og tjenester]
- prisenhed: values [V=Løbende priser, LKV=2020-priser, kædede værdier]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01
notes:
- TWO measurement selectors: prisenhed (V/LKV — note LKV not LAN) and saeson (N/Y). Always filter both or counts quadruple.
- Quarterly 15-group household consumption from 1990. Annual equivalent: nahc021 (from 1966). Use saeson='Y' for trend analysis.
- formaaal=CPT is the total — do not sum subcategories if you also include CPT.
