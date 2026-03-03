table: fact.hjemsyg2
description: Leveret hjemmesygepleje (eget hjem) efter område, alder, køn, dage og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- alder1: values [50=Alder i alt, 100=Under 65 år, 375=65-69 år, 400=70-74 år, 500=75-79 år, 600=80-84 år, 700=85-89 år, 800=90 år og derover]
- koen: values [100=Mænd og kvinder i alt, 200=Mænd, 300=Kvinder]
- dage: values [252=Dage med hjemmesygepleje i alt, 353=Dage med hjemmesygepleje pr. borger (gennemsnit)]
- tid: date range 2016-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- dage is a measurement selector, not a category: 252=total days delivered, 353=average days per recipient. These are completely different units. Always filter to one value of dage — never sum or aggregate across both.
- To get "how many days of care" use dage=252. To get "how long does a typical recipient receive care" use dage=353.
- omrade joins dim.nuts at niveau 3 only (98 kommuner), same as hjemsyg. koen and alder1 include totals (koen=100, alder1=50) — filter both to avoid overcounting.
- A full unfiltered query has 4 overcounting axes: koen, alder1, dage, and the hierarchical totals in omrade (though omrade has no aggregates here). Minimal correct query: WHERE koen=100 AND alder1=50 AND dage=252 (or 353).
- Map: /geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.