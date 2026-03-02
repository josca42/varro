table: fact.kohort01
description: Kumulerede fertilitetskvotienter for kvinders fødselsårgange efter fødselsår, alder og tid
measure: indhold (unit Pr. 1.000 kvinder)
columns:
- fodaar: values [1940-1941=1940-1941, 1941-1942=1941-1942, 1942-1943=1942-1943, 1943-1944=1943-1944, 1944-1945=1944-1945 ... 2005=2005, 2006=2006, 2007=2007, 2008=2008, 2009=2009]
- alder: values [1515=15 år, 1516=15-16 år, 1517=15-17 år, 1518=15-18 år, 1519=15-19 år ... 1545=15-45 år, 1546=15-46 år, 1547=15-47 år, 1548=15-48 år, 1549=15-49 år]
- tid: date range 2023-01-01 to 2024-01-01

notes:
- This table contains CUMULATIVE cohort fertility, not period fertility rates. Each row shows how many births per 1.000 women in a given birth cohort have occurred by a given age.
- alder is encoded as 15XX: 1515 = at age 15, 1516 = cumulative through age 16, ..., 1549 = cumulative through age 49 (completed cohort fertility). To compare completed fertility across generations, use WHERE alder='1549' — but only for cohorts born early enough to have passed age 49 (roughly fodaar ≤ 1974).
- fodaar covers two-year cohorts (e.g. '1940-1941') for older generations and single years (e.g. '2005') for recent ones. When querying a specific birth year, note that some early cohorts use the two-year format.
- Only 2 tid values (2023, 2024), so every (fodaar, alder) combination appears twice. Always filter to a single tid value to avoid doubling results.
- Use for: how many children has a generation had by age X? How does completed fertility differ across birth cohorts?