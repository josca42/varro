table: fact.auk04
description: Offentligt forsørgede (fuldtidsmodtagere) efter område, ydelsestype, oprindelsesland, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2]
- ydelsestype: values [TOT=I alt, SU=SU-modtagere, TOTLE=Nettoledige i alt, FD=Feriedagpenge, TOTVO=Vejledning og opkvalificering i alt, TOTSB=Støttet beskæftigelse i alt, TOTAN=Barselsdagpenge mv. i alt, FP=Førtidspension, EL=Efterløn, AYD=Andre ydelsesmodtagere, SY=Sygedagpenge mv.]
- ieland: values [TOT=I alt, 30=Dansk oprindelse, UDL=Udenlandsk oprindelse i alt, 1=Vestlige lande, 2=Ikke-vestlige lande ... THA=Thailand, VIE=Vietnam, XXX=Statsløse, UOP=Uoplyst, UOPH=Uoplyst herkomst]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2025-04-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 2 only (11 landsdele). There is no national total in dim.nuts — omrade='0' = Hele landet but is not in dim. For regional breakdown simply join on niveau=2; for national total use omrade='0' directly without the join.
- ieland (oprindelsesland) has hierarchical aggregate codes mixed with individual country codes. Aggregates: TOT=I alt, 30=Dansk oprindelse, UDL=Udenlandsk oprindelse i alt, 1=Vestlige lande, 2=Ikke-vestlige lande. Individual country codes: AFG, POL, SOM, SYR, etc. Never sum across both aggregate and leaf codes.
- No alder column in this table. For age breakdown by origin use auk01 (no origin breakdown) — these cannot be combined in a single table.
- ydelsestype has 11 broad group codes (TOT, SU, TOTLE, FD, TOTVO, TOTSB, TOTAN, FP, EL, AYD, SY) — fewer and more aggregated than auk01.
- Quarterly data to 2025-04-01. For annual data use auh04.
- Map: /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.
