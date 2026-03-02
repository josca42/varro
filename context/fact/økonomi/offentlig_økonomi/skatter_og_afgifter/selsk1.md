table: fact.selsk1
description: Selskaber mv. efter type, skattepligtig indkomst og tid
measure: indhold (unit Antal)
columns:
- type: values [101=Aktieselskaber (A/S), 102=Anpartsselskaber (ApS), 103=Finans- og kreditinstitutter, 104=Sparekasser, 105=Brugsforeninger, 106=Andelsforeninger, 107=Gensidige forsikringsforeninger, 108=Udenlandske selskaber eller foreninger, 111=Fonde, 109=Andre foreninger mv., 110=Alle selskaber og foreninger]
- skat: values [201=Negativ indkomst, 202=0-indkomst (0-99 kr.), 203=Positiv indkomst (over 99 kr.), 204=Selskaber mv. i alt]
- tid: date range 1996-01-01 to 2023-01-01

notes:
- type=110 (Alle selskaber og foreninger) = sum of all other type values (verified). skat=204 (Selskaber mv. i alt) = sum of 201+202+203 (verified). For total count of all companies: WHERE type='110' AND skat='204'.
- To break down by company type (keeping totals): WHERE skat='204' AND type != '110'. To see income distribution (all companies): WHERE type='110' AND skat != '204'.
- indhold is a count (Antal selskaber). This table only counts companies; for income and tax amounts see selsk2.
