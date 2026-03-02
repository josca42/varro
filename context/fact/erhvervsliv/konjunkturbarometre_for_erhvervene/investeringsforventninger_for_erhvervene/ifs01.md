table: fact.ifs01
description: Servicerhvervets investeringsforventninger efter branche (DB07), bedømmelse og tid
measure: indhold (unit Pct.)
columns:
- branche07: values [0=SERVICEERHVERV I ALT, 5=TRANSPORT (49-53), 10=Landtransport (49), 15=TURISME (55-56; 79), 20=Hoteller mv. (55), 25=Restauranter (56), 30=Rejsebureauer (79), 35=FORLAG, TELE OG IT (58; 61-63), 40=It-konsulenter mv. (62), 45=FINANS, FORSIKRING, EJENDOM mv. (64-65; 68), 50=Finansiering og forsikring (64-65), 55=Ejendomshandel og udlejning (68), 60=RÅDGIVNING, FORSKNING, O.A. VIDENSSERVICE (69-74), 65=RENGØRING O.A. OPERATIONEL SERVICE (77-78; 81-82), 70=Udlejning og leasing af materiel (77), 75=Ejendomsservice, rengøring og anlægsgartnere (81), 80=KULTUR, FRITID OG ANDEN SERVICE (90-95), 85=kultur, sport og fritid (90-93), 90=Andre serviceydelser (94-95)]
- bedommelse: values [STØ=Stigende/forbedret, UÆN=Omtrent uændret, MIN=Faldende/forringet, NET=Nettotal]
- tid: date range 2021-01-01 to 2026-01-01

notes:
- branche07 does NOT join dim.db — the numeric codes are survey-specific service sector groups unrelated to DB07 integer kodes. The doc previously annotated a dim.db join but it is invalid (code 5 would match "Indvinding af kul" instead of "TRANSPORT").
- branche07 has a 2-level hierarchy: codes 0 (total), 5, 15, 35, 45, 60, 65, 80 are sector aggregates (uppercase in labels); codes 10, 20, 25, 30, 40, 50, 55, 70, 75, 85, 90 are sub-sectors. Filter to aggregates OR sub-sectors to avoid double-counting.
- bedommelse: STØ+UÆN+MIN = 100; NET = STØ−MIN. Filter to one bedommelse per query.