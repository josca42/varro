table: fact.uhixy
description: Indeks for udenrigshandel med varer efter im- og eksport, indekstype og tid
measure: indhold (unit Indeks)
columns:
- indud: values [0=Bytteforhold, 1=Import, 2=Eksport]
- indekstype: values [KVANTUM=Kvantumindeks, ENHED=Enhedsværdiindeks]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- indud=0 (Bytteforhold = terms of trade) has different semantics than 1=Import / 2=Eksport. Never sum it with the other indud values.
- indekstype is a MEASUREMENT SELECTOR: KVANTUM or ENHED. Always filter to one — never sum across both.
- No saeson2 or sitc breakdown — simplest aggregate trade index table. Annual data 2007–2024.
- For monthly data with seasonal adjustment see uhixm. For SITC-level breakdown see sitcixy/sitcixm.