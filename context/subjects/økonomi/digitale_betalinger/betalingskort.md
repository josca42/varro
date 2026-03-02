<fact tables>
<table>
id: dnbsup
description: Dansk udstedte kort efter type, kortholder og tid
columns: kortype, privaterhverv, tid (time), indhold (unit 1.000 stk.)
tid range: 2016-01-01 to 2025-04-01
</table>
<table>
id: dnbsuk
description: Dansk udstedte kort efter type, teknologi og tid
columns: kortype, korttek, tid (time), indhold (unit 1.000 stk.)
tid range: 2016-01-01 to 2025-04-01
</table>
<table>
id: dnbsmis
description: Kortmisbrug efter type, kategori, land, datatype og tid
columns: kortype, misbrug2, nation, data, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2025-07-01
</table>
<table>
id: dnbstk
description: Transaktioner i Danmark med dansk udstedte kort efter type, teknologi, datatype og tid
columns: kortype, korttek, data, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2025-04-01
</table>
<table>
id: dnbsts
description: Transaktioner med kort efter type, anvendelsessted, land, datatype og tid
columns: kortype, anvsted, nation, data, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2025-07-01
</table>
<table>
id: dnbstp
description: Transaktioner med dansk udstedte kort efter type, kortholder, datatype og tid
columns: kortype, privaterhverv, data, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2025-04-01
</table>
<table>
id: dnbsk1
description: Transaktioner med kort i Danmark efter transaktionstype, kortudstedelsesland, datatype og tid
columns: transakt1, kortudsted, data, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2025-10-12
</table>
</fact tables>

notes:
- All tables share kortype as a 3-level hierarchy: BTK (total) → DEBK/KREK (debet/kredit subtotals) → DANK/CODANK/INTDEBK/INTKREK (leaf types). Always pick one level when querying — summing across levels double-counts.
- Five tables (dnbsmis, dnbstk, dnbsts, dnbstp, dnbsk1) have a `data` measurement selector column. Forgetting to filter it multiplies row counts by 2–4x. dnbsk1 uses BELOEB/ANTAL (not A/V like the others).
- Card counts vs transactions: dnbsup (cards by holder type) and dnbsuk (cards by technology) measure how many cards exist. All other tables measure transactions.
- For total transaction volume over time: dnbstk (by technology) or dnbstp (by holder type) — both cover 2016–2025, Danish-issued cards in Denmark only.
- For e-commerce vs physical shop breakdown: dnbsts — this is the only table with anvsted (usage venue). Also covers foreign cards (UDLKORT) and has a nation column. Be aware that anvsted='DKSB' has no UDL data.
- For POS vs online (CNP) split with foreign-card data: dnbsk1 — starts 2019, higher time resolution (daily), values in raw kr./stk. not 1.000 stk./mio. kr.
- For card fraud: dnbsmis — 4-value data column (counts, values, and promille shares), complex misbrug2 hierarchy, covers both Danish and foreign cards.
- For contactless/NFC adoption: dnbsuk (card counts by tech) or dnbstk (transactions by tech), both have korttek='NFCKORT'.
- dnbsk1 is the only table capturing foreign-issued cards used in Denmark (kortudsted='UDL') — useful for total market coverage of Danish terminals.