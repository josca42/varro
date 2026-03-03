table: fact.kubesk55
description: Beskæftigede (ultimo november) efter uddannelsesinstitution, uddannelse, arbejdsstedsregion, køn og tid
measure: indhold (unit Antal)
columns:
- uddinst: values [IALT=Alle uddannelsesinstitutioner, AAA=Arkitektskolen Aarhus, KAA=Kunstakademiets Arkitektskole, KAD=Kunstakademiets Designskole, KAS=Kunstakademiets Konservatorskole, DSK=Designskolen Kolding, DKD=Det Kgl. Danske Musikkonservatorium, RMC=Rytmisk Musikkonservatorium, DJM=Det Jyske Musikkonservatorium, SMM=Syddansk Musikkonservatorium, SSS=Den Danske Scenekunstskole, KAB=Kunstakademiets Billedkunstskoler, DDF=Den Danske Filmskole, FOF=Forfatterskolen]
- uddannelse: values [49=Alle uddannelser, 50=Mellemlang videregående uddannelse, 51=Bachelor, 52=Kandidat, 53=Ph.d., solist]
- arbreg: join dim.nuts on arbreg=kode; levels [1]
- koen: values [0=Køn i alt, 1=Mand, 2=Kvinde]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- arbreg joins dim.nuts at niveau=1 (5 regioner, codes 81–85). Code 0 is national total, not in dim.
- Join: SELECT f.*, d.titel FROM fact.kubesk55 f JOIN dim.nuts d ON f.arbreg::text = d.kode WHERE d.niveau = 1 AND f.arbreg != 0
- uddannelse=49, uddinst=IALT, koen=0 are totals; filter unused dimensions.
- Same institution list as other kubesk tables (14 cultural higher-education institutions).
- Map: /geo/regioner.parquet — merge on arbreg=dim_kode. Exclude arbreg=0.