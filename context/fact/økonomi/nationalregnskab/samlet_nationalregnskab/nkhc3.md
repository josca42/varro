table: fact.nkhc3
description: Husholdningers forbrug på dansk område efter varighed, prisenhed, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- kmdr: values [P31DC=Husholdningers forbrugsudgift på dansk område, P311_313=Varer i alt, P311_313_A4=Varer ekskl. køb af køretøjer samt forbrug af elektricitet, fjernvarme og andet brændsel, P311=Varige varer, P311A=Køb af køretøjer, P311B=Varige varer ekskl. køb af køretøjer, P312=Halvvarige varer, P313=Ikke varige varer, P313E=Forbrug af elektricitet, fjernvarme og andet brændsel, P313_4=Ikke-varige varer ekskl. forbrug af elektricitet, fjernvarme og andet brændsel, P314=Tjenester i alt, P314A=Boligbenyttelse, P314B=Tjenester ekskl. boligbenyttelse]
- prisenhed: values [V=Løbende priser, LKV=2020-priser, kædede værdier]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01
notes:
- TWO measurement selectors: prisenhed (V/LKV) and saeson (N/Y). Always filter both.
- Quarterly durability breakdown of household consumption from 1990. Annual equivalent: nahc3 (from 1966).
- Same kmdr hierarchy as nahc3 — P31DC is top total, watch for sub-aggregate double counting within P311 and P314.
