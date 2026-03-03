table: fact.sygedp01
description: Sygedagpenge efter kommune, køn, alder, ydelsesmodtager, enhed og tid
measure: indhold (unit -)
columns:
- dffekom: join dim.nuts on dffekom=kode; levels [2, 3]
- koen: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alerams: values [IALT=Alder i alt, -19=Under 20 år, 20-29=20-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 7099=70 år og derover]
- ydelsesmodtager: values [TOT=Modtagere i alt, LTOT=Lønmodtagere i alt, LR=Lønmodtagere med løn (refusion), LD=Lønmodtagere uden løn (dagpenge), SELV=Selvstændige, LED=Ledige]
- maengde6: values [0=Personer (antal), 5=Fuldtidspersoner (antal), 10=Dage (antal), 15=Beløb (tusind kr.), 20=Personer, delvist genoptaget arbejde (antal), 25=Fuldtidspersoner, delvist genoptaget arbejde (antal)]
- tid: date range 2020-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- maengde6 is a measurement selector — every dimension combination is repeated for all 6 measurement types (personer, fuldtidspersoner, dage, beløb, delvist-genoptaget variants). Always filter to one value, e.g. WHERE maengde6 = 0 (personer) or maengde6 = 5 (fuldtidspersoner). Omitting this inflates sums 6x.
- ydelsesmodtager has hierarchical totals: TOT = LTOT + SELV + LED, and LTOT = LR + LD. For overall counts use TOT; to break down by recipient type use LR, LD, SELV, LED — never sum across all values.
- koen and alerams both have total rows (koen=10, alerams=IALT). When not breaking down by these dimensions, always filter to their totals to avoid double-counting.
- dffekom joins dim.nuts at niveau 2 (11 landsdele) and niveau 3 (98 kommuner). Niveau 1 (regioner) is absent. Code '0' is a national total not in dim.nuts — use it directly for landstotaler or exclude it when joining to the dim. Use ColumnValues("nuts", "titel", for_table="sygedp01") to see the available codes.
- To get a clean count of sick-pay recipients by kommune: filter maengde6=0, koen=10, alerams='IALT', ydelsesmodtager='TOT', and d.niveau=3 in the dim join.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/landsdele.parquet (niveau 2) — merge on dffekom=dim_kode. Exclude dffekom='0'.