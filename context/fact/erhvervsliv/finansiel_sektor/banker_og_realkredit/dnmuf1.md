table: fact.dnmuf1
description: Udlån til husholdninger og erhverv efter opgørelsesmetode, datatype, sektor, instrument og tid
measure: indhold (unit -)
columns:
- opgoer: values [MODPART=Opgjort per låntager, LAAN=Opgjort per lån]
- data: values [ANTAL_MODPART=Antal låntagere (kun for opgørelse per låntager), ANTAL_LAAN=Antal lån (kun for opgørelse per lån), ONA=Restgæld, nominel værdi (mio. kr.), P10=Nedre decil (nominel restgæld, mio. kr.), P25=Nedre kvartil (nominel restgæld, mio. kr.), P50=Median (nominel restgæld, mio. kr.), P75=Øvre kvartil (nominel restgæld, mio. kr.), P90=Øvre decil (nominel restgæld, mio. kr.)]
- sektornat: values [1100=1100: Ikke-finansielle selskaber, 1410=1410: Husholdninger - personligt ejede virksomheder, 1430=1430: Husholdninger - lønmodtagere, pensionister mv.]
- instrnat: values [ALLE=1. Alle bank- og realkreditlån, PI=1.1. Banklån, PI_EKS=1.1.1. Banklån ekskl. kreditter, KRED=1.1.2. Kreditter, KRED_EKS=1.1.2.1. Kreditter ekskl. kreditkort, KRED_KORT=1.1.2.2. Kreditkort, RI=1.2. Realkreditlån, ALLE_EKS=2. Alle bank- og realkreditlån ekskl. kreditter]
- tid: date range 2020-01-01 to 2025-04-01

notes:
- data contains fundamentally different measure types that must never be summed together: ANTAL_MODPART (count of borrowers), ANTAL_LAAN (count of loans), ONA (total outstanding debt, mio. kr.), P10/P25/P50/P75/P90 (percentiles of the debt distribution).
- ANTAL_MODPART is only valid when opgoer='MODPART'; ANTAL_LAAN only when opgoer='LAAN'. The P10-P90 percentiles are per borrower or per loan depending on opgoer. Always filter both opgoer and data consistently.
- opgoer selects the unit of analysis: MODPART=per borrower (one row per unique CVR/CPR), LAAN=per loan. Counts differ substantially. Don't sum across opgoer.
- sektornat: only 3 values — 1100 (ikke-finansielle selskaber), 1410 (personligt ejede virksomheder), 1430 (lønmodtagere/pensionister). No aggregate 'total' code; to get all borrowers sum 1100+1410+1430 or use ONA to get total debt.
- instrnat hierarchy: ALLE=all loans (PI+RI); PI=banklån (PI_EKS+KRED); KRED=kreditter (KRED_EKS+KRED_KORT); RI=realkreditlån. ALLE_EKS=all excluding kreditter. Don't sum sub-components with their parent.
- Short time series: from 2020 only (quarterly).