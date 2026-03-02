table: fact.ilon12
description: Implicit lønindeks for virksomheder og organisationer efter branche, sæsonkorrigering og tid
measure: indhold (unit Indeks)
columns:
- erhverv: join dim.db on erhverv=kode::text; levels [2]
- saeson: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 2005-01-01 to 2025-04-01
dim docs: /dim/db.md
notes:
- WARNING: The documented dim.db join (erhverv=kode::text) is WRONG. The erhverv codes are DST custom groupings (C=all manufacturing, CA/CB/.../CM=manufacturing sub-sectors, G/H/I/M/N/S=service sections, TOT=overall) that do not correspond to dim.db entries. Use ColumnValues("ilon12", "erhverv") for correct labels (37 codes).
- saeson is a measurement-type selector: EJSÆSON=not seasonally adjusted, SÆSON=seasonally adjusted. ALWAYS filter to one value — every industry appears twice. For most analyses, use EJSÆSON unless comparing across quarters.
- This table covers only virksomheder og organisationer (private sector). Quarterly index from 2005. indhold is an index value (base year implied), not a kr/hour figure.
- For a simple private-sector wage index: WHERE saeson='EJSÆSON' AND erhverv='TOT', ORDER BY tid.
