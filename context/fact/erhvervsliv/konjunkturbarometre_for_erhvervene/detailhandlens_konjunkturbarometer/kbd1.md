table: fact.kbd1
description: Udviklingsforløb i detailhandlen efter branche (DB07), indikator, bedømmelse, forløb og tid
measure: indhold (unit Pct.)
columns:
- branche07: values [100=DETAILHANDEL I ALT, 105=BILHANDEL I ALT (45), 110=Bilhandel inkl. engroshandel (45,1), 115=Bilværksteder mv. (45,2-45,4), 120=DETAILHANDEL EKSKL. BILHANDEL I ALT (47), 125=Handel med fødevarer, drikke- og tobaks- varer (47,1;  47,2; 47,8), 130=Tankstationer (47,3), 135=Anden detailhandel (47,4-47,7; 47,9)]
- indikator: values [OMS=Omsætning, BES=Beskæftigelse, ORLE=Ordrebeholdning hos leverandører, SALG=Salgspriser]
- bedommelse: values [STØR=Stigende/forbedret, OMU=Omtrent uændret, MINDRE=Faldende/forringet, NET=Nettotal]
- forlob: values [FAK=Faktisk (foregående 3 måneder), FOR=Forventet (kommende 3 måneder)]
- tid: date range 2011-05-01 to 2025-10-01

notes:
- Each combination of (branche07, indikator, forlob, tid) has exactly 4 bedommelse rows. Never SUM across bedommelse — the three response categories (STØR, OMU, MINDRE) each represent % of firms giving that answer and sum to 100. NET is the derived nettotal (STØR minus MINDRE). To get the headline sentiment figure, filter bedommelse='NET'.
- forlob must always be filtered: FAK = faktisk (actual, previous 3 months), FOR = forventet (expected, next 3 months). Leaving both doubles the row count.
- indikator must always be filtered: OMS=omsætning, BES=beskæftigelse, ORLE=ordrebeholdning hos leverandører, SALG=salgspriser. Each is independent; filter to the one you need.
- branche07 has a hierarchy: 100=total detailhandel, 105=bilhandel total (contains 110, 115), 120=detailhandel ekskl. bil total (contains 125, 130, 135). Selecting all 8 codes together will double-count — pick either the aggregate codes (100, 105, 120) or the leaf codes (110, 115, 125, 130, 135), not both.
- Typical query: filter indikator='OMS', bedommelse='NET', forlob='FAK', then select branche07 codes at the level of interest.
- Data is monthly from May 2011.