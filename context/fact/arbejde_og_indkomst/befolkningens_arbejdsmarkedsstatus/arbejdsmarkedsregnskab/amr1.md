table: fact.amr1
description: Befolkningens tilknytning til arbejdsmarkedet (fuldtidspersoner) efter område, socioøkonomisk status, køn, alder og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- socio: values [21=Ordinær beskæftigelse i alt, 3=Støttet beskæftigelse med løn, 4=Midlertidigt fravær fra beskæftigelse, 50=Arbejdsløse, 80=Støttet beskæftigelse uden løn ... 150=Folkepension, 155=Anden pension, 165=Personer under uddannelse, 170=Børn og unge (ikke under uddannelse), 175=Øvrige uden for arbejdsstyrken]
- koen: values [M=Mænd, K=Kvinder]
- alder1: values [-15=Under 16 år, 16-19=16-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-66=65-66 år, 67-=67 år og derover]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts but code '0' (Hele landet) is NOT in the dim table and is silently dropped on join. Filter omrade='0' directly for national totals. For kommuner, join dim.nuts — all 99 matched codes are at niveau=3.
- Use ColumnValues("nuts", "titel", for_table="amr1") to browse the 99 kommuner. No regions (niveau=1) or landsdele present.
- The 26 socio codes are mutually exclusive and exhaustive — summing all codes for a given omrade/koen/alder1/tid gives the full population count for that cell (~5.94M nationally in 2023). socio=21 ("Ordinær beskæftigede i alt") is the single largest category (~2.4M) but is just one leaf. The "i alt" refers to all types of ordinary employment, not a population total.
- No aggregate rows for koen, alder1, or socio. koen has only M and K; alder1 has 13 age bands (-15 through 67-). Always sum all categories you don't filter on.
- Sample: total employed (socio='21') nationally in 2023: SELECT sum(indhold) FROM fact.amr1 WHERE omrade='0' AND socio='21' AND tid='2023-01-01' — result ~2.39M (M+K already covers all genders since there's no TOT row).
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade='0'.