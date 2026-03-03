<fact tables>
<table>
id: regnla4
description: Regnskabsstatistik for primære erhverv efter branche (DB07), regnskabsposter og tid
columns: branche07, regnskposter, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: regnla5
description: Nøgletal i procent for regnskabsstatistik for primære erhverv efter branche (DB07), regnskabsposter og tid
columns: branche07, regnskposter, tid (time), indhold (unit Pct.)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: regn50
description: Regnskabsstatistik for private byerhverv i mio. kr. efter branche, regnskabsposter og tid
columns: erhverv, regnskposter, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: regn50a
description: Nøgletal i procent for regnskabsstatistik for private byerhverv efter branche, regnskabsposter og tid
columns: erhverv, regnskposter, tid (time), indhold (unit Pct.)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: regn10
description: Regnskabsstatistik for private byerhverv i mio. kr. efter branche, regnskabsposter og tid
columns: erhverv, regnskposter, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: regn10a
description: Nøgletal i procent for regnskabsstatistik for private byerhverv efter branche, regnskabsposter og tid
columns: erhverv, regnskposter, tid (time), indhold (unit Pct.)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: regn20
description: Regnskabsstatistik for private byerhverv efter branche, regnskabsposter, størrelse og tid
columns: erhverv, regnskposter, storrelse, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: fregn20
description: Foreløbig regnskabsstatistik for private byerhverv efter branche, regnskabsposter, størrelse og tid
columns: erhverv, regnskposter, storrelse, tid (time), indhold (unit -)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: regn20a
description: Nøgletal i procent for regnskabsstatistik for private byerhverv efter branche, regnskabsposter, størrelse og tid
columns: erhverv, regnskposter, storrelse, tid (time), indhold (unit Pct.)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: fregn30
description: Foreløbig regnskabsstatistik for private byerhverv efter branche, regnskabsposter, ejerform og tid
columns: erhverv, regnskposter, ejerform, tid (time), indhold (unit -)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: regn30
description: Regnskabsstatistik for private byerhverv i mio. kr. efter branche, regnskabsposter, ejerform og tid
columns: erhverv, regnskposter, ejerform, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: regn30a
description: Nøgletal i procent for regnskabsstatistik for private byerhverv efter branche, regnskabsposter, ejerform og tid
columns: erhverv, regnskposter, ejerform, tid (time), indhold (unit Pct.)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: regn80
description: Regnskabsstatistik for private byerhverv i mio. kr. (DB07) efter område, branche, regnskabsposter og tid
columns: omrade, erhverv, regnskposter, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: atf1
description: Virksomheder, der søgte finansiering efter branche (DB07), finansieringsaktivitet, population og tid
columns: branche07, finakt, popu, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2018-01-01
</table>
<table>
id: atf2
description: Virksomheder, der søgte finansieringsformen efter finansieringsform, udfald, population og tid
columns: finform, udfald, popu, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2018-01-01
</table>
<table>
id: atf3
description: Virksomheder, der søgte finansiering hos lånefinansieringskilden efter lånefinansieringskilde, udfald, population og tid
columns: laanefin, udfald, popu, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2018-01-01
</table>
</fact tables>
notes:
- Common structure across all regnskab tables: regnskposter is ALWAYS a measure-selector column (not a dimension). Every (branche/erhverv/storrelse/ejerform/omrade, tid) combination repeats once per regnskabspost. MUST filter to a single regnskposter value or you mix units (antal firmaer, mio. kr., 1000 kr., pct.) and get inflated counts.

- Table selection by subject:
  - Primary industries (landbrug, fiskeri, skovbrug): regnla4 (absolute, 2008-2023) or regnla5 (ratios %).
  - Private urban industries, broad sector overview: regn50 (absolute), regn50a (ratios) — 16 sectors, 2019-2023.
  - Private urban industries, very detailed branches: regn10 (absolute), regn10a (ratios) — 101 sub-branches, 2019-2023.
  - Private urban industries + size breakdown: regn20 (absolute), regn20a (ratios).
  - Private urban industries + legal form breakdown: regn30 (absolute), regn30a (ratios).
  - Regional breakdown by landsdel: regn80 (absolute only, 7 measures, 11 landsdele, 2019-2023).
  - Preliminary data for latest year (2023): fregn20 (with size), fregn30 (with legal form) — limited to 8 measures.
  - Financing survey (outdated, ends 2018): atf1 (sector), atf2 (financing form outcomes), atf3 (loan source outcomes).

- Map: regn80 supports choropleth at landsdel level — /geo/landsdele.parquet, merge on omrade=dim_kode. Only table in this group with a geographic dimension.

- Naming pattern: suffix "a" = nøgletal i procent (ratio/percentage variant), prefix "f" = foreløbig (preliminary). regn50/regn50a, regn20/regn20a, regn30/regn30a, regn10/regn10a all share this pattern.

- erhverv column in private byerhverv tables (regn50, regn10, regn20, regn30, regn80): two different coding schemes are used. regn50/regn20/regn30/regn80 use a 16-code mixed scheme (DB07 section letters + a few numeric codes); regn10/regn10a uses 101 NR-branche derived numeric codes. Neither scheme joins cleanly to a standard dim table — use ColumnValues("table", "erhverv") to browse codes.

- branche07 in regnla4/regnla5: DB07 codes stored with leading zeros ("011100") that must be stripped to join dim.db ("11100"). Join: LTRIM(f.branche07, '0') = d.kode::text.

- All regnskab tables contain overlapping aggregate and detail codes. Never sum across all erhverv/branche07 values — use the total code (TOTR, "A", or "0") or filter to a consistent hierarchy level.
