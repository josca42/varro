table: fact.demo11
description: Erhvervsdemografi efter branche (DB07 127-grp), status, enhed og tid
measure: indhold (unit Antal)
columns:
- branchedb07127: join dim.db on branchedb07127=kode::text [approx]; levels [5]
- fstatus: values [OPH=Ophørte firmaer (antal), NYE=Nye firmaer (antal)]
- enhed: values [HAA=Heraf med ansatte (antal), NYE1=Firmaer (antal)]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- branchedb07127 does NOT join reliably to dim.db — only 12 of 128 codes match by coincidence. The 127-grouping is DST's own internal classification (5-digit zero-padded codes like 01000, 10001) that does not align with the dim.db hierarchy. Use ColumnValues("demo11", "branchedb07127") to get the full list of codes with Danish labels (e.g. 01000="Landbrug og gartneri", 10001="Slagterier").
- fstatus separates NEW from CLOSING firms: NYE=Nye firmaer, OPH=Ophørte firmaer. These are independent counts — never sum across fstatus values.
- enhed: HAA (Heraf med ansatte) is a SUBSET of NYE1 (Firmaer i alt). Do not sum HAA + NYE1; pick one. To see all firms use NYE1; to see only employer firms use HAA.
- For a simple count query: filter fstatus AND enhed each to one value, then group by branchedb07127 and/or tid.