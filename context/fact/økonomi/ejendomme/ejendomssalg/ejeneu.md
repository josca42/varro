table: fact.ejeneu
description: EU-harmoniseret boligprisindeks (HPI) efter urbaniseringsgrad, udgiftstype og tid
measure: indhold (unit Indeks)
columns:
- urbangrad: values [0=Hele landet, 100=Tætbefolket område, 200=Mellembefolket område, 300=Tyndtbefolket område]
- udgtyp: values [H1=Køb af boliger, H12=Køb af eksisterende boliger]
- tid: date range 2002-10-01 to 2025-04-01

notes:
- `udgtyp` has two values that are NOT independent: H1=Køb af boliger (all home purchases) and H12=Køb af eksisterende boliger (existing homes only, a subset of H1). Never sum them — always filter to one. For total market comparison use H1; for existing-homes-only use H12.
- `urbangrad` has 4 values: 0=Hele landet, 100=Tætbefolket, 200=Mellembefolket, 300=Tyndtbefolket. Filter to one to avoid overcounting. These are not joinable to dim.nuts — they use a coarser EU urbanisation classification.
- EU-harmoniseret House Price Index (HPI). The only table in this subject comparable across EU countries. Quarterly from 2002 Q4. No property-type breakdown.