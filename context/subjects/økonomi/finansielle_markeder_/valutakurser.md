<fact tables>
<table>
id: dnvald
description: Valutakurser efter valuta, kurstype og tid
columns: valuta, kurtyp, tid (time), indhold (unit -)
tid range: 1977-01-03 to 2025-10-30
</table>
<table>
id: dnvalm
description: Valutakurser efter valuta, kurstype, opgørelsesmetode og tid
columns: valuta, kurtyp, opgoer, tid (time), indhold (unit -)
tid range: 1970-01-01 to 2025-09-01
</table>
<table>
id: dnvalq
description: Valutakurser efter valuta, kurstype, opgørelsesmetode og tid
columns: valuta, kurtyp, opgoer, tid (time), indhold (unit Indeks)
tid range: 1970-01-01 to 2025-04-01
</table>
<table>
id: dnvala
description: Valutakurser efter valuta, kurstype, opgørelsesmetode og tid
columns: valuta, kurtyp, opgoer, tid (time), indhold (unit -)
tid range: 1970-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For spot exchange rates (DKK per foreign currency): use dnvald (daily, 1977+), dnvalm (monthly, 1970+), or dnvala (annual, 1970+). dnvalq has no spot rates — indices only.
- Table suffix encodes time granularity: d=daily, m=monthly, q=quarterly, a=annual.
- For a simple rate lookup (e.g. "what was EUR/DKK last month?"): dnvald for a specific date, dnvalm with opgoer='A' for monthly average or opgoer='E' for month-end.
- For Denmark's competitiveness (real/nominal effective exchange rate): dnvalq (quarterly) or dnvala (annual). dnvalm also has these indices but quarterly (dnvalq) is cleaner for that purpose.
- All tables express spot rates as DKK per 100 units of foreign currency (not per unit). Divide indhold by 100 to get per-unit rate.
- All tables in this subject share two common pitfalls: (1) kurtyp must always be filtered — it is a measurement type selector, not a dimension; mixing kurtyp values gives meaningless aggregates. (2) opgoer (present in dnvalm, dnvalq, dnvala) must also be filtered to avoid duplicate rows per period.
- valuta joins dim.valuta_iso, but 22 historical currencies (pre-euro national currencies like DEM, FRF, ITL; plus XDR, XEU) are in the data but not in the dim table. These codes still have valid historical data — use them directly by ISO code without joining dim.