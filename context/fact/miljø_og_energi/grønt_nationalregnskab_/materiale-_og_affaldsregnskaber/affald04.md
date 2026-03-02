table: fact.affald04
description: Im- og eksport af affald efter affaldsfraktion, behandlingsform, im- og eksport og tid
measure: indhold (unit Ton)
columns:
- afffrak: values [TOTAFFALD=Affald i alt (inkl. jord), TOTAFFALDX=Affald i alt (ekskl. jord), A=DAGRENOVATION OG LIGNENDE, 101=Dagrenovation og lignende, B=ORGANISK AFFALD, INKL. HAVEAFFALD ... 151=Restprodukter fra forbrænding, 152=Deponeringsegnet, 124=Tekstiler, 125=Blandet emballage, 199=Andet affald]
- behandling: values [TOT=I alt, GENANV=Genanvendelse, inkl. anden endelig materialenyttiggørelse, FORBRND=Forbrænding, DEPOT=Deponering, SPEC=Særlig behandling, MIDOP=Midlertidig oplagring]
- indud: values [1=Import, 2=Eksport]
- tid: date range 2011-01-01 to 2023-01-01
notes:
- Import/export of waste — the only table in this subject covering cross-border waste flows.
- indud: 1=Import, 2=Eksport. Always filter to one direction for directional analysis; sum both for total trade volume.
- afffrak and behandling both have aggregate totals (TOTAFFALD/TOTAFFALDX and TOT) — filter to consistent level.
- No erhverv dimension: covers all industries combined.
