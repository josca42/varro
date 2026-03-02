table: fact.nahc3
description: Husholdningers forbrug på dansk område efter varighed, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- kmdr: values [P31DC=Husholdningers forbrugsudgift på dansk område, P311_313=Varer i alt, P311_313_A4=Varer ekskl. køb af køretøjer samt forbrug af elektricitet, fjernvarme og andet brændsel, P311=Varige varer, P311A=Køb af køretøjer, P311B=Varige varer ekskl. køb af køretøjer, P312=Halvvarige varer, P313=Ikke varige varer, P313E=Forbrug af elektricitet, fjernvarme og andet brændsel, P313_4=Ikke-varige varer ekskl. forbrug af elektricitet, fjernvarme og andet brændsel, P314=Tjenester i alt, P314A=Boligbenyttelse, P314B=Tjenester ekskl. boligbenyttelse]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2024-01-01
notes:
- prisenhed is a measurement selector (V/LAN) — filter to one value or row counts double.
- kmdr codes classify household expenditure by durability: P311=varige varer, P312=halvvarige varer, P313=ikke-varige varer, P314=tjenester. P31DC='Husholdningers forbrugsudgift på dansk område' is the top-level total.
- Several codes are sub-aggregates (P313E is a subset of P313; P311A+P311B=P311; P314A+P314B=P314) — avoid double-counting by picking the level you need. Annual from 1966; quarterly with saeson: nkhc3.
