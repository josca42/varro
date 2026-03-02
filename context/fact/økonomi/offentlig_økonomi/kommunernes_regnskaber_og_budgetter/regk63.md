table: fact.regk63
description: Kommunernes finansielle aktiver og passiver efter funktion og tid
measure: indhold (unit 1.000 kr.)
columns:
- funktion: values [92200=9.22.00 Likvide aktiver i alt, 9220811=9.22.08-11 Obligationer (del af likvide aktiver i alt), 92500=9.25.00 Tilgodehavender hos staten, 92800=9.28.00 Kortfristede tilgodehavender i øvrigt, 93200=9.32.00 Langfristede tilgodehavender, 93500=9.35.00 Udlæg vedr. forsyningsvirksomheder, 93800=9.38.00 Aktiver vedr. beløb til opkrævning eller udbetaling for andre, 94200=9.42.00 Aktiver tilhørende fonds, legater m.v., 94500=9.45.00 Passiver tilhørende fonds, legater m.v., 94800=9.48.00 Passiver vedr. beløb til opkrævning eller udbetaling for andre, 95000=9.50.00 Kortfristet gæld til pengeinstitutter, 95100=9.51.00 Kortfristet gæld til staten, 95200=9.52.00 Kortfristet gæld i øvrigt, 95500=9.55.00 Langfristet gæld i alt, AKTIV=Aktiver i alt, PASSIV=Passiver i alt]
- tid: date range 2007-01-01 to 2025-04-01

notes:
- National aggregate only — no omrade dimension. For regional breakdown use regk4.
- Data is quarterly (tid goes to 2025-04-01), not annual like the regnskab tables.
- AKTIV and PASSIV are aggregate totals. funktion=92200 (likvide aktiver i alt) and funktion=95500 (langfristet gæld i alt) are sub-totals within AKTIV/PASSIV. funktion=9220811 (obligationer) is a sub-item of 92200. Do not sum aggregate and component codes together.
- Liability values (9.45.xx passiver, 9.48.xx passiver, 9.50.xx–9.55.xx gæld) are stored as negative numbers. PASSIV aggregate is negative.
- For liquid assets detail use regk64; for long-term debt detail use regk65.
