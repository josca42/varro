table: fact.nrbp10
description: 1-2.1.1 Produktion, BVT og indkomstdannelse (10a3-gruppering) efter område, transaktion, branche, prisenhed og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- transakt: values [P1K=P.1 Produktion, P2D=P.2 Forbrug i produktionen, B1GD=B.1g Bruttoværditilvækst, BVT, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst]
- branche: values [V=I alt, VA=A Landbrug, skovbrug og fiskeri, VB=B Råstofindvinding, VC=C Industri, VD_E=D_E Forsyningsvirksomhed, VF=F Bygge og anlæg, VG_I=G_I Handel og transport mv., VJ=J Information og kommunikation, VK=K Finansiering og forsikring, VLA=LA Ejendomshandel og udlejning af erhvervsejendomme, VLB=LB Boliger, VM_N=M_N Erhvervsservice, VO_Q=O_Q Offentlig administration, undervisning og sundhed, VR_S=R_S Kultur, fritid og anden service]
- prisenhed: values [V_T=Løbende priser, (mio. kr.), V_C=Pr. indbygger, løbende priser, (1000 kr.), LRG_T=2020-priser, kædede værdier, (mio. kr.), LRG_C=Pr. indbygger, 2020-priser, kædede værdier, (1000 kr.)]
- tid: date range 1993-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts but codes 0 (hele landet) and 999 (ikke regionalfordelt) are NOT in the dim. Exclude both when doing regional analysis.
- omrade uses levels 1 (5 regioner: 81–85) and 2 (11 landsdele: 1–11). Filter WHERE d.niveau=1 or d.niveau=2.
- prisenhed is a measurement selector — the same (omrade, transakt, branche, tid) combination appears 4 times. Always filter to one prisenhed: V_T (løbende priser, mio. kr.) or LRG_T (2020-priser, kædede værdier).
- transakt codes are distinct national accounts items (B1GD=BVT, B1GFD=BFI, D1D=aflønning af ansatte etc.). Do not sum across transakt — pick the specific transaction needed.
- branche=V is the "I alt" total. Filter branche='V' for aggregate figures. Do not include branche='V' when also summing individual branches.
- This table lacks B1GQD (BNP) — use nrhp for BNP. nrbp10 provides BVT (B1GD) broken down by branche, which nrhp does not.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade IN (0, 999).