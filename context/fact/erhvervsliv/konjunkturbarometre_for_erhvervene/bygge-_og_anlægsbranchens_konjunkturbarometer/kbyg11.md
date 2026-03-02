table: fact.kbyg11
description: Udviklingsforløb for bygge og anlæg efter branche (DB07), indikator, bedømmelse, forløb og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db_10 on branche07=kode::text [approx]; levels [2]
- indikator: values [VIAK=Omsætning, BES=Beskæftigelse, PRIS=Tilbudspriser ved licitation]
- bedommelse: values [STØR=Stigende/forbedret, UÆNDR=Uændret, MINDRE=Faldende/forringet, NET=Nettotal]
- forlob: values [FAK=Faktisk (foregående 3 måneder), FOR=Forventet (kommende 3 måneder)]
- tid: date range 2005-01-01 to 2025-10-01
dim docs: /dim/db_10.md

notes:
- branche07 does NOT join dim.db_10 — the codes (F, 41000, 42000, 43003, 43201, 432200, 43301, 43302, 439910) are DST's own survey groupings for bygge og anlæg, not standard DB07 codes. Use ColumnValues("kbyg11", "branche07") to get labels. F = total sector, 41000 = Byggeentreprenører, 42000 = Anlægsentreprenører, 432200/439910/43201/43301/43302/43003 = specialised sub-branches.
- bedommelse contains NET which is derived (NET = %STØR − %MINDRE). Never sum across all bedommelse values — STØR+UÆNDR+MINDRE+NET are four views of the same responses, not independent categories. For trend analysis use NET only. Example: for Q4 2025, branche07=F, indikator=VIAK, forlob=FAK: STØR=9, UÆNDR=80, MINDRE=11, NET=−2.
- indikator is a measurement selector (VIAK/BES/PRIS are independent indicators). Always filter to one.
- forlob is a measurement selector (FAK = actual past 3 months, FOR = expected next 3 months). Always filter to one.
- To get a single series: filter branche07, indikator, bedommelse=NET, forlob to chosen values, then SELECT tid, indhold. No aggregation needed.