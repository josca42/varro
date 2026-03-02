table: fact.lbesk46
description: Indvandrere med lønmodtagerjob efter enhed, branche (DB07 19-grp), oprindelsesland, køn og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- branchedb0738: join dim.db on branchedb0738=kode::text [approx]
- oprindland: join dim.lande_uhv on oprindland=kode [approx]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/db.md, /dim/lande_uhv.md
notes:
- SCOPE: Only covers indvandrere (immigrants) — NOT efterkommere or persons of Danish origin. Use lbesk43/lbesk62 for all herkomst groups.
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- WARNING: dim.db join for branchedb0738 is broken (0% match). branchedb0738 uses letter codes only (A–S, X, TOT) — NOT in dim.db. Treat as inline. Use ColumnValues("lbesk46", "branchedb0738") for labels.
- WARNING: dim.lande_uhv join for oprindland is broken (0% match). oprindland uses DST-specific 3-letter country codes (AFG, BOS, BUL, FRA, HOL, IND, IRA, IRN, ISL, ITA, etc.) plus aggregate codes 32=Indvandrere fra vestlige lande and 34=Indvandrere fra ikke-vestlige lande. These do NOT match dim.lande_uhv numeric continent codes. Use ColumnValues("lbesk46", "oprindland") for the 39 available country/group values. TOT = all origins.
- Note: kon uses M/K (not 1/2 as in other lbesk tables). TOT=I alt.
