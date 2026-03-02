table: fact.kultudd2
description: Gennemsnitlig studietid (måneder) for fuldførte uddannelser på Kulturministeriets institutioner efter uddannelsesinstitution, uddannelse og tid
measure: indhold (unit Mdr.)
columns:
- uddinst: values [IALT=Alle uddannelsesinstitutioner, DKD=Det Kgl. Danske Musikkonservatorium, RMC=Rytmisk Musikkonservatorium, DJM=Det Jyske Musikkonservatorium, SMK=Syddansk Musikkonservatorium, SSS=Den Danske Scenekunstskole, KAB=Kunstakademiets Billedkunstskoler, DDF=Den Danske Filmskole]
- uddannelse: values [TOT=I alt, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser]
- tid: date range 2005-01-01 to 2024-01-01
notes:
- Values are mean study duration in MONTHS (Mdr.) for completed educations. Do not SUM — these are averages.
- uddannelse=TOT and uddinst=IALT are totals. Filter unused dimensions.
- Use AVG() with caution when aggregating across institutions — the fact table already contains pre-computed averages.
