table: fact.dnpuddk2
description: Indenlandsk udlån fra pengeinstitutter til husholdninger og erhverv efter datatype, indenlandsk sektor, variabelt eller fast forrentet, referencerente, afdrag, tid til næste rentefiksering, formål for udlån til husholdninger og tid
measure: indhold (unit Mio. kr.)
columns:
- data: values [ULT=Ultimobalance (mio. kr.), VAL=Valutakursreguleringer (mio. kr.), NET=Nettotransaktioner (mio. kr.), KI=Indeks over nominelle beholdninger (indeks 201501=100)]
- indsek: values [1114=Ikke-finansielle selskaber og husholdninger i alt, 1100=- 1100: Ikke-finansielle selskaber, 1400=- 1400: Husholdninger, 1410=- - 1410: Husholdninger - personligt ejede virksomheder, 1430=- - 1430: Husholdninger - lønmodtagere, pensionister mv.]
- rente: values [ALLE=Variabelt og fast forrentet i alt, J=Fast forrentet, N=Variabelt forrentet]
- renteref: values [ALLE=I alt, J=Tilknyttet referencerente, N=Ikke tilknyttet referencerente]
- afdrag: values [ALLE=I alt, J=Med afdrag, N=Uden afdrag, ZZ=Ufordelt (fx kassekreditter og overtræk)]
- rentefix1: values [ALLE=I alt, M1A=- Op til og med 1 år, 1M=- - Op til og med 1 md., 1M6M=- - Over 1 md. og op til og med 6 mdr., 1A=- - Over 6 mdr. og op til og med 1 år, S1A=- Over 1 år, 1A3A=- - Over 1 år og op til og med 3 år, 5A=- - Over 3 år og op til og med 5 år, S5A=- - Over 5 år]
- formaal1: values [ALLE=Alle formål, B=Boligformål for udlån til husholdninger, F=Forbrugerkredit for udlån til husholdninger, A=Andet formål for udlån til husholdninger]
- tid: date range 2013-09-01 to 2025-09-01

notes:
- 7 dimension columns — every non-target dimension must be filtered to 'ALLE' to avoid overcounting.
- data: filter to data='ULT' for balance amounts.
- indsek hierarchy: 1114=total; 1100, 1400 (with sub-groups 1410, 1430) are components. Pick one level.
- rente: ALLE=total; J=fast forrentet, N=variabelt forrentet. These two sub-categories sum to ALLE.
- renteref: ALLE=total; J=with reference rate, N=without.
- afdrag: ALLE=total; J=med afdrag, N=uden afdrag, ZZ=ufordelt (kassekreditter etc.).
- rentefix1 is the time to next rate fixing: a hierarchy with ALLE=total → M1A (≤1 yr) → finer sub-ranges; S1A=>1 yr → 1A3A, 5A, S5A.
- formaal1: ALLE=all purposes; B/F/A apply to husholdninger only.
- This table has no instrnat (no instrument breakdown). For instrument+interest type cross: use dnpuddk3.
- To get a single total: data='ULT', indsek='1114', rente='ALLE', renteref='ALLE', afdrag='ALLE', rentefix1='ALLE', formaal1='ALLE'.