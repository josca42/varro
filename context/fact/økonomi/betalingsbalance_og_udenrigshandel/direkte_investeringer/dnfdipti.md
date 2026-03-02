table: fact.dnfdipti
description: Gennemløbsinvesteringer (gennemløbsholdingselskaber) efter retning, datatype, land og tid
measure: indhold (unit Mio. kr.)
columns:
- retnat: values [U=Udadgående, I=Indadgående]
- data: values [F=Transaktioner, S=Beholdninger (ultimo året)]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [2]
- tid: date range 2004-01-01 to 2024-01-01
dim docs: /dim/lande_uht_bb.md

notes:
- Specialised table for gennemløbsinvesteringer (pass-through investments via holding companies). Separate from regular FDI.
- Only 3 land codes: B6 (EU-27, the only one that joins dim.lande_uht_bb), I9 and W1 (BoP aggregates). No individual country breakdown.
- retnat selects direction: U=Udadgående, I=Indadgående. data selects type: F=Transaktioner, S=Beholdninger. No instrnat column — no instrument breakdown.
- Always filter retnat and data each to one value to avoid double-counting.
- Use this table specifically for pass-through/transit FDI questions. For regular direct investments, use dnfdiouc/dnfdiinc instead.