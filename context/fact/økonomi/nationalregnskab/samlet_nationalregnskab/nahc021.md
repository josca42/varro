table: fact.nahc021
description: Husholdningers forbrug på dansk område (15 grp) efter formål, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- formaaal: values [CPT=I alt, CPA=Fødevarer mv., CPB=Drikkevarer og tobak mv., CPC=Beklædning og fodtøj, CPD=Boligbenyttelse, CPE=Elektricitet, fjernvarme og andet brændsel, CPF=Boligudstyr, husholdningstjenester mv., CPG=Medicin, lægeudgifter o.l., CPH=Køb af køretøjer, CPI=Drift af køretøjer og transporttjenester, CPJ=Information og kommunikation, CPK=Fritid, sport og kultur, CPL=Undervisning, CPM=Restauranter og hoteller, CPN=Forsikring og finansielle tjenester, CPO=Andre varer og tjenester]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2024-01-01
notes:
- prisenhed is a measurement selector: V=løbende priser, LAN=2020-priser (kædede værdier). Filter to one value or row counts double.
- formaaal=CPT is 'I alt' (total across all 14 categories). If you want total household consumption, filter formaaal='CPT' — don't sum the 14 subcategories as CPT is already the sum.
- 15-group COICOP classification annual from 1966. For 44 groups use nahc022; for 73 groups (to 2022 only) use nahc023. Quarterly with saeson: nkhc021.
