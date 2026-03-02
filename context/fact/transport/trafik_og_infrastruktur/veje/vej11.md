table: fact.vej11
description: Vejnet efter landsdel, vejtype og tid
measure: indhold (unit Km)
columns:
- landdel: join dim.nuts on landdel=kode; levels [2]
- vejtype: values [0=VEJNETTET I ALT, 10=Motorveje, 15=Motortrafikveje, 20=Øvrige veje, 25=STATSVEJE, 30=Motorveje, statslige, 35=Motortrafikveje , statslige, 40=Øvrige statsveje, 65=KOMMUNEVEJE, 66=Motorveje, kommunale, 67=Motortrafikveje, kommunale, 68=Øvrige kommunale veje, 70=ANDRE VEJE, 85=Storebæltsforbindelsen, 90=Øresundsmotorvejen, 91=E-VEJE]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- landdel joins dim.nuts at niveau=2 (11 landsdele). Code 0 is a national total not present in dim.nuts — omit it (WHERE f.landdel != '0') when joining, or handle separately. ColumnValues("nuts", "titel", for_table="vej11") will show the 11 regions.
- vejtype has a 3-level inline hierarchy. 0=total, 25/65/70 are mid-level subtotals, and 10/15/20/30/35/40/66/67/68/85/90/91 are detail codes. The three top-level categories are: 25=STATSVEJE (state roads), 65=KOMMUNEVEJE (municipal roads), 70=ANDRE VEJE (other roads). Summing vejtype without filtering silently double-counts — pick one level.
- For a simple total road length by region: filter vejtype='0' and landdel != '0'. For breakdown by road class: use vejtype IN ('25','65','70').
- Annual data from 2007, measure is km of road network.
- Map: context/geo/landsdele.parquet — merge on landdel=dim_kode. Exclude landdel='0'.