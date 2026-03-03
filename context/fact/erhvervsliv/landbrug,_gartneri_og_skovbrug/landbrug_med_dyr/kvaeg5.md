table: fact.kvaeg5
description: Kvægbestanden efter område, art og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2]
- dyr: values [D17=Kvæg i alt, D2=Tyre- og studekalve, - under 1/2 år, D3=Tyre- og studekalve, 1/2-1 år, D39=Tyre- og studekalve i alt, D4=Tyre og stude, 1-2 år, D5=Tyre og stude, 2- år og over, D52=Tyre og stude i alt, D53=Handyr, kvæg i alt, D6=Kviekalve, under 1/2 år, D7=Kviekalve, 1/2-1 år, D72=Kviekalve i alt, D8=Kvier, 1-2 år drægtige , D10=Kvier, 1-2 år i alt, D11=Kvier, 2 år og over, drægtige , D13=Kvier, 2 år og over, i alt, D136=Kvier i alt, D14=Malkekøer, D15=Ammekøer, KKIALT=Køer i alt, D16=Hundyr, kvæg i alt]
- tid: date range 2008-01-01 to 2025-07-01
dim docs: /dim/nuts.md

notes:
- No enhed selector — indhold is always animal count (Antal). One row per omrade×dyr×tid.
- dyr has 20 values, all kvæg categories: D17=Kvæg i alt (overall total), then handyr subtypes (D2,D3,D39,D4,D5,D52,D53), hundyr subtypes (D6,D7,D72,D8,D10,D11,D13,D136,D16), and D14=Malkekøer, D15=Ammekøer, KKIALT=Køer i alt. Hierarchical: D17 > D53/D16 > individual types. Filter to D17 for total kvæg count.
- omrade has 12 values; 10 join to dim.nuts (5 regioner niveau 1, 5 landsdele niveau 2). Code 0=Hele landet and code 15=merged Copenhagen-area landsdel don't join. Same pattern as hdyr07.
- Most up-to-date kvæg table (to 2025). Simpler than hdyr07 — kvæg only, no enhed selector, no herd-size groups.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade IN (0, 15).