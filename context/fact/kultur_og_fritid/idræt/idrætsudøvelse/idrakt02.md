table: fact.idrakt02
description: Idrætsorganisationernes medlemskaber (andel af befolkningen) efter område, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- blstkom: join dim.nuts on blstkom=kode; levels [2, 3]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder1: values [TOT=Alder i alt, 0012=0-12 år, 1318=13-18 år, 1924=19-24 år, 2559=25-59 år, 6099=60 år og derover]
- tid: date range 2014-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- blstkom joins dim.nuts. Code 0 = national total (hele landet), not in dim.nuts. Fact table uses niveau 2 (11 landsdele) and niveau 3 (98 kommuner). Filter d.niveau to pick a single level.
- indhold is Pct. — the share of the population that are members of a sports organisation. Do not sum across blstkom values.
- 3 dimension columns (blstkom, kon, alder1). For national totals: blstkom='0', kon=10, alder1='TOT'.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/landsdele.parquet (niveau 2) — merge on blstkom=dim_kode. Exclude blstkom=0.