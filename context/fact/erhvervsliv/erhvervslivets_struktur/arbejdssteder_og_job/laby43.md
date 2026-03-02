table: fact.laby43
description: Arbejdssteder, job og fuldtidsbeskæftigede efter kommunegruppe, branche (DB07), enhed og tid
measure: indhold (unit Antal)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- branche07: join dim.db on branche07=kode::text
- tal: values [ARBSTED=Arbejdssteder ultimo november, ANSATTE=Job ultimo november, FULDBESK=Fuldtidsbeskæftigede]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md, /dim/kommunegrupper.md

notes:
- `tal` is a measurement selector — every row is repeated 3 times (ARBSTED, ANSATTE, FULDBESK). Always filter to one value.
- branche07 uses DB07 section-letter codes: C=Fremstillingserhverv (industri), G=Engros- og detailhandel, I=Overnatningsfaciliteter og restauranter. The documented dim.db join is BROKEN — dim.db uses integer codes, not letters. Treat branche07 as an inline column with 3 values (C, G, I). No total/aggregate code for branche07.
- komgrp joins dim.kommunegrupper at niveau=1 (5 kommunegrupper: Hoved­stads­kommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner). komgrp='0' = Denmark total (not in dim).
- This table is uniquely suited for comparing FULDBESK (full-time equivalents) across municipality types within these 3 specific sectors. For broader sector/branch coverage use erhv1 or laby43 is the wrong table.