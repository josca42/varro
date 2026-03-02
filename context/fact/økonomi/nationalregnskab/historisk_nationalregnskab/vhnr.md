table: fact.vhnr
description: Historiske nationalregnskabstal efter regime, transaktion, prisenhed og tid
measure: indhold (unit -)
columns:
- regime: values [201=NR1945: Nationalregnskabet, gældende fra 1945, til 1948 , 202=NR1948: Nationalregnskabet, gældende fra 1948, til 1951, 203=NR1951: Nationalregnskabet, gældende fra 1951, til 1955, 204=NR1955: Nationalregnskabet, gældende fra 1955, til 1960, 205=NR1960: Nationalregnskabet, gældende fra 1960, til 1962, 206=NR1962: Nationalregnskabet, gældende fra 1962, til 1965, 207=NR1965: Nationalregnskabet, gældende fra 1965, til 1972, 208=NR1972: Nationalregnskabet, gældende fra 1972, til 1978, 209=NR1978: Nationalregnskabet, gældende fra 1978, til 1981, 210=NR1981: Nationalregnskabet, gældende fra 1981, til 1984, 211=NR1984: Nationalregnskabet, gældende fra 1984, til 1995, 212=NR1995: Nationalregnskabet, gældende fra 1995, til 1997, 250=BU1958: Kjeld Bjerke og Niels Ussing: Studier over Danmarks Nationalprodukt, 1958 , 251=SH1983: Svend Aage Hansen: Økonomisk vækst i Danmark, bind II, 1983 , 252=SL2010: Nyeste år fra Kryger Larsen, Larsen og Nilsson, Historisk tidsskrift, 2010 ]
- transakt: values [101=Bruttonationalprodukt (BNP mio. kr.), 102=Bruttonationalindkomst (BNI mio. kr.), 103=Bruttofaktorindkomst (BFI mio. kr.), 104=Nettonationalprodukt (NNP mio. kr.), 105=Nettonationalindkomst (NNI mio. kr.), 106=Nettofaktorindkomst (NFI mio. kr.), 107=Forbrug af fast realkapital (afskrivninger mio. kr.)]
- prisenhed: values [401=Løbende priser, 402=1929-priser, 403=1935-priser, 404=1947-priser, 405=1949-priser, 406=1955-priser, 407=1970-priser, 408=1975-priser, 409=1980-priser, 450=Realvækst, årlig (pct)]
- tid: date range 1870-01-01 to 1992-01-01

notes:
- Every regime has both løbende priser (prisenhed=401) and realvækst pct (prisenhed=450). These are fundamentally different: 401 is in Mio. kr., 450 is an annual growth rate (pct). Never mix or sum across prisenhed values.
- Each regime also has exactly one historical reference price (e.g. 403=1935-priser, 406=1970-priser). The reference price varies by regime — check which prisenhed codes are available for the regime you need.
- The table only contains regimes 201–204, 206–212, 250, 251. Regimes 205, 213–218, and 252 are absent.
- Values differ from hnr1 for overlapping years — this is by design. vhnr preserves the original published figures from each accounting regime; hnr1 is a modern synthetic backcast that applies current methodology throughout.
- Typical query: filter to one regime, one transakt, and one prisenhed to get a single time series. Example: regime=250 (Bjerke/Ussing 1958), transakt=101 (BNP), prisenhed=401 (løbende priser).