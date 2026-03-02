table: fact.nahc011
description: Individuelt forbrugsudgift efter forbrugsart, formål, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- forbrugsart: values [P31S14=Husholdningernes forbrugsudgifter, P31S15=Forbrugsudgifter i Non-profit institutioner rettet mod husholdninger (NPISH), P31S1M=Privatforbrug, P31S13=Offentlige individuelle forbrugsudgifter, P41=Faktisk individuelt forbrug]
- formaaal: values [CPT=I alt, CPA=Fødevarer mv., CPB=Drikkevarer og tobak mv., CPC=Beklædning og fodtøj, CPD=Boligbenyttelse, CPE=Elektricitet, fjernvarme og andet brændsel, CPF=Boligudstyr, husholdningstjenester mv., CPG=Medicin, lægeudgifter o.l., CPH=Køb af køretøjer, CPI=Drift af køretøjer og transporttjenester, CPJ=Information og kommunikation, CPK=Fritid, sport og kultur, CPL=Undervisning, CPM=Restauranter og hoteller, CPN=Forsikring og finansielle tjenester, CPO=Andre varer og tjenester]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1995-01-01 to 2022-01-01
notes:
- prisenhed is a measurement selector (V/LAN) — filter to one value or row counts double.
- forbrugsart is a classification by who does the spending: P31S14=husholdninger, P31S15=NPISH, P31S1M=privatforbrug (=S14+S15), P31S13=offentlige individuelle udgifter, P41=faktisk individuelt forbrug (=S14+S15+S13). P41 is the broadest total. Do not sum all forbrugsart values.
- formaaal=CPT is the COICOP total (sum of all 14 purposes). The table covers individual consumption only (not collective). Annual from 1995 only.
