table: fact.ligeii8
description: Ligestillingsindikator for median pensionsformue for personer efter indikator, alder og tid
measure: indhold (unit -)
columns:
- indikator: values [LAK1=Mænd (kr.), LAK2=Kvinder (kr.), LAP3=Pensionsformuegab (pct.)]
- alder: values [IALT=Alder i alt, 1829=18-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8099=80 år og derover]
- tid: date range 2014-01-01 to 2023-01-01

notes:
- Mixed units across indikator — never sum or average across indikator values: LAK1=mænd median pensionsformue (kr.), LAK2=kvinder median pensionsformue (kr.), LAP3=pensionsformuegab (pct.).
- Pension wealth specifically (FGCX in the formue11-17 taxonomy) — not total nettoformue. Use for questions specifically about the pension gap between genders.
- alder='IALT' is the total; filter to one alder value.
- No famtyp dimension (unlike ligeii7). Covers persons, not family units.
