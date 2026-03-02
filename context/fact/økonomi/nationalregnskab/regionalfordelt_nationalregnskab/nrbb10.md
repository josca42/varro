table: fact.nrbb10
description: Beskæftigelse og timer (10a3-gruppering) efter område, socioøkonomisk status, branche og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- socio: values [EMPH_DC=Samlede præsterede timer (1000 timer), SALH_DC=Præsterede timer for lønmodtagere (1000 timer), EMPM_DC=Samlet antal beskæftigede (antal), SALM_DC=Lønmodtagere (antal)]
- branche: values [V=I alt, VA=A Landbrug, skovbrug og fiskeri, VB=B Råstofindvinding, VC=C Industri, VD_E=D_E Forsyningsvirksomhed, VF=F Bygge og anlæg, VG_I=G_I Handel og transport mv., VJ=J Information og kommunikation, VK=K Finansiering og forsikring, VLA=LA Ejendomshandel og udlejning af erhvervsejendomme, VLB=LB Boliger, VM_N=M_N Erhvervsservice, VO_Q=O_Q Offentlig administration, undervisning og sundhed, VR_S=R_S Kultur, fritid og anden service]
- tid: date range 1993-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts but codes 0 (hele landet) and 999 (ikke regionalfordelt) are NOT in the dim. Exclude both when doing regional analysis.
- omrade uses levels 1 (5 regioner: 81–85) and 2 (11 landsdele: 1–11). Filter WHERE d.niveau=1 or d.niveau=2.
- socio is a measurement selector with 4 mutually exclusive measure types — pick one. EMPM_DC=headcount (antal beskæftigede), SALM_DC=lønmodtagere headcount, EMPH_DC=total timer (1000 timer), SALH_DC=lønmodtagere timer. Do not sum across socio values.
- branche=V is the "I alt" total across all sectors. Filter branche='V' for economy-wide figures, or filter to specific branches. Do not sum branche='V' together with individual branches.
- Typical query: SELECT d.titel, f.tid, f.indhold FROM fact.nrbb10 f JOIN dim.nuts d ON f.omrade=d.kode WHERE d.niveau=1 AND f.socio='EMPM_DC' AND f.branche='V'.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade IN (0, 999).