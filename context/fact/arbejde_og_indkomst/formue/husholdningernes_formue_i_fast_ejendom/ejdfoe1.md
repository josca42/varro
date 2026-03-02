table: fact.ejdfoe1
description: Formue i fast ejendom efter værdisætning, bopælskommune, enhed, ejendomstype og tid
measure: indhold (unit -)
columns:
- vaerdi: values [100=Markedsværdi, 105=Offentlig ejendomsvurdering]
- bopkom: join dim.nuts on bopkom=kode; levels [1, 3]
- enhed: values [100=Ejendomme (Antal), 110=Total (mio. kr.), 120=Gennemsnit (Kr.)]
- ejentyp: values [T=FAST EJENDOM I ALT, A=A. Enfamiliehuse, B=B. Ejerlejligheder, C=C. Flerfamiliehuse, D=D. Andelsboliger, E=E. Beboelsesejendomme forbundet med erhverv, F=F. Andre beboelsesejendomme, G=G. Bebyggede landbrug, H=H. Sommerhuse mm., I=I. Grunde, landbrugsarealer og naturområder, J=J. Erhvervsejendomme, K=K. Anden fast ejendom]
- tid: date range 2004-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- vaerdi is a measurement selector (100=Markedsværdi, 105=Offentlig ejendomsvurdering). Always filter to one value — every row exists twice, once per valuation method.
- enhed is a measurement selector (100=Antal ejendomme, 110=Total mio. kr., 120=Gennemsnit kr.). Always filter to one. Combining units silently triples counts.
- ejentyp=T is the aggregate (FAST EJENDOM I ALT). It equals the sum of A-K. Filter to either T or individual types, never both.
- bopkom joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (99 kommuner). niveau 2 (landsdele) is NOT present. bopkom='0' is the national aggregate — it has no match in dim.nuts (use WHERE bopkom='0' directly for national totals).
- Use ColumnValues("nuts", "titel", for_table="ejdfoe1") to see the 103 joinable regions/kommuner.
- Minimal working query: filter vaerdi, enhed, ejentyp, and d.niveau to avoid 6x overcounting.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on bopkom=dim_kode. Exclude bopkom='0'.