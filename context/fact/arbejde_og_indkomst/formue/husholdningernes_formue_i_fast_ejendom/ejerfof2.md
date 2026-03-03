table: fact.ejerfof2
description: Husholdningernes formue i fast ejendom og gældskomponenter for familier efter komponenttype, bopælskommune, enhed, husstandsgrupper og tid
measure: indhold (unit -)
columns:
- formgld: values [105=A. Fast ejendom, 110=A.1. Fast ejendom, ejere, 115=A.2. Fast ejendom, andelshavere, 135=B. Gæld, 140=B.1 Kreditforeningsgæld, 145=B.2 Lån i pengeinstitutter, 146=B.2.1 Prioritetsgæld i pengeinstitutter, 147=B.2.2 Andre lån i pengeinstitutter, 150=B.3 Pantebrevsgæld med pant i fast ejendom, 155=B.4 Anden gæld, 160=C. Beregnet friværdi (A.1 - B.1 - B.2.1 - B.3)]
- bopkom: join dim.nuts on bopkom=kode; levels [1, 3]
- enhed: values [105=Familier med fast ejendom (antal), 115=Total (Mio. kr.), 125=Gennemsnit (Kr.)]
- husgrp: values [A0=A. SAMTLIGE FAMILIER, C0=B. HOVEDPERSONENS SOCIOØKONOMISK STATUS, C110=Selvstændige, C131=Lønmodtagere på højeste niveau, C132=Lønmodtagere på mellem niveau, C133=Lønmodtagere på grund niveau, C134=Lønmodtagere i øvrigt, C210=Arbejdsløse, C310=Uddannelsessøgende, C320=Pensionister og efterlønsmodtagere, C330=Øvrige ude af erhverv, D0=C. HOVEDPERSONENS UDDANNELSESNIVEAU, D10=Grundskole, D26=Gymnasiale uddannelser, D35=Erhvervsuddannelser, D40=Korte videregående uddannelser, D61=Mellemlange videregående uddannelser inkl. bachelor, D65=Lange videregående uddannelser, D9=Uoplyst]
- tid: date range 2004-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- enhed is a measurement selector (105=antal, 115=Total mio. kr., 125=Gennemsnit kr.). Always filter to one.
- formgld is hierarchical — same structure as ejerfof1: 105=A total (=110+115), 135=B total, 145=B.2 subtotal, 160=C friværdi. Never sum all formgld codes.
- husgrp mixes three independent breakdowns in one column. A0=alle familier, C0=total for socioøkonomisk status gruppe (equals A0), D0=total for uddannelse gruppe (equals A0). The sub-groups: C110-C330 are socioøkonomisk statuses; D10-D9 are uddannelsesniveauer. Pick exactly one breakdown at a time: either filter to A0, or filter to one C-sub-group, or filter to one D-sub-group. Summing A0+C0+D0 triples counts (they're all the same population total).
- bopkom joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (99 kommuner). niveau 2 NOT present. bopkom='0' = national aggregate, not in dim.nuts.
- Use ColumnValues("nuts", "titel", for_table="ejerfof2") to see available regions/kommuner.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on bopkom=dim_kode. Exclude bopkom='0'.