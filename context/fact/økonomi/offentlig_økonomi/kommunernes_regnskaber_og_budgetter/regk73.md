table: fact.regk73
description: Kommunernes forskydninger i likvide aktiver (1000 kr.) efter funktion, gruppering og tid
measure: indhold (unit 1.000 kr.)
columns:
- funktion: values [82200=8.22 Forskydninger i likvide aktiver i alt, 82201=8.22.01 Kontante beholdninger (netto), 82205=8.22.05 Indskud i pengeinstitutter m.v. (netto), 82207=8.22.07 Placerings- og investeringsforeninger, 82208=8.22.08 Realkreditobligationer, 82209=8.22.09 Kommunekreditobligationer, 82210=8.22.10 Statsobligationer m.v., 82211=8.22.11 Likvide aktiver udstedt i udlandet]
- gruppering: values [0=Netto, 1=Tilgang, 2=Afgang]
- tid: date range 2007-01-01 to 2025-04-01

notes:
- National aggregate only — no omrade dimension. Quarterly data (latest 2025-04-01).
- gruppering=0 (Netto) = Tilgang minus Afgang. Not all funktion codes have Tilgang/Afgang separately — some only have Netto (gruppering=0). Never sum gruppering values 0+1+2 for the same funktion; that triples the count.
- funktion=82200 (Forskydninger i likvide aktiver i alt) is the aggregate of all 8.22.xx sub-items. Do not sum 82200 with its components.
- This table shows the period-over-period change in liquid assets. For the stock (balance sheet position) use regk64.
