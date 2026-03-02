table: fact.ejdsk1
description: Ejendomsskatter efter område, skattetype og tid
measure: indhold (unit 1.000 kr.)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [3]
- skatter: values [1=Ejendomsskatter i alt, 2=Grundskyld, 3=Dækningsafgift af forretningsejendomme, 4=Dækningsafgift af offentlige ejendommes grundværdi, 5=Dækningsafgift af offentlige ejendommes forskelsværdi]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade only has niveau=3 (kommuner). omrade='0.0' is a national total (not in dim.nuts).
- skatter=1 (Ejendomsskatter i alt) = skatter=2+3+4+5 (verified). For total ejendomsskat by kommune: WHERE skatter='1'. For breakdown: filter to individual skatter values.
- Note: Grundskyld (skatter=2) dominates. Dækningsafgifter (3–5) are only levied in some kommuner; many will be zero.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.0.
