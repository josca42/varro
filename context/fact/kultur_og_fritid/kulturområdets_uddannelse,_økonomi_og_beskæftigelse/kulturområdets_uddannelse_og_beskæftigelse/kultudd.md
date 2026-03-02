table: fact.kultudd
description: Studerende på Kulturministeriets institutioner efter status, uddannelsesinstitution, uddannelse, internationale og ikke internationale studerende og tid
measure: indhold (unit Antal)
columns:
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- uddinst: values [IALT=Alle uddannelsesinstitutioner, DKD=Det Kgl. Danske Musikkonservatorium, RMC=Rytmisk Musikkonservatorium, DJM=Det Jyske Musikkonservatorium, SMK=Syddansk Musikkonservatorium, SSS=Den Danske Scenekunstskole, KAB=Kunstakademiets Billedkunstskoler, DDF=Den Danske Filmskole]
- uddannelse: values [TOT=I alt, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser]
- intnat: values [0=I alt, 1=Ikke international studerende, 2=International studerende]
- tid: date range 2005-01-01 to 2024-01-01
notes:
- CRITICAL: fstatus is a measurement selector for completely different counts: B=enrolled students (pr. 1. oktober), F=completed educations, T=new entrants. Always filter to one value — these are NOT additive.
- intnat=0 is the total (international + non-international); filter when comparing groups.
- uddannelse=TOT and uddinst=IALT are totals. Filter unused dimensions.
- Longest time series in this group (2005–2024). Covers only 8 music/scene/film institutions (NOT the architecture/design schools in kubesk tables).
- Institution codes here (SMK=Syddansk Musikkonservatorium) differ slightly from kubesk tables (SMM=Syddansk Musikkonservatorium) — same institution, different abbreviation.
