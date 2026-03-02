table: fact.vnrbb10
description: Versionstabel NRBB10 - Beskæftigelse og timer (10a3-gruppering) efter version, område, socioøkonomisk status, branche og tid
measure: indhold (unit -)
columns:
- version: values [V2024_JUN=Juniversion 2021-2024, V2023_JUN=Juniversion 1993-2023 (Hovedrevision 2024), V2022_SEP=Septemberversion 2020-2022, V2021_SEP=Septemberversion 2019-2021, V2020_SEP=Septemberversion 2018-2020, V2019_SEP=Septemberversion 2017-2019, V2018_NOV=Novemberversion 2016-2018, V2017_NOV=Novemberversion 2015-2017, V2017_MAR=Martsversion 2014-2017, V2016_NOV=Novemberversion 2014-2016, V2015_NOV=Novemberversion 2004-2015 (Datarevision 2016), V2014_NOV=Novemberversion 2012-2014, V2013_NOV=Novemberversion 2011-2013, V2013_SEP=Septemberversion 1966-2013 (Hovedrevision 2014)]
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- socio: values [EMPH_DC=Samlede præsterede timer (1000 timer), SALH_DC=Præsterede timer for lønmodtagere (1000 timer), EMPM_DC=Samlet antal beskæftigede (antal), SALM_DC=Lønmodtagere (antal)]
- branche: values [V=I alt, VA=A Landbrug, skovbrug og fiskeri, VB=B Råstofindvinding, VC=C Industri, VD_E=D_E Forsyningsvirksomhed, VF=F Bygge og anlæg, VG_I=G_I Handel og transport mv., VJ=J Information og kommunikation, VK=K Finansiering og forsikring, VLA=LA Ejendomshandel og udlejning af erhvervsejendomme, VLB=LB Boliger, VM_N=M_N Erhvervsservice, VO_Q=O_Q Offentlig administration, undervisning og sundhed, VR_S=R_S Kultur, fritid og anden service]
- tid: date range 1993-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- version is a critical filter — all 14 versions cover the full time series back to 1993 and heavily overlap. Always filter to one version: V2024_JUN for latest. Omitting this filter inflates values by 14x.
- socio is a measurement selector with 4 mutually exclusive measure types. Pick one: EMPM_DC (headcount), SALM_DC (lønmodtagere headcount), EMPH_DC (timer), SALH_DC (lønmodtagere timer).
- branche=V is the "I alt" total. Do not sum it with individual branches.
- omrade joins dim.nuts but codes 0 and 999 are not in the dim. Exclude for regional analysis. Levels 1 (regioner) and 2 (landsdele).
- Prefer nrbb10 for standard analysis. Use vnrbb10 only for vintage comparison across revisions.