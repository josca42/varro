table: fact.silc3b
description: Boligbyrde: Andel personer efter husstandstype, alder, i hvor høj grad husstanden synes boligudgiften er en byrde og tid
measure: indhold (unit Pct.)
columns:
- hustyp: values [ALLE=Alle, EUB=Enlige uden børn, EMB=Enlige med børn, PUB=Par uden børn, PMB=Par med børn, FF=Andre husstandstyper]
- alder: values [IALT=Alder i alt, 0019=Under 20 år, 2059=20-59 år, 6099=60 år og derover]
- svaerhed1: values [100=I alt, 115=En tung byrde, 120=Noget af en byrde, 125=Ikke noget problem]
- tid: date range 2004-01-01 to 2024-01-01
notes:
- Housing cost burden by household type and broad age. Same series as silc1b (2004–2024), percentages only.
- svaerhed1=100 is always indhold=100 (dummy total). Use svaerhed1 IN (115, 120, 125) for real distribution.
- hustyp: ALLE, EUB=Enlige uden børn, EMB=Enlige med børn, PUB=Par uden børn, PMB=Par med børn, FF=Andre.
- alder here has only 3 bands (0019, 2059, 6099) plus IALT — much coarser than silc1b. Use IALT for overall within hustyp.
