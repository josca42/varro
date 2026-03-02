table: fact.inst11
description: Uddannelsesinstitutioner med almengymnasiale uddannelser efter status, institution, uddannelse, herkomst, køn og tid
measure: indhold (unit Antal)
columns:
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- insti: values [TOT=I alt, 101108=101108 Akademisk Studenterkursus, 101115=101115 Rysensteen Gymnasium, 101117=101117 Sankt Annæ Gymnasium, 101118=101118 Christianshavns Gymnasium ... 851060=851060 Aalborg Katedralskole, 851061=851061 Nørresundby Gymnasium og HF, 851062=851062 Hasseris Gymnasium, 851248=851248 HF & VUC NORD, 861013=861013 Vesthimmerlands Gymnasium og HF]
- uddannelse: values [TOT=I alt, H2010=H2010 Alment gymnasiale uddannelser, H201010=H201010 Stx, H201020=H201020 Hf, H201030=H201030 Studenterkursus, H2030=H2030 Internationale gymnasiale uddannelser, H203010=H203010 Pre International Baccalaureate, H203020=H203020 International Baccalaureate, H203030=H203030 Dansk-Tysk studentereksamen, H203040=H203040 Dansk-Fransk Bacalaurétte, H203060=H203060 European Baccalaureate]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus is a measurement selector, not a category — every other dimension combination appears 3 times (once per fstatus). Always filter: fstatus = 'B' for student counts on Oct 1, 'F' for completions, 'T' for new entrants. Omitting this triples all sums.
- uddannelse has 2 hierarchy levels: 5-char parents (H2010=almengymnasiale, H2030=internationale gymnasiale) and 7-char children (H201010=Stx, H201020=Hf, etc.). TOT covers all. When grouping by uddannelse, filter to one level (e.g. WHERE LENGTH(uddannelse) = 7) to avoid double-counting parent and child rows.
- kon total code is '10' (Køn i alt), not 'TOT'. Filter kon = '10' for gender-totals.
- herkomst total is 'TOT'. Individual codes: 5=dansk oprindelse, 4=indvandrere, 3=efterkommere, 0=uoplyst. These sum to TOT.
- insti total is 'TOT'. All other insti values are 6-digit institution codes. Use ColumnValues("inst11", "insti") to search by name.