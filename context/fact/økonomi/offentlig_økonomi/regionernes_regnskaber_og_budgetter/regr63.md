table: fact.regr63
description: Regionernes finansielle aktiver og passiver efter funktion og tid
measure: indhold (unit 1.000 kr.)
columns:
- funktion: values [AKTIV=Aktiver i alt, 61000=6.10.00 Likvide aktiver i alt, 6100811=6.10.08-11 obligationer (del af Likvide aktiver i alt), 61500=6.15.00 Tilgodehavender hos staten , 62800=6.28.00 Kortfristede tilgodehavender i øvrigt, 63200=6.32.00 Langfristede tilgodehavender , 63500=6.35.00 Akkumuleret resultat hovedkonto 2, 63800=6.38.00 Aktiver vedr. beløb til opkrævning eller udbetaling for andre, 64200=6.42.00 Aktiver tilhørende fonds, legater m.v., PASSIV=Passiver i alt, 64500=6.45.00 Passiver tilhørende fonds, legater m.v., 64800=6.48.00 Passiver vedr. beløb til opkrævning eller udbetaling for andre, 65000=6.50.00 Kortfristet gæld til pengeinstitutter , 65100=6.51.00 Kortfristet gæld til staten , 65200=6.52.00 Kortfristet gæld i øvrigt , 65500=6.55.00 Langfristet gæld i alt]
- tid: date range 2007-04-01 to 2025-04-01

notes:
- No region dimension — national totals only (all 5 regions combined).
- Quarterly time series (dates are quarter end: 2007-04-01 = Q1 2007, 2007-07-01 = Q2, etc.).
- funktion includes aggregate codes AKTIV (total assets) and PASSIV (total liabilities) alongside 14 sub-accounts. Use AKTIV/PASSIV for totals; use sub-accounts for breakdowns. Do not sum all funktion rows.
- 6100811 is a special code covering "6.10.08-11 obligationer" (a combined range for bond types).
- For annual balance sheet by region: use regr4. For quarterly national totals: use this table.