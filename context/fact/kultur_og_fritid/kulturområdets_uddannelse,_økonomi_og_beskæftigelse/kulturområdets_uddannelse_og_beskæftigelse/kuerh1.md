table: fact.kuerh1
description: Kulturens erhvervsstruktur efter kulturemne, aktivitet, enhed og tid
measure: indhold (unit -)
columns:
- kulturemne: values [0=Alle kulturemner, 9=Fornøjelses- og temaparker, 10=Idræt, 11=Spil og lotteri, 13=Arkiver ... 26=Design, 27=Fotografering, 28=Kunsthåndværk, 30=Reklame, 33=Anden/tværgående kultur]
- aktivi: values [TOT=Alle aktiviteter, 0=Kerneaktivitet, 1=Støtteaktivitet]
- enhed: values [40=Årlig lønsum (Mio. kr.), 10=Fuldtidsbeskæftigede, 20=Arbejdssteder ultimo november, 30=Job ultimo november]
- tid: date range 2008-01-01 to 2023-01-01

notes:
- CRITICAL: enhed is a measurement selector with 4 fundamentally different measures (10=Fuldtidsbeskæftigede, 20=Arbejdssteder, 30=Job, 40=Lønsum i Mio. kr.). Every dimension combination is repeated 4 times. Always filter enhed to a single value.
- aktivi=TOT is the aggregate (kerneaktivitet + støtteaktivitet); filter when breaking down by type.
- kulturemne=0 is total. Numeric kulturemne codes cannot be joined to dim.kulturemner (K-prefix mismatch). The numeric codes correspond to K-prefix stripped values (9=K09=Fornøjelses- og temaparker, 21=K21=Musik, etc.). Use inline values from the columns doc.