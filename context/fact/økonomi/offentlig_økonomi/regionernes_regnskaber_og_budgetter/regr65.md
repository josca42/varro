table: fact.regr65
description: Regionernes langfristede gæld (1000 kr.) efter funktion og tid
measure: indhold (unit 1.000 kr.)
columns:
- funktion: values [65500=6.55.00 Langfristet gæld i alt, 65563=6.55.63 Selvejende institutioner med driftsoverenskomst, 65564=6.55.64 Stat og hypotekbank, 65565=6.55.65 Kommuner og andre regioner, 65566=6.55.66 Kommunernes Pensionsforsikring, 65567=6.55.67 Andre forsikringsselskaber, 65568=6.55.68 Realkredit, 65570=6.55.70 Kommunekredit, 65571=6.55.71 Pengeinstitutter, 65573=6.55.73 Lønmodtagernes Feriemidler , 65574=6.55.74 Offentlige emitterede obligationer i udland, 65575=6.55.75 Anden langfristet gæld med indenlandsk kreditor, 65576=6.55.76 Anden langfristet gæld med udenlandsk kreditor, 65577=6.55.77 Langfristet gæld vedrørende ældreboliger, 65578=6.55.78 Gæld vedr. kvalitetsfondsinvesteringer, 65579=6.55.79 Gæld vedrørende finansielt leasede aktiver]
- tid: date range 2007-04-01 to 2025-04-01

notes:
- No region dimension — national totals only.
- Quarterly time series (same quarter encoding as regr63/regr64).
- funktion 65500 = Langfristet gæld i alt (total). Sub-codes 65563-65579 are types of long-term debt by creditor (Kommunekredit, pengeinstitutter, realkredit, kvalitetsfondsinvesteringer, etc.). Do not sum all funktion rows — 65500 is already the aggregate.
- Subset of regr63 (65500 group). Use regr63 to compare long-term debt alongside total assets/liabilities.