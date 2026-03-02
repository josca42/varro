<fact tables>
<table>
id: nasl1
description: 1-2.1.1 Produktion, BVT og indkomstdannelse (hovedposter) efter transaktion, sektor og tid
columns: transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1971-01-01 to 2024-01-01
</table>
<table>
id: nasl2
description: 2.1.2-3.1 Indkomst, forbrug, opsparing og investering (hovedposter) efter transaktion, sektor og tid
columns: transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1971-01-01 to 2024-01-01
</table>
<table>
id: nkso1
description: 1-2.1.1 Produktion, BVT og indkomstdannelse (oversigtstabel) efter transaktion, sektor og tid
columns: transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1999-01-01 to 2025-04-01
</table>
<table>
id: nkso2
description: 2.1.2-3.1 Indkomst,forbrug, opsparing og investering (oversigtstabel) efter transaktion, sektor og tid
columns: transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1999-01-01 to 2025-04-01
</table>
<table>
id: nks3
description: 2.3 + 2.4.2 Korrigeret disponibel indkomst og faktisk forbrug (supplerende tabel) efter transaktion, sektor og tid
columns: transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1999-01-01 to 2025-04-01
</table>
<table>
id: naso1
description: 1-2.1.1 Produktion, BVT og indkomstdannelse (oversigtstabel) efter transaktion, sektor og tid
columns: transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: vnaso1
description: Versionstabel NASO1 - Produktion, BVT og indkomstdannelse (oversigtstabel) efter version, transaktion, sektor og tid
columns: version, transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: naso2
description: 2.1.2-3.1 Indkomst, forbrug, opsparing og investering (oversigtstabel) efter transaktion, sektor og tid
columns: transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: vnaso2
description: Versionstabel NASO2 - 2.1.2-3.1 Indkomst, forbrug, opsparing og investering (oversigtstabel) efter version, transaktion, sektor og tid
columns: version, transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: nasd11
description: 1 Produktion og BVT (detaljeret) efter transaktion, sektor og tid
columns: transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: nasd12
description: 2.1.1 Indkomstdannelse (detaljeret) efter transaktion, sektor og tid
columns: transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: nasd22
description: 2.2 Fordeling af 
sekundær indkomst (detaljeret) efter transaktion, sektor og tid
columns: transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: nasd23
description: 2.4.1 Anvendelse (forbrug og opsparing) af disponibel indkomst (detaljeret) efter transaktion, sektor og tid
columns: transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: nasd24
description: 3.1 Kapital, investering mv. (detaljeret) efter transaktion, sektor og tid
columns: transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: nas3
description: 2.3 + 2.4.2 Korrigeret disponibel indkomst og faktisk forbrug (supplerende tabel) efter transaktion, sektor og tid
columns: transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: vnas3
description: Versionstabel NAS3 - 2.3 + 2.4.2 Korrigeret disponibel indkomst og faktisk forbrug (supplerende tabel) efter version, transaktion, sektor og tid
columns: version, transakt, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: nask
description: Akkumulations- og statuskonti, investering og beholdning af faste aktiver, efter beholdning / strøm, aktiv, sektor og tid
columns: behold, aktiv, sektor, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: nasfk
description: Nationalregnskabets finansielle konti efter sektor, konto, balance, finansielt instrument, modpartssektor og tid
columns: sektornat, konto1, balance, finins, modseknat, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: nksfk
description: Nationalregnskabets finansielle konti efter sektor, konto, balance, finansielt instrument, modpartssektor og tid
columns: sektornat, konto1, balance, finins, modseknat, tid (time), indhold (unit Mio. kr.)
tid range: 1999-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- All tables use ESA sector codes without dots (S13 instead of S.13). Joining dim.esa requires: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. Several aggregate codes (S1=Hele økonomien, S1W=private sector, S1M=husholdninger+NPIsH) have no dim.esa entry — use ColumnValues("table_name", "sektor") to get their labels.

- Table naming pattern: NAS=annual, NKS=quarterly (kvartalsvis). Suffix 1=production/BVT/income formation (chapter 1-2.1.1), 2=income distribution/savings/investment (chapter 2.1.2-3.1), 3=adjusted income and actual consumption (chapter 2.3+2.4.2).

- For current production and BVT by sector: naso1 (annual, 1995-2024, 9 sectors) or nkso1 (quarterly, 1999-2025, 7 sectors). For finer financial subsector detail: nasd11. For the long run since 1971: nasl1 (only 4 aggregate sectors).

- For income, savings and investment by sector: naso2 (annual) or nkso2 (quarterly). Detailed breakdown: nasd12 (income formation), nasd22 (secondary income redistribution), nasd23 (use of income/savings), nasd24 (capital account and investment).

- For adjusted disposable income and actual consumption (including government services redistributed to households): nas3 (annual) or nks3 (quarterly).

- For capital stocks and investment flows: nask (annual 1995-2024). Specifies behold (LSN=opening stock, P51N=net investment, K3A7=other changes, LEN=closing stock) and aktiv (asset type). Never sum across behold values.

- For financial accounts (assets/liabilities by sector and financial instrument): nasfk (annual 1995-2024) or nksfk (quarterly 1999-2025). Both are 5-dimension tables (sektornat, konto1, balance, finins, modseknat) — all must be specified. Use modseknat='SALLE' for totals. Use konto1='U' for end-of-period stocks.

- Version tables (vnaso1, vnaso2, vnas3): identical to naso1/naso2/nas3 but include a version column for comparing across publication releases. Always filter to the latest version (V2024_JUN) unless doing revision analysis.

- Sector coverage varies by table: nasl1/nasl2 have only 4 aggregates (S1, S13, S1W, S2). Quarterly NKS tables have 7 sectors (no individual S14/S15). Annual NAS overview tables have 9 sectors (including S14, S15). NAS detailed tables add financial subsectors (S121, S122A123, S124-S129, S1311, S1313, S1314).