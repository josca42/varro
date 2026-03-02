<fact tables>
<table>
id: alko6
description: Salg af alkohol og tobak efter type og tid
columns: type, tid (time), indhold (unit -)
tid range: 1921-01-01 to 2024-01-01
</table>
<table>
id: alko5
description: Salg af alkohol og tobak efter type og tid
columns: type, tid (time), indhold (unit Indeks)
tid range: 1955-01-01 to 2024-01-01
</table>
<table>
id: alko2
description: Salg af alkohol og tobak pr. indbygger efter type og tid
columns: type, tid (time), indhold (unit Gns.)
tid range: 1921-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For absolute sales volumes (1000 liters, mio. pieces, tons): use alko6. It has alcohol (beer/wine/spirits) and tobacco (cigarettes/cigars/smoking tobacco) back to 1921-1923, and pure-alcohol breakdowns per drink type from 1955.
- For per-capita consumption: use alko2 (pure alcohol in liters and cigarettes per person, two population bases: all ages vs 18+).
- For relative trends on a common scale: use alko5 (index values, all series from 1955). Good for charting how beer, wine, spirits, and tobacco categories moved relative to each other over time.
- None of these tables have regional or demographic breakdowns — all are national aggregates.
- All three tables have mixed units or index values encoded in the type column. Never sum across type values within any table.