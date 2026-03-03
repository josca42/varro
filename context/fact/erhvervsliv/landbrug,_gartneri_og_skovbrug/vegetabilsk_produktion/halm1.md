table: fact.halm1
description: Halmudbytte og halmanvendelse efter område, afgrøde, enhed, anvendelse og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2]
- afgrode: values [H90=Alle afgrøder, H95=KORN I ALT, H110=Vinterhvede, H120=Vårhvede, H130=Rug, H140=Triticale, H150=Vinterbyg, H160=Vårbyg, H170=Havre, blandsæd og andet korn, H175=Majs til modenhed, H200=RAPS I ALT, H210=Vinterraps, H220=Vårraps, H300=BÆLGSÆD I ALT, H310=Markærter, H312=Hestebønner]
- enhed: values [10=Areal (1000 hektar), 50=Mængde (mio. kilo)]
- anvendelse: values [1010=Halm i alt, 1020=Til fyring, 1030=Til foder, 1040=Til strøelse m.v., 1050=Ikke bjerget]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. INNER JOIN gives 10 labeled geographies: niveau=1 (5 regioner: 81-85) and niveau=2 (5 landsdele: 4=Bornholm, 7=Fyn, 8=Sydjylland, 9=Østjylland, 10=Vestjylland). The remaining 6 landsdele (Copenhagen metro, Nordsjælland, etc.) are not present — these urban areas have little agricultural activity.
- omrade=0 is Hele landet (national total) and is NOT in dim.nuts. omrade=15 is an unmapped regional aggregate also absent from dim.nuts. Filter these out when joining, or handle separately for national totals.
- enhed is a measurement selector — 10=Areal (1000 ha), 50=Mængde (mio. kg). Both appear for the same omrade/afgrode/anvendelse/tid. Always filter to one.
- afgrode has a two-level hierarchy: H90=Alle afgrøder (grand total) = H95 (Korn i alt) + H200 (Raps i alt) + H300 (Bælgsæd i alt). Each IALT code also contains specific sub-crops (H110-H312). Don't sum across levels.
- anvendelse=1010 (Halm i alt) = sum of 1020 (fyring) + 1030 (foder) + 1040 (strøelse) + 1050 (ikke bjerget). Filter to one level to avoid double-counting.
- A fully filtered query needs: enhed=X, afgrode=single level, anvendelse=single level, omrade=specific region or INNER JOIN to dim.nuts.
- Map: /geo/landsdele.parquet (niveau 2) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.