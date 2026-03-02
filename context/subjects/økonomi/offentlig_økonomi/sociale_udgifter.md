<fact tables>
<table>
id: esspros1
description: Sociale udgifter efter Foranstaltning, ydelsestype og tid
columns: foranstalt, ydelsestype, tid (time), indhold (unit Mio. kr.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: esspros2
description: Sociale udgifter efter formål, finansieringskilde og tid
columns: formal, finans, tid (time), indhold (unit Mio. kr.)
tid range: 2007-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Both tables cover 2007–2024 annual data in Mio. kr. Neither has regional breakdown.
- esspros1: use when you need breakdown by type of measure (kontantydelser vs naturalydelser) across detailed foranstaltninger (61 codes in a 2-level hierarchy). Always filter ydelsestype — use ydelsestype=1 for total, or 2/4 for cash vs. in-kind.
- esspros2: use when you need breakdown by financing source (staten/kommuner/arbejdsgivere/sikrede/formueindkomst) across the 8 main formål only. No subcategory detail. Always filter finans — use finans=60 for total.
- Neither foranstalt nor formal join to dim.esspros — both use their own integer coding schemes. Always use ColumnValues("esspros1", "foranstalt") or ColumnValues("esspros2", "formal") to look up labels.
- The two tables use different scope and coding: esspros1 total (foranstalt=1000, ydelsestype=1) ≠ esspros2 total (formal=100, finans=60) — do not mix figures between tables.