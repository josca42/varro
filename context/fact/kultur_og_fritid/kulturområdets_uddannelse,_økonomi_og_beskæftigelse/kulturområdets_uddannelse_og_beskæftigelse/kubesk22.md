table: fact.kubesk22
description: Erhvervsfrekvenser (ultimo november) efter uddannelsesinstitution, uddannelse, køn, dimittendårgang og tid
measure: indhold (unit Pct.)
columns:
- uddinst: values [IALT=Alle uddannelsesinstitutioner, AAA=Arkitektskolen Aarhus, KAA=Kunstakademiets Arkitektskole, KAD=Kunstakademiets Designskole, KAS=Kunstakademiets Konservatorskole, DSK=Designskolen Kolding, DKD=Det Kgl. Danske Musikkonservatorium, RMC=Rytmisk Musikkonservatorium, DJM=Det Jyske Musikkonservatorium, SMM=Syddansk Musikkonservatorium, SSS=Den Danske Scenekunstskole, KAB=Kunstakademiets Billedkunstskoler, DDF=Den Danske Filmskole, FOF=Forfatterskolen]
- uddannelse: values [49=Alle uddannelser, 50=Mellemlang videregående uddannelse, 51=Bachelor, 52=Kandidat, 53=Ph.d., solist]
- koen: values [0=Køn i alt, 1=Mand, 2=Kvinde]
- dimmitend: values [IALT=Alle dimittendårgange, 2009=2009, 2010=2010, 2011=2011, 2012=2012, 2013=2013, 2014=2014, 2015=2015, 2016=2016, 2017=2017, 2018=2018, 2019=2019, 2020=2020, 2021=2021, 2022=2022]
- tid: date range 2019-01-01 to 2023-01-01
notes:
- Values are employment RATES (Pct.). Do not sum — pick a single slice.
- dimmitend=IALT, koen=0, uddannelse=49, uddinst=IALT are totals. Filter all unused dimensions.
- No ledtyp split (unlike kubesk11) — single employment-rate definition.
- Cohorts available: 2009–2022 in dimmitend. The tid column covers the observation years (2019–2023).
