table: fact.laby23
description: Uddannelsesaktivitet i grundskolen (antal) efter status, uddannelse, grundskoleinstitutionstype, kommunegruppe og tid
measure: indhold (unit Antal)
columns:
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- uddannelse: values [TOT=I alt, U20=U20 0. klassetrin, U21=U21 1. klassetrin, U22=U22 2. klassetrin, U23=U23 3. klassetrin, U24=U24 4. klassetrin, U25=U25 5. klassetrin, U26=U26 6. klassetrin, U27=U27 7. klassetrin, U28=U28 8. klassetrin, U29=U29 9. klassetrin, U30=U30 10. klassetrin]
- grundskol: values [TOT=I alt, 1011=Efterskoler, 1012=Folkeskoler, 1013=Friskoler og private grundskoler, 1999=Andre skoler]
- komgrp: join dim.kommunegrupper on komgrp=kode [approx]; levels [1, 2]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp joins dim.kommunegrupper at niveau 1 (5 kommunegrupper) and niveau 2 (98 kommuner). Codes 0 (national), 411, 995, 998 are not in dim — skip when joining.
- 4 selector columns (fstatus, uddannelse, grundskol, komgrp) all have totals. For a simple national total: fstatus='B', uddannelse='TOT', grundskol='TOT', komgrp='0'.
- fstatus always needs filtering: B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang. Rows are tripled if not filtered.
- grundskol='TOT' in this table (vs grundskol='0' in uddakt20 — different coding for the total).