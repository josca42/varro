table: fact.dnvald
description: Valutakurser efter valuta, kurstype og tid
measure: indhold (unit -)
columns:
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- kurtyp: values [KBH=Valutakurser (DKK pr. 100 enheder valuta), INX=Indeks (kun nominel effektiv kronekurs), indeks 1980=100, TT3=Terminstillæg, 3 mdr. (kun USD og EUR fra 1998), DKK pr. 100 enheder valuta (USD 1998 dec-2013 dec og EUR 1999 jan-2013 dec), TT6=Terminstillæg, 6 mdr. (kun USD og EUR fra 1998), DKK pr. 100 enheder valuta (USD 1998 dec-2013 dec og EUR 1999 jan-2013 dec)]
- tid: date range 1977-01-03 to 2025-10-30
dim docs: /dim/valuta_iso.md

notes:
- kurtyp is a measurement selector — always filter to one value. KBH=spot rate (DKK per 100 units of foreign currency), INX=nominal effective exchange rate index 1980=100 (only valuta='DKK'), TT3/TT6=forward premiums for USD and EUR only (1998 onwards). Never aggregate across kurtyp.
- Values are DKK per 100 units of foreign currency (KBH). To get DKK per 1 unit: divide indhold by 100.
- valuta joins dim.valuta_iso, but only ~60% of codes match. The 22 unmatched codes are historical currencies no longer active: pre-euro national currencies (DEM, FRF, ITL, NLG, ESP, ATS, BEF, FIM, IEP, GRD, PTE, EEK, LTL, LVL, SIT, SKK, CYP, MTL, ROL, TRL) and supranational units (XDR=IMF Special Drawing Rights, XEU=European Currency Unit/ECU). These have valid historical data in the fact table but no dim label. Use the ISO code directly rather than joining for historical currencies.
- For a spot rate on a specific date: WHERE valuta='EUR' AND kurtyp='KBH' AND tid='2024-01-15'
- ColumnValues("valuta_iso", "titel", for_table="dnvald") returns the 33 currently active currencies available in this table.