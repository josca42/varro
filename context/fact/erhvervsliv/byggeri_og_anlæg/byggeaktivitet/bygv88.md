table: fact.bygv88
description: Det samlede etageareal (korrigeret for forsinkelser) efter byggefase, anvendelse, bygherreforhold, sæsonkorrigering og tid
measure: indhold (unit M2)
columns:
- bygfase: values [2=Påbegyndt byggeri, 3=Fuldført byggeri, 4=Byggeri under opførelse, 1=Tilladt byggeri]
- anvendelse: join dim.byganv on anvendelse=kode [approx]
- bygherre: join dim.bygherre on bygherre=kode::text [approx]
- saeson: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 1998-01-01 to 2025-06-01
dim docs: /dim/byganv.md, /dim/bygherre.md
notes:
- saeson is a measurement selector: 'EJSÆSON' (ikke sæsonkorrigeret) vs 'SÆSON' (sæsonkorrigeret). Always filter to one — failing to do so doubles counts. The SÆSON series only exists for bygherre='TOT'; BOLIG, PRIVAT, OFFBYG only have EJSÆSON.
- anvendelse does NOT join dim.byganv. It uses standalone 5-digit codes: 10000=Alle bygninger (total), 10100=Boliger, 10200=Erhvervsbygninger, 10500=Øvrige bygninger. Do not attempt a dim join.
- bygherre does NOT join dim.bygherre. It uses standalone codes: TOT=Alle bygherrer, BOLIG=Boligforeninger, PRIVAT=Private bygherrer, OFFBYG=Offentlige bygherrer. Do not attempt a dim join.
- This is the delay-corrected (korrigeret) version of total etageareal with seasonal adjustment and bygherre breakdown. For non-corrected data with regional breakdown use bygv11. For corrected without bygherre/saeson use bygv80.
