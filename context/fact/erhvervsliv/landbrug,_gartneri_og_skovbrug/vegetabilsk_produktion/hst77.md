table: fact.hst77
description: Høstresultat efter område, afgrøde, enhed og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2]
- afgrode: values [H100=KORN (KERNE) I ALT, H110=Vinterhvede, H120=Vårhvede, H130=Rug, H140=Triticale ... H620=Majs til ensilering, H630=Korn til ensilering, H650=Græs og kløver i omdriften, H660=Græs uden for omdriften, H685=Efterslæt efter korn og helsæd]
- maengde4: values [10=Areal (1000 hektar), 20=Gennemsnitsudbytte (hkg pr. hektar), 30=Produktion (mio. kg), 40=Foderværdi (mio. FE), 45=100 FE pr. hektar]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. INNER JOIN gives 10 labeled geographies: niveau=1 (5 regioner: 81-85) and niveau=2 (5 landsdele: 4=Bornholm, 7=Fyn, 8=Sydjylland, 9=Østjylland, 10=Vestjylland). Urban landsdele are absent (low agricultural activity). omrade=0 = Hele landet (not in dim.nuts), omrade=15 = unmapped aggregate (not in dim.nuts).
- maengde4 is a measurement selector — 5 different measures appear for the same omrade/afgrode/tid: 10=Areal (1000 ha), 20=Gennemsnitsudbytte (hkg/ha), 30=Produktion (mio. kg), 40=Foderværdi (mio. FE), 45=100 FE pr. hektar. Always filter to one.
- afgrode has aggregate codes: H100=KORN (KERNE) I ALT, H200=RAPS I ALT, H300=BÆLGSÆD I ALT alongside specific crops. Also H600-H685 are fodder/green mass categories. Don't sum across afgrode levels.
- A correct query requires: maengde4=single measure, afgrode=single level, and either omrade=0 for national or INNER JOIN dim.nuts for regional breakdown.
- Map: /geo/landsdele.parquet (niveau 2) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.