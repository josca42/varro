table: fact.dnmuvs
description: Udlån til erhverv efter opgørelsesmetode, datatype, sektor og størrelse, instrument og tid
measure: indhold (unit -)
columns:
- opgoer: values [MODPART=Opgjort per låntager]
- data: values [ANTAL_MODPART=Antal låntagere, ONA=Restgæld, nominel værdi (mio. kr.), P10=Nedre decil (nominel restgæld, mio. kr.), P25=Nedre kvartil (nominel restgæld, mio. kr.), P50=Median (nominel restgæld, mio. kr.), P75=Øvre kvartil (nominel restgæld, mio. kr.), P90=Øvre decil (nominel restgæld, mio. kr.)]
- sekstr: values [ALL=1. Erhverv i alt (sektor 1100+1410), 1100=1.1. Ikke-finansielle selskaber (sektor 1100), 1100_DC=1.1.1. Store (sektor 1100, regnskabsklasse D og Store C), 1100_CBA=1.1.2. Små og mellemstore (sektor 1100, regnskabsklasse Mellemstore C, B og A), 1100_C=1.1.2.1. Mellemstore (sektor 1100, regnskabsklasse Mellemstore C), 1100_OEVRIGE=1.1.3. Øvrige (sektor 1100), 1100_BA=1.1.2.2. Små (sektor 1100, regnskabsklasse B og A), 1100_FONDE=1.1.3.1. Foreninger, fonde og andre selvejende institutioner (sektor 1100), 1100_ZZ=1.1.3.2. Ikke fordelt (sektor 1100, regnskabsklasse ukendt), 1410=1.2. Personligt ejede virksomheder (sektor 1410)]
- instrnat: values [ALLE=1. Alle bank- og realkreditlån, PI=1.1. Banklån, PI_EKS=1.1.1. Banklån ekskl. kreditter, KRED=1.1.2. Kreditter, KRED_EKS=1.1.2.1. Kreditter ekskl. kreditkort, KRED_KORT=1.1.2.2. Kreditkort, RI=1.2. Realkreditlån, ALLE_EKS=2. Alle bank- og realkreditlån ekskl. kreditter]
- tid: date range 2020-01-01 to 2025-04-01

notes:
- data contains different measure types: ANTAL_MODPART (borrower count), ONA (total debt mio. kr.), P10-P90 (percentiles). Never sum across data values.
- opgoer only has MODPART (per borrower) — no per-loan view in this table.
- sekstr is a size-based sub-hierarchy of erhverv (sektor 1100+1410): ALL=alle erhverv total; then sub-divided by company size class (large D+C, SME C+B+A, small B+A) and ownership type (fonde, ufordelt). This is the only table with company-size breakdown.
- Don't sum sekstr sub-categories with ALL (double-counting). Within 1100: DC + CBA + OEVRIGE = 1100; within CBA: C + BA = CBA.
- instrnat hierarchy same as dnmuf1: ALLE=all loans; PI=banklån (PI_EKS+KRED); RI=realkreditlån.
- This table covers erhverv only (sektor 1100+1410). For household borrowers use dnmuf1/dnmuf2.