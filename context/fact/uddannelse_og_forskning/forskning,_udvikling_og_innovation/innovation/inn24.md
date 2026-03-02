table: fact.inn24
description: Procesinnovative virksomheder efter branche og størrelsesgruppe, region, procesinnovationstype og tid
measure: indhold (unit Pct.)
columns:
- innbranche: values [1000=ALLE BRANCHER (DB07), 1010=Industri, 1015=Bygge og anlæg, 1020=Handel, 1025=Transport, 1030=Hotel, restauration, 1035=Information og kommunikation, 1040=Finansiering og forsikring, 1045=Erhvervsservice, 1050=Øvrige brancher, 1055=STØRRELSESGRUPPER I ALT (årsværk), 1060=Under 10 årsværk, 1065=10-49 årsværk, 1070=50-249 årsværk, 1075=250 årsværk og derover]
- region: join dim.nuts on region=kode; levels [1]
- innproces: values [470=Nye/forbedrede metoder til produktion af varer eller serviceydelser, 480=Metoder vedr. logistik, levering eller distribution, 490=Metoder til databehandling eller kommunikation, 500=Nye regnskabsmetoder eller andre administrative funktioner, 510=Nye forretningsgange, procedurer eller organisering af eksterne relationer, 520=Metoder til organisering af ansvar og beslutningskompetence eller personaleledelse, 530=Metoder til promovering af produkter, indpakning, prissætning, produkteksponering eller kundeservice]
- tid: date range 2020-01-01 to 2022-01-01
dim docs: /dim/nuts.md

notes:
- innbranche mixes two independent hierarchies: branch view (1000=ALLE BRANCHER total, 1010-1050=individual branches) and size group view (1055=STØRRELSESGRUPPER I ALT total, 1060-1075=individual size groups). Choose one view per query.
- region joins dim.nuts at niveau=1 (codes 81-85, the 5 regions). Code 0 = national total, not in dim.nuts.
- innproces has 7 process innovation categories (470-530). These cover different types of process innovation — check whether they're mutually exclusive or multi-select before summing. Each row is a share of procesinnovative firms. This table covers only procesinnovative firms; for the share of all firms that are procesinnovative, use inn22.
- All indhold values are percentages. Never sum across innbranche categories.
- Map: context/geo/regioner.parquet — merge on region=dim_kode. Exclude region='0'.