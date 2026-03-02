table: fact.uhixm
description: Indeks for udenrigshandel med varer efter im- og eksport, indekstype, sæsonkorrigering og tid
measure: indhold (unit Indeks)
columns:
- indud: values [0=Bytteforhold, 1=Import, 2=Eksport]
- indekstype: values [KVANTUM=Kvantumindeks, ENHED=Enhedsværdiindeks]
- saeson2: values [1=Ikke sæsonkorrigeret, 2=Sæsonkorrigeret]
- tid: date range 2007-01-01 to 2025-08-01

notes:
- indud=0 (Bytteforhold = terms of trade) has different semantics than 1=Import and 2=Eksport. Bytteforhold is the ratio of export unit values to import unit values — never sum or average it with the import/eksport indices.
- indekstype is a MEASUREMENT SELECTOR: KVANTUM or ENHED. Always filter to one.
- saeson2 is a MEASUREMENT SELECTOR: 1=Ikke sæsonkorrigeret, 2=Sæsonkorrigeret. Always filter to one. Each indud+tid cell appears 4 times (2 indekstype × 2 saeson2).
- No product (sitc) breakdown — aggregate trade index only. For SITC-level breakdown use uhixm/sitcixm.
- Monthly data 2007–2025. For annual see uhixy.