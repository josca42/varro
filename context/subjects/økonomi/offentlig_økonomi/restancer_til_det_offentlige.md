<fact tables>
<table>
id: offres10
description: Offentlige restancer efter restancetype, gældstype, prisenhed og tid
columns: restance, deltyp, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 2013-01-01 to 2024-01-01
</table>
<table>
id: offres11
description: Offentlige restancer efter restancetype, gældstype, konto og tid
columns: restance, deltyp, konto1, tid (time), indhold (unit Mio. kr.)
tid range: 2019-01-01 to 2024-01-01
</table>
<table>
id: offres20
description: Skatterestancer efter restancetype, gældstype, prisenhed og tid
columns: restance, deltyp, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 2013-01-01 to 2024-01-01
</table>
<table>
id: offres21
description: Skatterestancer efter restancetype, gældstype, konto og tid
columns: restance, deltyp, konto1, tid (time), indhold (unit Mio. kr.)
tid range: 2019-01-01 to 2024-01-01
</table>
<table>
id: offres30
description: Andre offentlige restancer efter restancetype, gældstype, prisenhed og tid
columns: restance, deltyp, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 2013-01-01 to 2024-01-01
</table>
<table>
id: offres31
description: Andre offentlige restancer efter restancetype, gældstype, konto og tid
columns: restance, deltyp, konto1, tid (time), indhold (unit Mio. kr.)
tid range: 2019-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Table naming: x0 tables (offres10/20/30) give stock levels by prisenhed (nominal vs. market value). x1 tables (offres11/21/31) give account movements (tilgang, afskrivning, provenu, etc.) without prisenhed but with konto1.
- For outstanding debt totals and trends over time: use offres10 (2013-2024). For SKAT breakdown by tax type: offres20. For non-SKAT breakdown by creditor (municipalities, state agencies, public enterprises): offres30.
- For flow analysis (how much new debt arose, how much was written off, how much collected): use offres11/21/31 (from 2019 only).
- All tables share the same restance and deltyp hierarchies. restance includes aggregate totals (101, 201, 301) and level-1 and level-2 subtotals mixed in the same column — always filter to a single level. deltyp 601 = 602+603, so filter to one value.
- prisenhed in x0 tables doubles every row (401=nominal, 402=kursværdi). Forgetting to filter prisenhed silently doubles all sums. Prefer prisenhed=401 unless market value is specifically needed.
- konto1 in x1 tables: codes 501-506 represent a stock-flow identity (primo + flows = ultimo). Summing across konto1 is always wrong. Choose konto1=506 for closing balance, konto1=502 for new debt, etc.