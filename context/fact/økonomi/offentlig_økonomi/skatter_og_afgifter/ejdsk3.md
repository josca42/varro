table: fact.ejdsk3
description: Grundskyld efter område, ejendomstype og tid
measure: indhold (unit 1.000 kr.)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [3]
- ejentyp: values [1=Grundskyld i alt, 2=En-familiehuse, 3=To-familiehuse, 4=Tre-familiehuse, 5=Anden beboelse, 6=Landbrug mv., 7=Ejerlejligheder, 8=Sommerhuse, 9=Erhvervsejendomme, 10=Andre ejendomme]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade only has niveau=3 (kommuner). omrade='0.0' is a national total (not in dim.nuts).
- ejentyp=1 (Grundskyld i alt) = sum of ejentyp=2 through 10 (verified). For total grundskyld by kommune: WHERE ejentyp='1'. For breakdown by property type: filter individual ejentyp values.
- Only covers grundskyld (land tax), not dækningsafgifter. For full ejendomsskat picture use ejdsk1.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.0.
