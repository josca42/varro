table: fact.kubs11
description: Kulturministeriets udbetalinger målrettet internationale formål efter landetype, kulturemne, land og tid
measure: indhold (unit 1.000 kr.)
columns:
- landtyp: values [1=Sagsland, 2=Modtagerland]
- kulturemne: values [0=Alle kulturemner, 8=IDRÆT OG FRITID, 9=Fornøjelses- og temaparker, 10=Idræt, 11=Spil og lotteri ... 31=Statslig administration, 32=Udstyr, 33=Anden/tværgående kultur, 34=Folkeoplysning og folkehøjskoler, 99=Uoplyst]
- land: values [TOT=I alt, EU1=EU, EU2=Europa udenfor EU, EUS=Europa, NORDEN=Norden ... KIN=Kina, OCEAN=Oceanien, MEØ=Mellemøsten, UOP=Uoplyst, USP=Uspecificeret land]
- tid: date range 2012-01-01 to 2023-01-01

notes:
- `landtyp` is a mandatory selector: 1=Sagsland (the country where the project is registered), 2=Modtagerland (the country that receives the funds). These are two different views of the same payments — always filter to one.
- `land` has hierarchical aggregates: TOT=all, EUS=all Europe, EU1=EU members, EU2=non-EU Europe, NORDEN=Nordic. Filtering to TOT and individual country codes simultaneously will double-count. Pick one level.
- `kulturemne=0` is all topics aggregate; broad category codes include sub-categories — don't sum across levels.