table: fact.orgout60
description: Firmaers forhold for organisering af deres globale værdikæder efter branche (DB07 10-grp), forholdstype, betydning og tid
measure: indhold (unit Andel i pct.)
columns:
- branchedb0710: values [TOT=TOT Erhverv i alt, 2=2 Industri, råstofindvinding og forsyningsvirksomhed, 3=3 Bygge og anlæg, 4=4 Handel og transport mv., 5=5 Information og kommunikation, 6=6 Finansiering og forsikring, 7=7 Ejendomshandel og udlejning, 8=8 Erhvervsservice]
- fortyp: values [FOR=Forsyningsmangel i eksisterende værdikæder af råvarer, halvfabrikata og forbrugsvarer og serviceydelser, OMK=Stigning i omkostninger til råvarer grundet stigende energipriser, TRANSP=Problemer med transportkapacitet, forlænget transporttid eller transportomkostninger, OMKB=Andre stigninger i omkostninger til råvarer, halvfabrikata og forbrugsvarer, SANK=Effekten af sanktioner mod Rusland, C19=COVID-19-relaterede begrænsninger, MILJ=Miljøpolitiske begrænsninger]
- betyd: values [VERYIMP=Meget vigtig, IMP=Vigtig, NOTIMP=Ikke vigtig, NA=Ikke relevant]
- tid: date range 2021 to 2024

notes:
- tid is int4range. Only one survey wave: [2021,2024). No need to filter tid for the current period.
- indhold is Andel i pct. — same betyd distribution structure as orgout41. For each fortyp+branche combination, betyd distributes ~100% across importance levels. Filter WHERE betyd='VERYIMP' for "considered very important". Never sum across betyd.
- betyd: NA/Ikke relevant is stored as '' (empty string) in the database.
- fortyp: 7 independent global value chain challenge types. Do not sum across fortyp — each firm rates all 7 separately.
- branchedb0710: sectors 2–8 sum to TOT. Filter to TOT for national total, or exclude TOT when grouping by sector.