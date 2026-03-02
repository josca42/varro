table: fact.inn23
description: Produktinnovative virksomheder efter branche og størrelsesgruppe, region, produktinnovationstype og tid
measure: indhold (unit Pct.)
columns:
- innbranche: values [1000=ALLE BRANCHER (DB07), 1010=Industri, 1015=Bygge og anlæg, 1020=Handel, 1025=Transport, 1030=Hotel, restauration, 1035=Information og kommunikation, 1040=Finansiering og forsikring, 1045=Erhvervsservice, 1050=Øvrige brancher, 1055=STØRRELSESGRUPPER I ALT (årsværk), 1060=Under 10 årsværk, 1065=10-49 årsværk, 1070=50-249 årsværk, 1075=250 årsværk og derover]
- region: join dim.nuts on region=kode; levels [1]
- innpro: values [170=Kun vareinnovation, 180=Både vare- og serviceinnovation, 190=Kun serviceinnovation]
- tid: date range 2020-01-01 to 2022-01-01
dim docs: /dim/nuts.md

notes:
- innbranche mixes two independent hierarchies: branch view (1000=ALLE BRANCHER total, 1010-1050=individual branches) and size group view (1055=STØRRELSESGRUPPER I ALT total, 1060-1075=individual size groups). Choose one view per query.
- region joins dim.nuts at niveau=1 (codes 81-85, the 5 regions). Code 0 = national total, not in dim.nuts.
- innpro has 3 mutually exclusive product innovation types: 170=vareinnovation only, 180=both vare- og serviceinnovation, 190=serviceinnovation only. These sum to ~100% for product-innovative firms. This table covers only produktinnovative firms (a subset); for the share of all firms that are produktinnovative, use inn22.
- All indhold values are percentages. Never sum innpro categories (they already cover 100%).
- Map: context/geo/regioner.parquet — merge on region=dim_kode. Exclude region='0'.