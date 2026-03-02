table: fact.ror1
description: Rørledningsnettet efter rørledningstype og tid
measure: indhold (unit Km)
columns:
- ror: values [100=RØRLEDNINGER I ALT, 110=Naturgasrør (Transmissionssystemet), 120=Søledning, Nordsø, 130=Søledning, Bælt, 140=Landledning, 150=OLIERØR, 160=Nordsøledning, 170=Landledning]
- tid: date range 1981-01-01 to 2024-01-01

notes:
- `ror` has a 3-level hierarchy. 100=grand total; 110=Naturgasrør and 150=OLIERØR are subtotals; 120/130/140 (gas components) and 160/170 (oil components) are leaf codes. Verified: 110+150=100, 120+130+140=110, 160+170=150.
- Never mix hierarchy levels in a sum. Pick one level: ror='100' for total, ror IN ('110','150') for gas vs oil, or ror NOT IN ('100','110','150') for individual pipe types.
- No dimension joins — ror values are inline codes with labels in the fact doc.