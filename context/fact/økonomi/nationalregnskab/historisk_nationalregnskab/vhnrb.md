table: fact.vhnrb
description: Historisk nationalregnskabs middelfolketal efter regime, population og tid
measure: indhold (unit 1.000)
columns:
- regime: values [201=NR1945: Nationalregnskabet, gældende fra 1945, til 1948, 202=NR1948: Nationalregnskabet, gældende fra 1948, til 1951 , 203=NR1951: Nationalregnskabet, gældende fra 1951, til 1955 , 204=NR1955: Nationalregnskabet, gældende fra 1955, til 1960 , 205=NR1960: Nationalregnskabet, gældende fra 1960, til 1962  ... 217=NR2011: Nationalregnskabet, gældende fra 2011, til 2014, 218=NR2014: Nationalregnskabet, gældende fra 2014, til 2016 , 250=BU1958: Kjeld Bjerke og Niels Ussing: Studier over Danmarks Nationalprodukt, 1958 , 251=SH1983: Svend Aage Hansen: Økonomisk vækst i Danmark, bind II, 1983 , 252=SL2010: Nyeste år fra Kryger Larsen, Larsen og Nilsson, Historisk tidsskrift, 2010 ]
- popu: values [EMPM_DC=Samlet antal beskæftigede (antal), EMPM_NC=Beskæftigede med bopæl i Danmark, POP=Gennemsnitsbefolkning]
- tid: date range 1870-01-01 to 2019-01-01

notes:
- Despite the doc listing many regime values, only 3 are actually present: 218 (NR2014, 1966–2019), 250 (BU1958/Bjerke-Ussing, 1870–1952), 251 (SH1983/Svend Aage Hansen, 1903–1975).
- EMPM_NC is not present in this table at all — only POP and EMPM_DC.
- Each (regime, popu) combination is an independent series. Always filter to one regime and one popu.
- For per-capita calculations, pair with vhnr: use the same regime in both tables to stay within a consistent accounting framework.
- Regime 218 (POP, 1966–2019) largely overlaps with hnrb — use hnrb if you want the synthetic unified series; use vhnrb regime=218 if you specifically want the NR2014 population figures.