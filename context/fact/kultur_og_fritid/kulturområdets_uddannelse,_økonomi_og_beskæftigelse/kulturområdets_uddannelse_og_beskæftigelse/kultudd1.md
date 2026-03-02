table: fact.kultudd1
description: Studerende med frafald inden for 5 år på Kulturministeriets institutioner efter uddannelsesinstitution og tid
measure: indhold (unit Antal)
columns:
- uddinst: values [IALT=Alle uddannelsesinstitutioner, DKD=Det Kgl. Danske Musikkonservatorium, RMC=Rytmisk Musikkonservatorium, DJM=Det Jyske Musikkonservatorium, SMK=Syddansk Musikkonservatorium, SSS=Den Danske Scenekunstskole, KAB=Kunstakademiets Billedkunstskoler, DDF=Den Danske Filmskole]
- tid: date range 2005-01-01 to 2019-01-01
notes:
- Single measure: dropout count within 5 years. No breakdown by gender, education type, or nationality.
- Time series ends at 2019 — no recent data. Use with kultudd for context on total enrolled.
- uddinst=IALT is the total across all 8 institutions.
