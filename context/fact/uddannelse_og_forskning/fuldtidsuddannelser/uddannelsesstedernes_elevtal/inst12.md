table: fact.inst12
description: Uddannelsesinstitutioner med erhvervsgymnasiale uddannelser efter status, institution, uddannelse, herkomst, køn og tid
measure: indhold (unit Antal)
columns:
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- insti: values [TOT=I alt, 101401=101401 NEXT Uddannelse København, 101403=101403 Hotel- og Restaurantskolen, 101497=101497 Niels Brock (Copenhagen Business College), 147401=147401 TEC, Technical Education Copenhagen ... 823007=823007 Mariagerfjord Gymnasium, 851401=851401 TECHCOLLEGE, 851402=851402 Aalborg Handelsskole, Hovedafdeling, 861013=861013 Vesthimmerlands Gymnasium og HF, 861403=861403 Erhvervsskolerne Aars]
- uddannelse: values [TOT=I alt, H2020=H2020 Erhvervsrettede gymnasiale uddannelser, H202010=H202010 Hhx 1-årig, H202030=H202030 Hhx 3-årig, H202040=H202040 Htx]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus is a measurement selector — always filter to one value. B=elever pr. 1. oktober, F=fuldført, T=tilgang. Every dimension combination repeats 3 times (one per fstatus); omitting this triples sums.
- uddannelse has 2 hierarchy levels: 5-char parents (H2020=erhvervsrettede gymnasiale) and 7-char children (H202010=Hhx 1-årig, H202030=Hhx 3-årig, H202040=Htx). Filter to one level when grouping.
- kon total code is '10' (Køn i alt), not 'TOT'.
- herkomst total is 'TOT'. Individual codes: 5=dansk oprindelse, 4=indvandrere, 3=efterkommere, 0=uoplyst.
- insti total is 'TOT'. Use ColumnValues("inst12", "insti") to browse institution names.