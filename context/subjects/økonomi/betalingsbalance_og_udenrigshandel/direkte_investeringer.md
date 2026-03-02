<fact tables>
<table>
id: dnfdiouc
description: Danske direkte investeringer I udlandet efter land, instrument, datatype og tid
columns: land, instrnat, data, tid (time), indhold (unit Mio. kr.)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: dnfdiflo
description: Direkte investeringer transaktioner (strøm) efter retning, instrument, land og tid
columns: retnat, instrnat, land, tid (time), indhold (unit Mio. kr.)
tid range: 2005-01-01 to 2025-04-01
</table>
<table>
id: dnfdioui
description: Danske direkte investeringer i udlandet efter udenlandsk branche (DB07), instrument, datatype og tid
columns: udlbranche, instrnat, data, tid (time), indhold (unit Mio. kr.)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: dnfdiinc
description: Udlandets direkte investeringer i Danmark efter land, instrument, datatype og tid
columns: land, instrnat, data, tid (time), indhold (unit Mio. kr.)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: dnfdiini
description: Udlandets direkte investeringer i Danmark efter indenlandsk branche (DB07), instrument, datatype og tid
columns: indlbranche, instrnat, data, tid (time), indhold (unit Mio. kr.)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: dnfdiuie
description: Ultimativt investorland for udlandets direkte investeringer i Danmark efter land, instrument, datatype og tid
columns: land, instrnat, data, tid (time), indhold (unit Mio. kr.)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: dnfdipti
description: Gennemløbsinvesteringer (gennemløbsholdingselskaber) efter retning, datatype, land og tid
columns: retnat, data, land, tid (time), indhold (unit Mio. kr.)
tid range: 2004-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All tables share a common pattern: data (F/S/I) and instrnat (2.0/2.1/2.2) are selector dimensions that repeat across every combination. Always filter both to a single value or you will multiply-count. The one exception is dnfdipti which has no instrnat column.
- For FDI by country (land): use dnfdiouc (outward, 2004–2024) or dnfdiinc (inward, 2004–2024). Both join dim.lande_uht_bb with ~93% match at niveaux 1, 2, and 4. Unmatched codes W1, I9, R12 are custom BoP aggregates — not in the dim.
- For FDI by industry (branche): use dnfdioui (outward by foreign industry, 2015–2024) or dnfdiini (inward by domestic industry, 2004–2024). These use NACE letter codes — do NOT join dim.db (0% match). Use ColumnValues("dnfdioui", "udlbranche") or ColumnValues("dnfdiini", "indlbranche") for labels.
- For transaction flows (strøm) with quarterly resolution and most recent data (through 2025): use dnfdiflo. It has both direction (retnat: U/I) and a finer instrnat breakdown (2.1A=equity investments, 2.1B=reinvested earnings, both subcategories of 2.1).
- For ultimate investor country (who actually owns the investment, not the immediate counterpart): use dnfdiuie (inward only, 2016–2024). Includes DK as a land code (round-tripping). Holdings and income only — no transaction flows.
- For pass-through investments via holding companies: use dnfdipti (2004–2024). Very coarse geography — only B6 (EU-27), I9, and W1. No instrnat breakdown.
- instrnat values differ slightly across tables: dnfdiflo has the finest breakdown (adds 2.1A, 2.1B); dnfdiuie label for 2.1 says "Egenkapital" (same as others but no sub-split).
- The NACE subcategories in the branche tables (C21⊂C, C28⊂C, H50⊂H, K64.2⊂K, M70⊂M) are additive subsets — never sum parent + child.