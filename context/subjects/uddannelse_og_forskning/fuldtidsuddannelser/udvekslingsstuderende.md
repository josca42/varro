<fact tables>
<table>
id: udvstd02
description: Udvekslingsstuderende efter køn, udveksling, opholds varighed, uddannelse, område og tid
columns: kon, udveksling, opvar, uddannelse, omr20, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Only one table: udvstd02. It covers exchange students 2010–2024, broken down by gender (kon), direction (udveksling: inbound/outbound), stay duration (opvar), education level (uddannelse), and world region of partner country (omr20).
- Always filter all non-target columns to their totals (kon=0, udveksling=TOT, opvar=TOT, omr20=TOT, uddannelse=TOT) to avoid overcounting — every column carries aggregate rows.
- uddannelse uses inline hierarchy codes (H30/H40/.../H80 as level-1 aggregates, H3055/H4024/... as detail). Pick one level consistently; never mix.
- To split inbound vs outbound: filter udveksling=1 (foreigners in Denmark) or udveksling=2 (Danes abroad).