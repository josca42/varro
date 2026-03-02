<fact tables>
<table>
id: vbbm
description: Versionstabel af BBM - Betalingsbalancen månedlig efter version, poster, indtægt/udgift, land, enhed, sæsonkorrigering og tid
columns: version, post, indudbop, land, enhed, saeson, tid (time), indhold (unit -)
tid range: 2005-01-01 to 2025-08-01
</table>
<table>
id: bbq
description: Betalingsbalancen kvartalsvis efter poster, indtægt/udgift, land og tid
columns: post, indudbop, land, tid (time), indhold (unit Mio. kr.)
tid range: 2005-01-01 to 2025-04-01
</table>
<table>
id: vbbq
description: Versionstabel af BBQ - Betalingsbalancen kvartalsvis efter version, poster, indtægt/udgift, land og tid
columns: version, post, indudbop, land, tid (time), indhold (unit Mio. kr.)
tid range: 2005-01-01 to 2025-07-01
</table>
<table>
id: bby
description: Betalingsbalancen årlig efter poster, indtægt/udgift, land og tid
columns: post, indudbop, land, tid (time), indhold (unit Mio. kr.)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: bbuhv
description: Overgangstabel for varer mellem udenrigshandel og betalingsbalance efter poster, indtægt/udgift, land og tid
columns: post, indudbop, land, tid (time), indhold (unit Mio. kr.)
tid range: 2005-01-01 to 2025-08-01
</table>
<table>
id: vbbuhv
description: Versionstabel af BBUHV - Overgangstabel for varer mellem udenrigshandel og betalingsbalance efter version, poster, indtægt/udgift, land og tid
columns: version, post, indudbop, land, tid (time), indhold (unit Mio. kr.)
tid range: 2005-01-01 to 2025-08-01
</table>
<table>
id: bb2uhv
description: Korrektion af varer mellem udenrigshandel og betalingsbalance efter varebegreb, poster, im- og eksport, land og tid
columns: uhbegreb, post, indud, land, tid (time), indhold (unit Mio. kr.)
tid range: 2016-01-01 to 2025-08-01
</table>
</fact tables>

notes:
- Time granularity pattern: bbq=kvartalsvis (quarterly, 2005–), bby=årlig (annual, 2005–2024), vbbm=månedlig (monthly, 2005–) via version table. Suffix q=quarterly, y=yearly, m=monthly holds across these tables.
- Version tables (vbbm, vbbq, vbbuhv): each prefixed with 'v'. They store all historical revision vintages. For normal use, filter to MAX(version). For revision analysis (how did the estimate change over time?), keep all versions and compare.
- For current-account balance over time: use bbq (quarterly, no version overhead) or bby (annual, richest geographic breakdown). For monthly figures use vbbm (remember to filter version + enhed + saeson).
- For country-level geographic detail: bby is the only option — it has all 4 hierarchy levels (verdensdele → regioner → underregioner → individuelle lande). bbq and vbbq only have niveau 2 (regions) and niveau 4 (countries), while vbbm and bbuhv only have niveau 2.
- bbuhv / vbbuhv are reconciliation tables, not standard current-account tables. They explain the methodological gap between udenrigshandel statistics (CIF) and betalingsbalancen (FOB) for goods. Use these when a user asks about the difference between the two data series, not for standard balance of payments queries.
- bb2uhv compares two trade-measurement principles (Grænsepassage vs Ejerskifte) at goods-category level. Only total-world (W1). Use when asked about statistical methodology differences, not for standard queries.
- Common pitfalls for all tables: (1) post is hierarchical — parent codes are sums of children, never sum across all post values; (2) indudbop has N=K−D, never sum K+D+N; (3) land has extra aggregate codes (W1, I9, J9, P7 etc.) not in dim.lande_uht_bb — these can be used as inline filters.