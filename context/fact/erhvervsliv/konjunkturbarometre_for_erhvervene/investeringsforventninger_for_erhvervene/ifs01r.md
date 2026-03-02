table: fact.ifs01r
description: Serviceerhvervets investeringsforventninger efter branche (DB07), opgørelse (målingstidspunkt), bedømmelse og tid
measure: indhold (unit Pct.)
columns:
- branche07: values [0=SERVICEERHVERV I ALT, 5=TRANSPORT (49-53), 10=Landtransport (49), 15=TURISME (55-56; 79), 20=Hoteller mv. (55), 25=Restauranter (56), 30=Rejsebureauer (79), 35=FORLAG, TELE OG IT (58; 61-63), 40=It-konsulenter mv. (62), 45=FINANS, FORSIKRING, EJENDOM mv. (64-65; 68), 50=Finansiering og forsikring (64-65), 55=Ejendomshandel og udlejning (68), 60=RÅDGIVNING, FORSKNING, O.A. VIDENSSERVICE (69-74), 65=RENGØRING O.A. OPERATIONEL SERVICE (77-78; 81-82), 70=Udlejning og leasing af materiel (77), 75=Ejendomsservice, rengøring og anlægsgartnere (81), 80=KULTUR, FRITID OG ANDEN SERVICE (90-95), 85=kultur, sport og fritid (90-93), 90=Andre serviceydelser (94-95)]
- opg: values [10=Foreløbige tal (Opgjort oktober året før), 25=Foreløbige tal 1. revision (Opgjort april samme år), 30=Foreløbige tal 2. revision (Opgjort oktober samme år), 45=Endelige tal (Opgjort april året efter)]
- bedommelse: values [STØ=Stigende/forbedret, UÆN=Omtrent uændret, MIN=Faldende/forringet, NET=Nettotal]
- tid: date range 2021-01-01 to 2026-01-01

notes:
- opg multiplies rows 4× per year — always filter to one opg value. Use opg=45 for final figures. Prefer ifs01 if revision tracking is not needed.
- branche07 uses survey-specific numeric codes (0=total, 5=TRANSPORT sector, 10=Landtransport sub-sector, etc.) — does NOT join dim.db. Has a 2-level hierarchy: aggregate codes (0, 5, 15, 35, 45, 60, 65, 80) vs sub-sector codes (10, 20, 25, 30, 40, 50, 55, 70, 75, 85, 90). Filter to one level to avoid double-counting.
- bedommelse: STØ+UÆN+MIN = 100; NET = STØ−MIN. Filter to one bedommelse per query.