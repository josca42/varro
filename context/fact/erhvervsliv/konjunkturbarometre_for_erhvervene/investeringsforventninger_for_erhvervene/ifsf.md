table: fact.ifsf
description: Serviceerhvervets investeringsforventninger efter branche (DB07), formål og tid
measure: indhold (unit Pct.)
columns:
- branche07: values [0=SERVICEERHVERV I ALT, 5=TRANSPORT (49-53), 10=Landtransport (49), 15=TURISME (55-56; 79), 20=Hoteller mv. (55), 25=Restauranter (56), 30=Rejsebureauer (79), 35=FORLAG, TELE OG IT (58; 61-63), 40=It-konsulenter mv. (62), 45=FINANS, FORSIKRING, EJENDOM mv. (64-65; 68), 50=Finansiering og forsikring (64-65), 55=Ejendomshandel og udlejning (68), 60=RÅDGIVNING, FORSKNING, O.A. VIDENSSERVICE (69-74), 65=RENGØRING O.A. OPERATIONEL SERVICE (77-78; 81-82), 70=Udlejning og leasing af materiel (77), 75=Ejendomsservice, rengøring og anlægsgartnere (81), 80=KULTUR, FRITID OG ANDEN SERVICE (90-95), 85=kultur, sport og fritid (90-93), 90=Andre serviceydelser (94-95)]
- formal: values [ERST=Erstatning af nedslidt materiel eller udstyr, UDVI=Udvidelse af produktionskapaciteten, RATI=Rationalisering af driften, ANDR=Andre formål, fx miljø og sikkerhed]
- tid: date range 2021-01-01 to 2026-01-01

notes:
- branche07 uses survey-specific numeric codes — does NOT join dim.db. Same coding as ifs01: 0=total, aggregates vs sub-sectors. Filter to one hierarchy level.
- formal values sum to 100 per branche07/tid — they are an allocation of investment budget (ERST+UDVI+RATI+ANDR = 100). Show all four values together to understand investment purpose composition. Service counterpart of ifif.