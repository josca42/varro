<fact tables>
<table>
id: dnfx
description: Bankers køb og salg af DKK opdelt på valuta, modpartssektor eller løbetid efter transaktionstype, dimension og tid
columns: transakt1, dimension, tid (time), indhold (unit Mio. kr.)
tid range: 2023-04-01 to 2025-09-01
</table>
<table>
id: dnfxswap
description: Bankers køb og salg af FX swaps i DKK opdelt på valuta, modpartssektor eller løbetid efter transaktionstype, dimension og tid
columns: transakt1, dimension, tid (time), indhold (unit Mio. kr.)
tid range: 2023-04-01 to 2025-09-01
</table>
<table>
id: dnirs
description: Bankers køb og salg af renteswaps i DKK opdelt på modpartssektor, løbetid eller referencerente efter transaktionstype, dimension og tid
columns: transakt1, dimension, tid (time), indhold (unit Mio. kr.)
tid range: 2023-04-01 to 2025-09-01
</table>
<table>
id: dnsemm
description: Bankers sikrede indlån og udlån i DKK opdelt på modpartssektor, løbetid eller sikkerhedsstillelse efter transaktionstype, dimension og tid
columns: transakt1, dimension, tid (time), indhold (unit Mio. kr.)
tid range: 2023-04-01 to 2025-09-01
</table>
<table>
id: dnunmm
description: Bankers usikrede indlån og udlån i DKK opdelt på modpartssektor eller løbetid efter dimension og tid
columns: dimension, tid (time), indhold (unit Mio. kr.)
tid range: 2023-04-01 to 2025-09-01
</table>
</fact tables>

notes:
- All 5 tables cover the Danish money and derivatives market as reported monthly by banks to Danmarks Nationalbank (from April 2023).
- **Shared gotcha**: the `dimension` column is a stacked breakdown — each row is one perspective (valuta, modpartssektor, løbetid, etc.). Always filter to exactly one dimension group. `ALL` equals the group-level totals (FCCALL=CPSALL=MATALL=ALL). Summing across all dimension values overcounts by 3–4x.
- **dnfx** — FX spot market (køb/salg af DKK). Breakdown by currency (EUR/USD/other), counterparty sector, or maturity (1-day buckets up to 20+ bankdays).
- **dnfxswap** — FX swap market (near-leg køb/salg af DKK). Same dimension groups as dnfx but coarser maturity buckets (5-day increments, up to 60+ bankdays).
- **dnirs** — Interest rate swap market (renteswaps i DKK). Breakdowns by counterparty, maturity (in bankdays: ~2yr/2–5yr/>5yr), and reference rate (CIBOR3M/CIBOR6M/DESTR/other).
- **dnsemm** — Secured money market (sikrede indlån/udlån). Adds a collateral dimension: danish mortgage bonds, govt bonds, other. CCP present as counterpart type.
- **dnunmm** — Unsecured money market (usikrede indlån/udlån). No `transakt1` column — transaction type is in dimension (ALLBOR/ALLLEN). Lending side only available as aggregate; deposit side has counterparty and maturity breakdowns.