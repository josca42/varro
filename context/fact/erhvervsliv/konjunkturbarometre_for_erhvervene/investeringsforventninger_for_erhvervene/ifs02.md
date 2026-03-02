table: fact.ifs02
description: Serviceerhvervets investeringsforventninger efter branche (DB07), investeringstype, bedømmelse og tid
measure: indhold (unit Pct.)
columns:
- branche07: values [0=SERVICEERHVERV I ALT, 5=TRANSPORT (49-53), 10=Landtransport (49), 15=TURISME (55-56; 79), 20=Hoteller mv. (55), 25=Restauranter (56), 30=Rejsebureauer (79), 35=FORLAG, TELE OG IT (58; 61-63), 40=It-konsulenter mv. (62), 45=FINANS, FORSIKRING, EJENDOM mv. (64-65; 68), 50=Finansiering og forsikring (64-65), 55=Ejendomshandel og udlejning (68), 60=RÅDGIVNING, FORSKNING, O.A. VIDENSSERVICE (69-74), 65=RENGØRING O.A. OPERATIONEL SERVICE (77-78; 81-82), 70=Udlejning og leasing af materiel (77), 75=Ejendomsservice, rengøring og anlægsgartnere (81), 80=KULTUR, FRITID OG ANDEN SERVICE (90-95), 85=kultur, sport og fritid (90-93), 90=Andre serviceydelser (94-95)]
- invest: values [TOTAL=Samlet investeringer, MASK=Maskiner og udstyr, LAND=Land, bygninger og infrastruktur, IMMA=Immaterielle investeringer (forskning og udvikling/ software/intellektuelle rettigheder /efteruddannelse osv.)]
- bedommelse: values [STØ=Stigende/forbedret, UÆN=Omtrent uændret, MIN=Faldende/forringet, NET=Nettotal]
- tid: date range 2021-01-01 to 2025-01-01

notes:
- branche07 uses survey-specific numeric codes — does NOT join dim.db. Same coding as ifs01: 0=total, aggregates vs sub-sectors. Filter to one hierarchy level.
- invest: TOTAL is reported independently (not summed from parts in the fact table). Filter invest='TOTAL' for aggregate; use MASK/LAND/IMMA to compare investment type composition. Don't sum across invest.
- bedommelse: STØ+UÆN+MIN = 100 per branche07/invest/tid; NET = STØ−MIN. Filter to one bedommelse per query.
- No opg column — data are final only. For revision tracking use ifs02r.