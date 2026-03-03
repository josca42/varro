table: fact.indkf122
description: Familiernes indkomst i alt efter område, enhed, familietype, indkomstinterval og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- enhed: values [102=Familier i gruppen (Antal), 110=Indkomstbeløb (1.000 kr.), 117=Gennemsnit for familier i gruppen (kr.)]
- famtyp: values [FAIA=Familier i alt, PAIA=Par i alt, ENIA=Enlige i alt]
- indkintb: values [99=I alt, 800=Under 200.000 kr., 810=200.000 - 299.999 kr., 815=300.000 - 399.999 kr., 820=400.000 - 499.999 kr., 600=500.000 - 599.999 kr., 700=600.000 - 699.999 kr., 710=700.000 - 799.000 kr., 715=800.000 - 899.000 kr., 720=900.000 - 999.000 kr., 725=1 million kr. og derover]
- tid: date range 1987-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 3 only (kommuner). No region or landsdel here — use indkf102 for those.
- omrade='0' is national aggregate, not in dim.nuts.
- indkintb total code is '99' (not '0' like person tables). Brackets in 100k steps from 200k up to 1M+.
- famtyp: only 3 types (FAIA, PAIA, ENIA). Filter to one.
- enhed selector (3 types). Always filter to one.
- Covers indkomst i alt (before tax). For disponibel by kommune use indkf132 (identical structure).
- Map: /geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
