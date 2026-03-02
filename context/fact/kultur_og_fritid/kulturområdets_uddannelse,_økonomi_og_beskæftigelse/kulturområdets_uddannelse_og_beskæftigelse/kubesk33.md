table: fact.kubesk33
description: Beskæftigede (ultimo november) efter uddannelsesinstitution, uddannelse, sektor, køn og tid
measure: indhold (unit Antal)
columns:
- uddinst: values [IALT=Alle uddannelsesinstitutioner, AAA=Arkitektskolen Aarhus, KAA=Kunstakademiets Arkitektskole, KAD=Kunstakademiets Designskole, KAS=Kunstakademiets Konservatorskole, DSK=Designskolen Kolding, DKD=Det Kgl. Danske Musikkonservatorium, RMC=Rytmisk Musikkonservatorium, DJM=Det Jyske Musikkonservatorium, SMM=Syddansk Musikkonservatorium, SSS=Den Danske Scenekunstskole, KAB=Kunstakademiets Billedkunstskoler, DDF=Den Danske Filmskole, FOF=Forfatterskolen]
- uddannelse: values [49=Alle uddannelser, 50=Mellemlang videregående uddannelse, 51=Bachelor, 52=Kandidat, 53=Ph.d., solist]
- sektor: values [0=Alle sektorer, 2=Lønmodtager offentlige sektor, 3=Lønmodtager private sektor, 1=Selvstændige eller medarbejdende ægtefælle]
- koen: values [0=Køn i alt, 1=Mand, 2=Kvinde]
- tid: date range 2019-01-01 to 2023-01-01
notes:
- Values are employment COUNTS (Antal). Sums are meaningful within a single sektor/koen/uddannelse slice.
- sektor=0 is the total across all sectors; filter when breaking down by sector.
- uddannelse=49, koen=0, uddinst=IALT are totals. Filter all unused dimensions.
- No dimmitend (cohort) breakdown — for cohort-level rates see kubesk22, for income see kubesk44.
- Sector breakdown: sektor=1 (selvstændige), sektor=2 (offentlig), sektor=3 (privat). These sum to sektor=0.
