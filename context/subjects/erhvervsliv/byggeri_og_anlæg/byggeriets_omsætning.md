<fact tables>
<table>
id: bygoms2
description: Omsætning i byggeri og anlæg efter branche (DB07), arbejdets art og tid
columns: branche07, arbart, tid (time), indhold (unit Mio. kr.)
tid range: 2015-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- bygoms2 is the only table in this subject. It covers annual omsætning (Mio. kr.) in construction 2015–2024, broken down by branche and arbejdets art.
- branche07 uses survey-specific codes — do NOT join dim.db. Use ColumnValues("bygoms2", "branche07") to get the 9 categories. F is the grand total; 41000 (byggeentreprenører) and 42000 (anlægsentreprenører) cover sections 41 and 42 as blocks; section 43 is broken into 6 specialist trades (el, VVS, tømrer, maler, murere, andre).
- arbart encodes both totals and sub-categories in the same column. Filter to arbart='0' for overall omsætning, or to single-digit codes (1–4) for top-level split by type of work. Double-digit codes (10, 11, 20…) are sub-categories that sum to their parent — never mix levels.