<fact tables>
<table>
id: kbd1
description: Udviklingsforløb i detailhandlen efter branche (DB07), indikator, bedømmelse, forløb og tid
columns: branche07, indikator, bedommelse, forlob, tid (time), indhold (unit Pct.)
tid range: 2011-05-01 to 2025-10-01
</table>
<table>
id: kbd2
description: Vurdering af varelagre i detailhandlen efter branche (DB07), bedømmelse og tid
columns: branche07, bedommelse, tid (time), indhold (unit Pct.)
tid range: 2011-05-01 to 2025-10-01
</table>
</fact tables>

notes:
- kbd1 covers the main business tendency indicators (omsætning, beskæftigelse, ordrebeholdning, salgspriser), both faktisk (previous 3 months) and forventet (next 3 months). Use this for general retail sentiment.
- kbd2 covers only inventory assessment (varelagre: for stor / passende / for lille). Use this when the question is specifically about stock levels.
- Both tables are monthly from May 2011 and share the same branche07 breakdown (8 codes with a 2-level hierarchy).
- In both tables, bedommelse='NET' is the nettotal (% positive minus % negative) — the standard headline figure. Never sum across bedommelse values.
- branche07 100 is the total; 105 (bilhandel) and 120 (detailhandel ekskl. bil) are sub-totals. Always pick one hierarchy level to avoid double-counting.