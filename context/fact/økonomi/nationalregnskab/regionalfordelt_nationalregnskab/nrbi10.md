table: fact.nrbi10
description: Investeringer (10a3-gruppering) efter område, branche, prisenhed og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- branche: values [V=I alt, VA=A Landbrug, skovbrug og fiskeri, VB=B Råstofindvinding, VC=C Industri, VD_E=D_E Forsyningsvirksomhed, VF=F Bygge og anlæg, VG_I=G_I Handel og transport mv., VJ=J Information og kommunikation, VK=K Finansiering og forsikring, VLA=LA Ejendomshandel og udlejning af erhvervsejendomme, VLB=LB Boliger, VM_N=M_N Erhvervsservice, VO_Q=O_Q Offentlig administration, undervisning og sundhed, VR_S=R_S Kultur, fritid og anden service]
- prisenhed: values [V_T=Løbende priser, (mio. kr.), V_C=Pr. indbygger, løbende priser, (1000 kr.), LRG_T=2020-priser, kædede værdier, (mio. kr.), LRG_C=Pr. indbygger, 2020-priser, kædede værdier, (1000 kr.)]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts but codes 0 (hele landet) and 999 (ikke regionalfordelt) are NOT in the dim. Exclude both when doing regional analysis.
- omrade uses only niveau 1 (5 regioner: 81–85) — no landsdel breakdown in this table. Use WHERE f.omrade IN (81,82,83,84,85) or JOIN dim.nuts d ON f.omrade=d.kode WHERE d.niveau=1.
- prisenhed is a measurement selector — the same (omrade, branche, tid) combination appears 4 times. Always filter to one prisenhed: V_T (løbende priser, mio. kr.) or LRG_T (2020-priser, kædede værdier).
- branche=V is the "I alt" total. Do not sum branche='V' together with individual branches.
- Shortest time range in the subject (2000–2023) and coarsest geography (region only, no landsdele).
- Map: /geo/regioner.parquet — merge on omrade=dim_kode. Exclude omrade IN (0, 999).