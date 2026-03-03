table: fact.regn80
description: Regnskabsstatistik for private byerhverv i mio. kr. (DB07) efter område, branche, regnskabsposter og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2]
- erhverv: join dim.db on erhverv=kode::text [approx]; levels [2]
- regnskposter: values [XOM_M=Omsætning, XVAMV_M=Vareforbrug mv., XBF_M=Bruttofortjeneste, XINV_M=Investeringer, netto, XBA_P=Bruttoavance i pct., ANTAL=Antal arbejdssteder, VAERK=Antal ansatte (årsværk)]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md, /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 2 (11 landsdele, koder 1-11). Code "0" = Hele landet (national total) — not in dim.nuts. Join: JOIN dim.nuts d ON f.omrade::integer = d.kode AND d.niveau = 2. Filter WHERE omrade != '0' to get regional data only.
- erhverv same mixed letter+number codes as regn50 (B, C, D, E, F, 45, 46, 47, H, I, J, L, M, N, 95 + two totals: "0"=I alt and "TOTREG80"=I alt excl. råstofudvinding og energiforsyning). Use ColumnValues("regn80", "erhverv").
- regnskposter has only 7 measures (vs. 30+ in regn50): XOM_M=Omsætning, XVAMV_M=Vareforbrug mv., XBF_M=Bruttofortjeneste, XINV_M=Investeringer netto, XBA_P=Bruttoavance i pct., ANTAL=Antal arbejdssteder, VAERK=Antal ansatte årsværk. Note XBA_P is a percentage while the others are mio. kr. or counts — MUST filter regnskposter.
- This is the only regnskab table with regional breakdown. For national totals by sector, regn50 has a fuller set of measures; use regn80 only when you need the geographical dimension.
- Three-column filter required: regnskposter + omrade + erhverv. Omitting any one multiplies row count.
- Map: /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.
