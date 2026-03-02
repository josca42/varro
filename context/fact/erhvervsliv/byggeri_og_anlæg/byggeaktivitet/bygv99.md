table: fact.bygv99
description: Boliger i det samlede boligbyggeri (korrigeret for forsinkelser) efter byggefase, anvendelse, bygherreforhold, sæsonkorrigering og tid
measure: indhold (unit Antal)
columns:
- bygfase: values [2=Påbegyndt byggeri, 3=Fuldført byggeri, 4=Byggeri under opførelse, 1=Tilladt byggeri]
- anvendelse: join dim.byganv on anvendelse=kode [approx]
- bygherre: join dim.bygherre on bygherre=kode::text [approx]
- saeson: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 1998-01-01 to 2025-06-01
dim docs: /dim/byganv.md, /dim/bygherre.md
notes:
- saeson is a measurement selector: 'EJSÆSON' vs 'SÆSON'. Always filter to one — failing to do so doubles counts. The SÆSON series only exists for bygherre='TOT'.
- anvendelse does NOT join dim.byganv. It uses standalone 5-digit codes: 10000=Alle boliger (total), 10300=Række/kæde/dobbelthuse, 10400=Etageboliger, 10500=Øvrige boligtyper. Do not attempt a dim join.
- bygherre does NOT join dim.bygherre. Standalone codes: TOT=Alle bygherrer, BOLIG=Boligforeninger, PRIVAT=Private bygherrer, OFFBYG=Offentlige bygherrer. Do not attempt a dim join.
- This is the boliger (count) counterpart of bygv88 (m2). For corrected boliger without bygherre/saeson use bygv90. For non-corrected with regional breakdown use bygv33.
