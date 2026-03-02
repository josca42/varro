table: fact.dnrugpi
description: Pengeinstitutternes nye og udestående indenlandske forretninger - Gruppeinddelt efter instrument, instituttype, indenlandsk sektor, valuta, formål og tid
measure: indhold (unit Pct.)
columns:
- instrnat: values [AL00NRENTEUF=Effektiv rentesats (pct.) på udlån i alt - udestående forretninger, AL00ALLERENTENF=Effektiv rentesats (pct.) på udlån i alt - nye forretninger ekskl. kassekreditter (revolverende lån) og overtræk, PL00ALLERENTEUF=Effektiv rentesats (pct.) på indlån i alt - udestående forretninger, PL00ALLERENTENF=Effektiv rentesats (pct.) på indlån i alt - nye forretninger]
- institype: values [ALLE=Pengeinstitutter i alt, 1=- Store pengeinstitutter, 2=- Mellemstore pengeinstitutter]
- indsek: values [1100=1100: Ikke-finansielle selskaber, 1400=1400: Husholdninger, 1410=- 1410: Husholdninger - personligt ejede virksomheder, 1430=- 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=1500: Nonprofitinstitutioner rettet mod husholdninger]
- valuta: values [Z01=Alle valutaer, DKK=- heraf DKK, EUR=- heraf EUR]
- formal: values [ALLE=Alle formål, B=Boligformål for udlån til husholdninger, EXB=Ej boligformål for udlån til husholdninger, F=- Forbrugerkredit for udlån til husholdninger, A=- Andet formål for udlån til husholdninger]
- tid: date range 2003-01-01 to 2025-09-01
notes:
- instrnat encodes both direction (loans vs deposits) and observation type (outstanding vs new) in one code — four independent series that cannot be summed: AL00NRENTEUF=loans outstanding, AL00ALLERENTENF=new loans (excl. kassekreditter), PL00ALLERENTEUF=deposits outstanding, PL00ALLERENTENF=new deposits. Filter to exactly one instrnat.
- institype: ALLE=all banks, 1=store pengeinstitutter, 2=mellemstore pengeinstitutter. ALLE is already a total — don't sum 1+2 to approximate ALLE.
- indsek has no total row. Values: 1100, 1400, 1410, 1430, 1500. Avoid double-counting 1400 with sub-sectors 1410/1430.
- valuta: Z01=all currencies (total), DKK and EUR are subsets. Don't sum across them.
- formal: ALLE=all purposes, B=boligformål, EXB=ej boligformål. formal breakdown is only meaningful for household loans (indsek 1400/1410/1430).
- This table groups banks by size (store/mellemstore). For overall MFI rates without bank-size split, see dnruum (loans) or dnruim (deposits).
