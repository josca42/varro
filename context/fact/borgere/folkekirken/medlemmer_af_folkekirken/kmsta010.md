table: fact.kmsta010
description: Befolkningen 1. januar (15 år+) efter provsti, folkekirkemedlemsskab, pendling og tid
measure: indhold (unit Antal)
columns:
- provsti: values [101=1-01 Københavns Vor Frue Provsti, 102=1-02 Københavns Holmens Provsti, 103=1-03 Østerbro Provsti, 104=1-04 Nørrebro Provsti, 105=1-05 Vesterbro Provsti ... 1004=10-04 Fredericia Provsti, 1005=10-05 Kolding Provsti, 1006=10-06 Vejle Provsti, 1007=10-07 Hedensted Provsti, 9999=99-99 Uoplyst provsti]
- fkmed: values [F=Medlem af Folkekirken, U=Ikke medlem af Folkekirken]
- pendling: values [10=Natbefolkning, 20=Indpendling, 30=Udpendling, 40=Dagbefolkning]
- tid: date range 2016-01-01 to 2024-01-01

notes:
- Provsti-level equivalent of kmsta009. Same pendling selector semantics apply.
- pendling is a MEASUREMENT SELECTOR — NEVER sum across all 4 values. Always filter to one: 10=Natbefolkning (resident count), 20=Indpendling, 30=Udpendling, 40=Dagbefolkning.
- For standard "how many members in this provsti": filter pendling='10' (Natbefolkning).
- Covers only population aged 15+. Available 2016–2024.
