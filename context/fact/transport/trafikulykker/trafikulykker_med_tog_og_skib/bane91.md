table: fact.bane91
description: Dræbte og tilskadekomne ved jernbanetrafik efter banenet, personkategori, personskade og tid
measure: indhold (unit Antal)
columns:
- bane: values [10010=BANENETTET I ALT, 10020=BANEDANMARKS NET  I ALT, 10130=METROEN, 10120=ANDRE BANER, 10140=LETBANE]
- pkategori: values [0=I alt, 3020=Passagerer, 3025=Ansatte ved banen, 3030=Andre]
- uheld: values [1=Dræbte, 2=Alvorligt tilskadekomne]
- tid: date range 1993-01-01 to 2024-01-01

notes:
- bane=10010 (BANENETTET I ALT) is the aggregate of all networks. bane=10020 is Banedanmarks net (national rail), 10130=Metro, 10140=Letbane. Note: 10120 (ANDRE BANER) is documented but absent from the actual data.
- pkategori=0 (I alt) is the total across person categories (3020=Passagerer, 3025=Ansatte, 3030=Andre). Filter to pkategori=0 for overall counts or pick a specific category.
- uheld has only 2 values with no aggregate: 1=Dræbte (killed), 2=Alvorligt tilskadekomne (seriously injured). These are independent outcomes — summing them gives total casualties, which is valid.
- To get total railway fatalities for all of Denmark: filter bane=10010, pkategori=0, uheld=1. To break down by person type, filter bane=10010 and a specific uheld, then group by pkategori (excluding pkategori=0 to avoid double-counting).