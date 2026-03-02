table: fact.laby15
description: Pensionformue for personer mindre end 5 år fra folkepensionsalderen (median) efter kommunegruppe og tid
measure: indhold (unit Kr.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- tid: date range 2014-01-01 to 2023-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp joins dim.kommunegrupper. Both hierarchy levels present: niveau=1 (5 kommunegrupper: Hovedstad, Storby, Provinsby, Opland, Land), niveau=2 (98 kommuner). Code 0 = "hele landet" aggregate (not in dim table). Filter d.niveau=1 for kommunegruppe comparison, d.niveau=2 for individual kommuner.
- indhold is the median pensionsformue in kr. for persons less than 5 years from folkepensionsalderen. Only one measure — no enhed selector.
- Very simple table: just komgrp and tid. Use it to compare pension preparedness across urban/rural municipality types for near-retirement cohort.
- For same cohort with age/gender breakdown use penfor11 (filtering alder to 60-64 or similar). laby15 gives a single annual median with finer geography.