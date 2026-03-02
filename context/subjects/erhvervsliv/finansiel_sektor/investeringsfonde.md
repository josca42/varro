<fact tables>
<table>
id: dnifubal
description: Investeringsfondenes ultimobalance efter balancepost, investeringsfondstype og tid
columns: balpostnat1, investfond, tid (time), indhold (unit Mio. kr.)
tid range: 2018-01-01 to 2025-09-01
</table>
<table>
id: dnifsum
description: Investeringsfonde og investorernes formue efter investeringsfondstype, hovedkategori, forvaltningstype, datatype og tid
columns: investfond, hovedkat, forvalt, data, tid (time), indhold (unit Mio. kr.)
tid range: 2018-01-01 to 2025-09-01
</table>
</fact tables>

notes:
- For balance sheet (ultimobalance) — aktiver og passiver by type: use dnifubal. It has 10 individual balance line items; no totals row for aktiver/passiver, so sum the relevant items in SQL.
- For investor wealth (formue) or number of funds by fund category and management type: use dnifsum. It covers both metrics via the data selector column (data='1' formue, data='7' antal) — always filter data to one value.
- Both tables cover the same investfond breakdown (AIF/UCITS/XX total) and the same time range (2018–2025, quarterly).
- Neither table has regional breakdown or investor demographics — they are aggregate national statistics for the investment fund sector.