table: fact.auh04
description: Offentligt forsørgede (fuldtidsmodtagere) efter område, ydelsestype, oprindelsesland, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2]
- ydelsestype: values [TOT=I alt, SU=SU-modtagere, TOTLE=Nettoledige i alt, FD=Feriedagpenge, TOTVO=Vejledning og opkvalificering i alt, TOTSB=Støttet beskæftigelse i alt, TOTAN=Barselsdagpenge mv. i alt, FP=Førtidspension, EL=Efterløn, AYD=Andre ydelsesmodtagere, SY=Sygedagpenge mv.]
- ieland: values [TOT=I alt, 30=Dansk oprindelse, UDL=Udenlandsk oprindelse i alt, 1=Vestlige lande, 2=Ikke-vestlige lande ... THA=Thailand, VIE=Vietnam, XXX=Statsløse, UOP=Uoplyst, UOPH=Uoplyst herkomst]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Annual version of auk04 (origin × benefit type, regional). Latest to 2024-01-01.
- omrade at landsdele level only (niveau=2, 11 landsdele). omrade='0' = Hele landet (not in dim.nuts).
- ieland: hierarchical codes — aggregates (TOT, 30=Dansk oprindelse, UDL, 1=Vestlige, 2=Ikke-vestlige) and individual country codes. Never sum across hierarchy levels.
- No alder column.
- Map: context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.
