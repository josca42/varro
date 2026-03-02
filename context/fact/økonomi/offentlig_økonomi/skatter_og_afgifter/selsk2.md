table: fact.selsk2
description: Skatteydende selskaber mv. efter type, indkomst og skat og tid
measure: indhold (unit -)
columns:
- type: values [101=Aktieselskaber (A/S), 102=Anpartsselskaber (ApS), 103=Finans- og kreditinstitutter, 104=Sparekasser, 105=Brugsforeninger, 106=Andelsforeninger, 107=Gensidige forsikringsforeninger, 108=Udenlandske selskaber eller foreninger, 111=Fonde, 109=Andre foreninger mv., 110=Alle selskaber og foreninger]
- indskat: values [301=Antal selskaber, 302=Skattepligtig indkomst (mio. kr.), 303=Selskabsskat (mio. kr.)]
- tid: date range 1996-01-01 to 2023-01-01

notes:
- indskat has 3 values with completely different units: 301=count (antal), 302=income in mio. kr., 303=tax in mio. kr. Never sum or mix across indskat values — always filter to exactly one per query.
- type=110 (Alle selskaber) = sum of all other type values (same structure as selsk1). For total selskabsskat: WHERE type='110' AND indskat='303'.
- Note: this table covers only skatteydende (tax-paying) selskaber — those with positive skattepligtig indkomst. For counts including non-taxpayers (negative/zero income), use selsk1.
