table: fact.ifatsf20
description: Udenlandsk ejede firmaer efter lande, enhed og tid
measure: indhold (unit -)
columns:
- lande: join dim.lande_uhv on lande=kode [approx]; levels [4]
- enhed: values [ANTFIR=Firmaer (antal), XOM=Omsætning (mio. kr.), VAERK=Antal ansatte (årsværk)]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/lande_uhv.md

notes:
- lande only partially joins dim.lande_uhv: 5 of 9 codes match (DE, NL, NO, SE, US — all niveau 4/individual countries). The other 4 don't join.
- EU27 (2019 only) and EU27UK (2020–2023) are aggregate categories covering "remaining EU/UK countries." They represent the same concept under different names — EU27 was renamed EU27UK after Brexit. UK is always listed separately.
- UK uses code "UK" in the fact table, but dim.lande_uhv uses "GB" for Storbritannien — no dim join for UK.
- U1 = all other countries (catch-all).
- The 9 lande codes are mutually exclusive — they add up to the total with no separate total row. Use ColumnValues("ifatsf20", "lande") to see all values; do not rely on dim.lande_uhv to enumerate available countries.
- enhed is a measurement-type selector: ANTFIR (firm count), XOM (revenue mio. DKK), VAERK (FTE). Always filter to one value.
- For queries about specific countries, use the raw lande codes directly (e.g. lande='DE'). Dim join only adds value if you want to filter/label by continent — and even then, only works for the 5 joinable codes.