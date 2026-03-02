table: fact.ejerfof1
description: Husholdningernes formue i fast ejendom og gældskomponenter for familier efter komponenttype, bopælskommune, enhed, familietype og tid
measure: indhold (unit -)
columns:
- formgld: values [105=A. Fast ejendom, 110=A.1. Fast ejendom, ejere, 115=A.2. Fast ejendom, andelshavere, 135=B. Gæld, 140=B.1 Kreditforeningsgæld, 145=B.2 Lån i pengeinstitutter, 146=B.2.1 Prioritetsgæld i pengeinstitutter, 147=B.2.2 Andre lån i pengeinstitutter, 150=B.3 Pantebrevsgæld med pant i fast ejendom, 155=B.4 Anden gæld, 160=C. Beregnet friværdi (A.1 - B.1 - B.2.1 - B.3)]
- bopkom: join dim.nuts on bopkom=kode; levels [1, 3]
- enhed: values [105=Familier med fast ejendom (antal), 115=Total (Mio. kr.), 125=Gennemsnit (Kr.)]
- famtype: values [A0=A. FAMILIER I ALT, A1=B. ENLIGE I ALT, A11=Enlig  uden børn, under 35 år, A14=Enlig med børn, A12=Enlig uden børn, mellem 35-59 år, A13=Enlig uden børn, over 59 år, A2=C. PAR I ALT, A21=2 voksne uden børn, hovedperson under 35 år, A22=2 voksne uden børn, hovedperson mellem 35 - 59 år,, A23=2 voksne uden børn, hovedperson over 59 år,, A24=2 voksne med børn]
- tid: date range 2004-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- enhed is a measurement selector (105=Familier med fast ejendom antal, 115=Total mio. kr., 125=Gennemsnit kr.). Always filter to one — every row is repeated 3x.
- formgld is hierarchical. Aggregates: 105=A total (=110+115), 135=B total (=140+145+150+155), 145=B.2 subtotal (=146+147). Never sum all formgld codes — you'll double-count. Pick a single component or a single aggregate. 160=C is computed (friværdi = A.1 - B.1 - B.2.1 - B.3), not a sum.
- famtype is hierarchical: A0=alle familier, A1=enlige total (=A11+A12+A13+A14), A2=par total (=A21+A22+A23+A24). Filter to one level. Summing A0+A1+A2 triples counts.
- bopkom joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (99 kommuner). niveau 2 NOT present. bopkom='0' = national aggregate, not in dim.nuts.
- Use ColumnValues("nuts", "titel", for_table="ejerfof1") to see available regions/kommuner.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on bopkom=dim_kode. Exclude bopkom='0'.