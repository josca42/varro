table: fact.dnmuf2
description: Udlån til husholdninger og erhverv efter opgørelsesmetode, datatype, sektor, instrument, rentetype, afdrag og tid
measure: indhold (unit -)
columns:
- opgoer: values [MODPART=Opgjort per låntager, LAAN=Opgjort per lån]
- data: values [ANTAL_MODPART=Antal låntagere (kun for opgørelse per låntager), ANTAL_LAAN=Antal lån (kun for opgørelse per lån), ONA=Restgæld, nominel værdi (mio. kr.), P10=Nedre decil (nominel restgæld, mio. kr.), P25=Nedre kvartil (nominel restgæld, mio. kr.), P50=Median (nominel restgæld, mio. kr.), P75=Øvre kvartil (nominel restgæld, mio. kr.), P90=Øvre decil (nominel restgæld, mio. kr.)]
- sektornat: values [1100=1100: Ikke-finansielle selskaber, 1410=1410: Husholdninger - personligt ejede virksomheder, 1430=1430: Husholdninger - lønmodtagere, pensionister mv.]
- instrnat: values [RI=Realkreditlån, PI_EKS=Banklån ekskl. kreditter]
- rentetype: values [TOT=Alle rentetyper, FAST=Fastforrentet, VAR=Variabelt forrentet]
- afdrag: values [TOT=Alle afdragstyper, MED=Med afdrag, UDEN=Uden afdrag]
- tid: date range 2020-01-01 to 2025-04-01

notes:
- data contains different measure types: ANTAL_MODPART/ANTAL_LAAN (counts), ONA (total debt mio. kr.), P10-P90 (percentiles). Never sum across data values.
- opgoer+data must be consistent: ANTAL_MODPART only for opgoer='MODPART'; ANTAL_LAAN only for opgoer='LAAN'. Percentiles apply to both.
- instrnat: only RI (realkreditlån) and PI_EKS (banklån ekskl. kreditter) — narrower than dnmuf1. For interest type and afdrag breakdown, only these two instrument types are available.
- rentetype: TOT=total; FAST+VAR are sub-categories summing to TOT.
- afdrag: TOT=total; MED+UDEN are sub-categories.
- sektornat: same 3 codes as dnmuf1 (1100, 1410, 1430) — no aggregate total.
- Vs. dnmuf1: dnmuf2 adds rentetype and afdrag dimensions but covers fewer instrnat values.