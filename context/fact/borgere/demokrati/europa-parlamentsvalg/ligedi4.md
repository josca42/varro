table: fact.ligedi4
description: Ligestillingsindikator for opstillede og valgte kandidater til Europa-Parlamentsvalg efter kandidater, indikator og tid
measure: indhold (unit -)
columns:
- kandidat: values [OK=Opstillede kandidater, VK=Valgte kandidater]
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- tid: date range 1994-01-01 to 2024-01-01

notes:
- kandidat (OK=opstillede, VK=valgte) represents two independent populations. Do not sum across kandidat values.
- indikator LA1 (mænd %) + LA2 (kvinder %) = 100 exactly. LA3 = LA1 - LA2 (derived gender gap in percentage points). Never sum all 3 indicators.
- Despite unit shown as "-", values are percentages for LA1/LA2 and percentage points for LA3.
- Typical query: SELECT tid, kandidat, indhold FROM fact.ligedi4 WHERE indikator = 'LA2' to track % women candidates/elected over time.