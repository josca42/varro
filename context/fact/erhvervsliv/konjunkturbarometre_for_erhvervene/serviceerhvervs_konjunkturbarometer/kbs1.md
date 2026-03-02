table: fact.kbs1
description: Udviklingsforløb i serviceerhverv efter branche (DB07), indikator, bedømmelse, forløb og tid
measure: indhold (unit Pct.)
columns:
- branche07: values [0=SERVICEERHVERV I ALT, 5=TRANSPORT (49-53), 10=Landtransport (49), 15=TURISME (55-56; 79), 20=Hoteller mv. (55), 25=Restauranter (56), 30=Rejsebureauer (79), 35=FORLAG, TELE OG IT (58; 61-63), 40=It-konsulenter mv. (62), 45=FINANS, FORSIKRING, EJENDOM mv. (64-65; 68), 50=Finansiering og forsikring (64-65), 55=Ejendomshandel og udlejning (68), 60=RÅDGIVNING, FORSKNING, O.A. VIDENSSERVICE (69-74), 65=RENGØRING O.A. OPERATIONEL SERVICE (77-78; 81-82), 70=Udlejning og leasing af materiel (77), 75=Ejendomsservice, rengøring og anlægsgartnere (81), 80=KULTUR, FRITID OG ANDEN SERVICE (90-95), 85=kultur, sport og fritid (90-93), 90=Andre serviceydelser (94-95)]
- indikator: values [FOS=Forretningssituation, OM1=Omsætning, BES=Beskæftigelse, SAL=Salgspriser/servicetakster]
- bedommelse: values [SFO=Stigende/forbedret, OMU=Omtrent uændret, MFO=Faldende/forringet, NET=Nettotal]
- forlob: values [FAK=Faktisk (foregående 3 måneder), FOR=Forventet (kommende 3 måneder)]
- tid: date range 2011-05-01 to 2025-10-01

notes:
- bedommelse has 4 values but NET is derived: NET = SFO - MFO (confirmed). SFO + OMU + MFO = 100% exactly. Never sum across bedommelse — for the net balance indicator just filter bedommelse='NET'. For the raw survey distribution use SFO/OMU/MFO individually.
- indikator=FOS (Forretningssituation) only has forlob=FAK. The other three indicators (OM1, BES, SAL) have both FAK and FOR. Always filter forlob explicitly to avoid double-counting.
- Every query must filter to exactly one indikator, one forlob, and one bedommelse. Failing to filter any of these silently multiplies the result.
- branche07=0 (SERVICEERHVERV I ALT) is the aggregate for all services. The codes alternate between sector totals (uppercase names, e.g. 5=TRANSPORT, 15=TURISME) and their sub-sectors (lowercase names, e.g. 10=Landtransport, 20=Hoteller). Both levels coexist in the table — summing across all branche07 values double-counts. Pick one level: use branche07='0' for the aggregate, the uppercase-labeled codes for sector totals, or the lowercase-labeled codes for sub-sector drill-down.
- Typical net balance query: SELECT branche07, tid, indhold FROM fact.kbs1 WHERE indikator='OM1' AND forlob='FAK' AND bedommelse='NET' AND branche07='0' ORDER BY tid;