table: fact.kubesk11
description: Ledighedsprocenter for dimittender fra de kulturelle uddannelser efter uddannelsesinstitution, uddannelse, dimittendårgang, køn, ledighedstype og tid
measure: indhold (unit Pct.)
columns:
- uddinst: values [IALT=Alle uddannelsesinstitutioner, AAA=Arkitektskolen Aarhus, KAA=Kunstakademiets Arkitektskole, KAD=Kunstakademiets Designskole, KAS=Kunstakademiets Konservatorskole, DSK=Designskolen Kolding, DKD=Det Kgl. Danske Musikkonservatorium, RMC=Rytmisk Musikkonservatorium, DJM=Det Jyske Musikkonservatorium, SMM=Syddansk Musikkonservatorium, SSS=Den Danske Scenekunstskole, KAB=Kunstakademiets Billedkunstskoler, DDF=Den Danske Filmskole, FOF=Forfatterskolen]
- uddannelse: values [49=Alle uddannelser, 50=Mellemlang videregående uddannelse, 51=Bachelor, 52=Kandidat, 53=Ph.d., solist]
- dimmitend: values [IALT=Alle dimittendårgange, 2010=2010, 2011=2011, 2012=2012, 2013=2013, 2014=2014, 2015=2015, 2016=2016, 2017=2017, 2018=2018, 2019=2019, 2020=2020, 2021=2021, 2022=2022, 2023=2023]
- koen: values [0=Køn i alt, 1=Mand, 2=Kvinde]
- ledtyp: values [4=Nettoledige, 5=Bruttoledige]
- tid: date range 2020-01-01 to 2024-01-01
notes:
- Values are unemployment RATES (Pct.), not counts. Never sum across ledtyp — these are independent measures of the same phenomenon.
- ledtyp: 4=Nettoledige (strictly unemployed), 5=Bruttoledige (includes people in activation). Always filter to one type.
- dimmitend=IALT aggregates all graduation cohorts; uddannelse=49 aggregates all degree types; uddinst=IALT aggregates all institutions; koen=0 aggregates gender. Filter all unused dimensions to their total.
- Short time series (2020–2024 only). For student enrollment history, see kultudd (from 2005).
- Table covers 14 named cultural higher-education institutions — distinct from the broader municipal cultural sector in kuerh/kuarb tables.
