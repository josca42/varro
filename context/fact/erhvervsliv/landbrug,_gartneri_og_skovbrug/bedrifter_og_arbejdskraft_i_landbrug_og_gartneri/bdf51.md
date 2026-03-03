table: fact.bdf51
description: Bedrifter efter område, udvalgte bedrifter afgrøder og husdyr og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- udbedrift: values [1000=Bedrifter i alt, 1010=Under 10,0 ha, 1020=10,0-19,9 ha, 1030=20,0-29,9 ha, 1040=30,0-49,9 ha ... 3100=Søer i alt, 3110=Svin i øvrigt, 3120=Svin i alt, 3130=Får i alt, 3140=Fjerkræ i alt]
- tid: date range 2010-01-01 to 2020-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 3 (kommuner). 93 out of 94 distinct omrade values match; only code 0 (Hele landet) is unmatched. Use ColumnValues("nuts", "titel", for_table="bdf51") to see the municipalities present.
- udbedrift encodes three completely independent breakdowns in one column — never sum across groups: 1xxx = farm size by cultivated area (1000=i alt, 1010-1080=size brackets); 2xxx = crop types; 3xxx = livestock types. Each group has its own total: 1000 for farm count total; 3120=Svin i alt, 3100=Søer i alt etc. for livestock.
- The same farm appears in both 2xxx (crops) and 3xxx (livestock) categories — these are not mutually exclusive subsets. Pick one category group per query.
- Data only runs 2010-2020. For more recent municipal agricultural data, there is no direct equivalent in this subject.
- Map: /geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.