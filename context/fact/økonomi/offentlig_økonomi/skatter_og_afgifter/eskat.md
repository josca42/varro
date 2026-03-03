table: fact.eskat
description: Beskatningsværdier og ejendomsskatter efter område, beskatningsgrundlag og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [3]
- skatgrl: values [3=Afgiftspligtig grundværdi (mio. kr.), 2=Forskelsværdi (mio. kr.), 1=Ejendomsværdi (mio. kr.), 4=Ejendomsskatter i alt (1.000 kr)]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade only has niveau=3 (kommuner). omrade='0.0' is a national total (not in dim.nuts). Use ColumnValues("nuts","titel",for_table="eskat") to see the 98 kommuner.
- skatgrl has 4 values with completely different units: 1/2/3 are property values in mio. kr., 4 is taxes paid in 1.000 kr. Never sum or mix across skatgrl. The unit column header '-' reflects this mix.
- Typical use: pick one skatgrl per query. For total property tax paid by kommune: WHERE skatgrl='4'. For the taxable land value base: WHERE skatgrl='3'.
- Map: /geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.0.
