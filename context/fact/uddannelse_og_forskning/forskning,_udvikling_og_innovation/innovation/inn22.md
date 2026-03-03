table: fact.inn22
description: Innovative virksomheder efter branche og størrelsesgruppe, region, innovationstype og tid
measure: indhold (unit Pct.)
columns:
- innbranche: values [1000=ALLE BRANCHER (DB07), 1010=Industri, 1015=Bygge og anlæg, 1020=Handel, 1025=Transport, 1030=Hotel, restauration, 1035=Information og kommunikation, 1040=Finansiering og forsikring, 1045=Erhvervsservice, 1050=Øvrige brancher, 1055=STØRRELSESGRUPPER I ALT (årsværk), 1060=Under 10 årsværk, 1065=10-49 årsværk, 1070=50-249 årsværk, 1075=250 årsværk og derover]
- region: join dim.nuts on region=kode; levels [1]
- inno: values [130=Innovative i alt, 80=Produktinnovativ, 90=Procesinnovativ]
- tid: date range 2020-01-01 to 2022-01-01
dim docs: /dim/nuts.md

notes:
- innbranche mixes two independent hierarchies: branch view (1000=ALLE BRANCHER total, 1010-1050=individual branches) and size group view (1055=STØRRELSESGRUPPER I ALT total, 1060-1075=individual size groups). Choose one view per query; never mix rows from both.
- region joins dim.nuts at niveau=1 (the 5 regions, codes 81-85). Code 0 = national total, not in dim.nuts. Use WHERE f.region = '0' for national results or LEFT JOIN.
- inno is multi-select: a firm can be both produktinnovativ (80) and procesinnovativ (90). inno=130 (Innovative i alt) is the total (46%); 80+90=24+41=65% > 46%, confirming overlap. Use inno=130 for the headline share of innovative firms.
- All indhold values are percentages. Never sum across inno or innbranche categories.
- Map: /geo/regioner.parquet — merge on region=dim_kode. Exclude region='0'.