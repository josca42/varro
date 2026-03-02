table: fact.kubesk44
description: Gennemsnitlige indkomster for beskæftigede dimittender efter uddannelsesinstitution, uddannelse, dimittendårgang, køn, indkomsttype og tid
measure: indhold (unit Kr.)
columns:
- uddinst: values [IALT=Alle uddannelsesinstitutioner, AAA=Arkitektskolen Aarhus, KAA=Kunstakademiets Arkitektskole, KAD=Kunstakademiets Designskole, KAS=Kunstakademiets Konservatorskole, DSK=Designskolen Kolding, DKD=Det Kgl. Danske Musikkonservatorium, RMC=Rytmisk Musikkonservatorium, DJM=Det Jyske Musikkonservatorium, SMM=Syddansk Musikkonservatorium, SSS=Den Danske Scenekunstskole, KAB=Kunstakademiets Billedkunstskoler, DDF=Den Danske Filmskole, FOF=Forfatterskolen]
- uddannelse: values [49=Alle uddannelser, 50=Mellemlang videregående uddannelse, 51=Bachelor, 52=Kandidat, 53=Ph.d., solist]
- dimmitend: values [IALT=Alle dimittendårgange, 2009=2009, 2010=2010, 2011=2011, 2012=2012, 2013=2013, 2014=2014, 2015=2015, 2016=2016, 2017=2017, 2018=2018, 2019=2019, 2020=2020, 2021=2021, 2022=2022]
- koen: values [0=Køn i alt, 1=Mand, 2=Kvinde]
- indkomsttype: values [ERHVERVSINDK=Erhvervsindkomst, PERSONINDK=Personindkomst]
- tid: date range 2019-01-01 to 2023-01-01
notes:
- indkomsttype is a measurement selector: ERHVERVSINDK and PERSONINDK are different income concepts applied to the same people. Always filter to one type — summing across them is meaningless.
- Values are MEAN incomes (Kr.), not totals. Do not use SUM() across institutions or education types.
- dimmitend=IALT, koen=0, uddannelse=49, uddinst=IALT are totals. Filter all unused dimensions.
- For person counts of employed graduates, use kubesk33. This table only has income data.
