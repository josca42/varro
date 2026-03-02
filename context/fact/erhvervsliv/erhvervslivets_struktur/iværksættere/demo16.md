table: fact.demo16
description: Erhvervsdemografi efter branche (DB07 10-grp), enhed, startår og tid
measure: indhold (unit -)
columns:
- branchedb0710: join dim.db on branchedb0710=kode::text [approx]; levels [2, 3]
- enhed: values [NYE=Nye firmaer (antal), SURV=Overlevelsesprocent]
- startaar: values [2019=År 2019, 2020=År 2020, 2021=År 2021, 2022=År 2022, 2023=År 2023]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- This is a cohort survival table. startaar defines the founding cohort; tid is the observation year. For startaar=2019, SURV starts at 100 in 2019 and falls to ~52 by 2023 (52% of firms survived 4 years). NYE gives the absolute count of surviving firms from that cohort.
- enhed mixes counts and percentages: NYE=antal firmaer (count), SURV=overlevelsesprocent (%). NEVER sum across enhed — filter to one per query.
- branchedb0710 is documented as joining dim.db but actually joins dim.db_10 at niveau 1. Use: JOIN dim.db_10 d ON f.branchedb0710 = d.kode::text AND d.niveau = 1. Codes 1–11 plus TOT. The dim.db link (levels 2,3) is incorrect.
- Typical query pattern: pick one startaar, one enhed, and compare SURV across tid to see attrition — or pick one tid and compare across startaar cohorts.
- To compare survival across industries: WHERE enhed='SURV' AND startaar=2020 GROUP BY branchedb0710, tid.