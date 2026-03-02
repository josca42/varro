table: fact.dnpuddk1
description: Indenlandsk udlån fra pengeinstitutter til husholdninger og erhverv efter instrument, datatype, indenlandsk sektor, løbetid (oprindelig løbetid), restløbetid, tid til næste rentefiksering, formål for udlån til husholdninger og tid
measure: indhold (unit Mio. kr.)
columns:
- instrnat: values [AL00=Udlån i alt, AL20=- Kassekreditter (revolverende lån) og overtræk, AL30=- Kredit på kreditkort, AL40=- Repoudlån, AL99=- Øvrige udlån]
- data: values [ULT=Ultimobalance (mio. kr.), VAL=Valutakursreguleringer (mio. kr.), NET=Nettotransaktioner (mio. kr.), KI=Indeks over nominelle beholdninger (indeks 201501=100)]
- indsek: values [1114=Ikke-finansielle selskaber og husholdninger i alt, 1100=- 1100: Ikke-finansielle selskaber, 1400=- 1400: Husholdninger, 1410=- - 1410: Husholdninger - personligt ejede virksomheder, 1430=- - 1430: Husholdninger - lønmodtagere, pensionister mv.]
- lobetid1: values [ALLE=Alle løbetider]
- lobetid2: values [ALLE=Alle løbetider]
- rentefix1: values [ALLE=I alt, M1A=- Op til og med 1 år, S1A=- Over 1 år]
- formaal1: values [ALLE=Alle formål, B=Boligformål for udlån til husholdninger, F=Forbrugerkredit for udlån til husholdninger, A=Andet formål for udlån til husholdninger]
- tid: date range 2013-09-01 to 2025-09-01

notes:
- 7 dimension columns — every non-target dimension must be filtered to its "ALLE" aggregate or a single value to avoid overcounting.
- data: filter to data='ULT' for balance amounts; other values (NET, VAL, KI) are different measure types.
- indsek hierarchy: 1114=ikke-fin. selskaber + husholdninger i alt (the broadest); 1100=ikke-fin. selskaber, 1400=husholdninger total, 1410+1430=husholdnings sub-segments. Pick one level.
- instrnat: AL00=udlån i alt (total); AL20/AL30/AL40/AL99 are sub-types summing to AL00.
- lobetid1 and lobetid2 only have ALLE in this table — no maturity breakdown here (use dnpuddkb for maturity).
- rentefix1: ALLE=total; M1A and S1A are sub-ranges (≤1 year, >1 year to next rate fixing).
- formaal1: ALLE=alle formål; B/F/A apply only to husholdninger (sektor 1400). For erhvervssektor queries use formaal1='ALLE'.
- To get a single total: instrnat='AL00', data='ULT', indsek='1114', lobetid1='ALLE', lobetid2='ALLE', rentefix1='ALLE', formaal1='ALLE'.