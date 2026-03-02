table: fact.skib44
description: International godsomsætning på større danske havne efter havn, retning, land og tid
measure: indhold (unit 1.000 ton)
columns:
- havn: values [0=HAVNE I ALT, 10=Avedøreværkets Havn, 12=Avedøre Råstofhavn, 25=Københavns Havn, 45=Helsingør Havn ... 730=Aalborg Havn, 735=Aalborg Portland Havn, 750=Frederikshavn Havn, 765=Hirtshals Havn, 785=Nordjyllandsværkets Havn]
- ret: values [1184=INDGÅENDE OG UDGÅENDE GODS I ALT, 1186=Indgående gods, 1188=Udgående gods]
- land: join dim.lande_uhv on land=kode [approx]; levels [4]
- tid: date range 2004-01-01 to 2024-01-01
dim docs: /dim/lande_uhv.md
notes:
- land joins dim.lande_uhv at ~76% match rate. The 10 unmatched codes are NOT errors — they are special country-group and aggregate codes used by this table's own classification: IA=I alt (total), EUA=Europa i øvrigt, AC1=Afrika nord, AC2=Afrika vest, AC3=Afrika i øvrigt, E10=Syd og Mellemamerika, E2=Nær- og Mellemøsten, F2=Asien, Z5=Uoplyst land, CS=Serbien og Montenegro (historical). Do NOT use a simple JOIN to dim.lande_uhv — many rows will be dropped. Instead, use ColumnValues("skib44", "land") to get the full land→label mapping and apply it with a CASE or lookup in your query.
- ret: filter to one of 3 values (1184 total, 1186 indgående, 1188 udgående). Never sum across all ret values.
- havn has aggregate code 0=HAVNE I ALT plus 35 individual larger ports (no LANDSDEL aggregate codes, unlike skib421/431).
- This table covers only larger (større) Danish ports. Use skib431 for all ports including smaller ones.
- For country breakdown without port detail use skib50, which has the same land classification plus gods breakdown.
