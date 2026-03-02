table: fact.kbs2
description: Produktionsbegrænsninger i serviceerhverv efter branche (DB07), type og tid
measure: indhold (unit Pct.)
columns:
- branche07: values [0=SERVICEERHVERV I ALT, 5=TRANSPORT (49-53), 10=Landtransport (49), 15=TURISME (55-56; 79), 20=Hoteller mv. (55), 25=Restauranter (56), 30=Rejsebureauer (79), 35=FORLAG, TELE OG IT (58; 61-63), 40=It-konsulenter mv. (62), 45=FINANS, FORSIKRING, EJENDOM mv. (64-65; 68), 50=Finansiering og forsikring (64-65), 55=Ejendomshandel og udlejning (68), 60=RÅDGIVNING, FORSKNING, O.A. VIDENSSERVICE (69-74), 65=RENGØRING O.A. OPERATIONEL SERVICE (77-78; 81-82), 70=Udlejning og leasing af materiel (77), 75=Ejendomsservice, rengøring og anlægsgartnere (81), 80=KULTUR, FRITID OG ANDEN SERVICE (90-95), 85=kultur, sport og fritid (90-93), 90=Andre serviceydelser (94-95)]
- type: values [INGEN=Ingen begrænsninger, MEFT=Mangel på efterspørgsel, MAAK=Mangel på arbejdskraft, MALOK=Mangel på lokaler eller materiel/udstyr, FINBR=Finansielle begrænsninger, ANDÅS=Andre årsager]
- tid: date range 2011-05-01 to 2025-10-01

notes:
- type values are NOT mutually exclusive. Companies can report multiple production constraints simultaneously. The six types sum to ~113% for total services (2025-10), so summing across type is meaningless. Each value is an independent % of companies reporting that constraint.
- To read the table: for a given branche07+tid, each type row answers "what % of firms cite this as a constraint?" Read them side by side, never sum them.
- INGEN=42% means 42% of firms report no constraints — the complement of firms citing at least one constraint is NOT simply 100-INGEN since the others overlap.
- branche07 hierarchy: same as kbs1 — sector totals (uppercase) and sub-sectors (lowercase) coexist. Filter to one level to avoid double-counting.
- Typical query: SELECT type, indhold FROM fact.kbs2 WHERE branche07='0' AND tid='2025-10-01' ORDER BY indhold DESC;