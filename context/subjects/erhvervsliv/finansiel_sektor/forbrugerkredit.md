<fact tables>
<table>
id: mpk30
description: Forbrugerkredit, ultimo kvartalet efter type og tid
columns: type, tid (time), indhold (unit Mio. kr.)
tid range: 2018-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- Only one table: mpk30. Quarterly end-of-quarter consumer credit balances in Mio. kr., from 2018 Q1 to 2025 Q2.
- type column is hierarchical — use 2482 for total, 2481 for bank credit, 2480 for non-bank consumer credit companies. Never sum all 8 type codes together.
- Two sub-categories (2440, 2443) were discontinued after 2018 Q4; use aggregate types for full-period trend analysis.