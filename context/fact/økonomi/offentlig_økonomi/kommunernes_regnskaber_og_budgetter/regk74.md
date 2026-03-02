table: fact.regk74
description: Kommunernes langfristede låntagning (1000 kr.) efter funktion, dranst og tid
measure: indhold (unit 1.000 kr.)
columns:
- funktion: values [85500=8.55 Forskydninger i langfristet gæld, 85563=8.55.63 Selvejende institutioner med overenskomst, 85564=8.55.64 Stat og hypotekbank, 85565=8.55.65 Andre kommuner og regioner, 85566=8.55.66 Kommunernes Pensionsforsikring, 85567=8.55.67 Andre forsikringsselskaber, 85568=8.55.68 Realkredit, 85570=8.55.70 Kommunekredit, 85571=8.55.71 Pengeinstitutter, 85572=8.55.72 Gæld vedrørende klimatilpasningsprojekter, 85573=8.55.73 Lønmodtagernes Feriemidler, 85574=8.55.74 Offentligt emitterede obligationer i udland, 85575=8.55.75 Anden langfristet gæld med indenlandsk kreditor, 85576=8.55.76 Anden langfristet gæld med udenlandsk kreditor, 85577=8.55.77 Langfristet gæld vedrørende ældreboliger, 85578=8.55.78 Gæld vedrørende færgeinvesteringer, 85579=8.55.79 Gæld vedrørende finansielt leasede aktiver (frivillig)]
- dranst: values [0=Netto, 6=Afdrag på lån, 7=Finansiering]
- tid: date range 2007-01-01 to 2025-04-01

notes:
- National aggregate only — no omrade dimension. Quarterly data (latest 2025-04-01).
- dranst=0 (Netto) = dranst=7 (Finansiering/nye lån) + dranst=6 (Afdrag på lån, stored as negative). Verified: netto = finansiering + afdrag. Do not sum dranst=0 with dranst=6 or 7.
- funktion=85500 (Forskydninger i langfristet gæld) is the aggregate of all 8.55.xx sub-items. Do not sum 85500 with its components.
- This table shows the period flow (new borrowing and repayments). For the stock (balance sheet position of long-term debt) use regk65.
