table: fact.dnfdiflo
description: Direkte investeringer transaktioner (strøm) efter retning, instrument, land og tid
measure: indhold (unit Mio. kr.)
columns:
- retnat: values [U=Udadgående, I=Indadgående]
- instrnat: values [2.0=2.0: Direkte investeringer (I alt), 2.1=2.1: Egenkapital, 2.1A=2.1a: Egenkapitalinvesteringer, 2.1B=2.1b: Geninvesteret indtjening, 2.2=2.2: Koncernlån mv.]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [1, 2, 4]
- tid: date range 2005-01-01 to 2025-04-01
dim docs: /dim/lande_uht_bb.md

notes:
- Transaction flows (strøm) only — no holdings or income. retnat selects direction: U=Udadgående (outward), I=Indadgående (inward). Always filter retnat to one value.
- instrnat is a selector with a finer breakdown than other tables: 2.0=total, 2.1=egenkapital (subtotal), 2.1A=egenkapitalinvesteringer, 2.1B=geninvesteret indtjening, 2.2=koncernlån. Note 2.1A+2.1B=2.1. Always filter to one code to avoid overcounting.
- This table has only 8 distinct land codes (A1, B6, F1, I9, R12, S1, US, W1) — much fewer than dnfdiouc/dnfdiinc. Only 5 join to dim.lande_uht_bb; W1, I9, R12 are custom BoP aggregates.
- Quarterly data (tid has Q1–Q4 entries), running through 2025 — the most current of the direkte investeringer tables.