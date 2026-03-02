table: fact.dnpuddk3
description: Indenlandsk udlån fra pengeinstitutter til husholdninger og erhverv efter instrument, datatype, indenlandsk sektor, variabelt eller fast forrentet, referencerente, afdrag, formål for udlån til husholdninger og tid
measure: indhold (unit Mio. kr.)
columns:
- instrnat: values [AL00=Udlån i alt, AL20=- Kassekreditter (revolverende lån) og overtræk, AL30=- Kredit på kreditkort, AL40=- Repoudlån, AL99=- Øvrige udlån]
- data: values [ULT=Ultimobalance (mio. kr.), VAL=Valutakursreguleringer (mio. kr.), NET=Nettotransaktioner (mio. kr.), KI=Indeks over nominelle beholdninger (indeks 201501=100)]
- indsek: values [1114=Ikke-finansielle selskaber og husholdninger i alt, 1100=- 1100: Ikke-finansielle selskaber, 1400=- 1400: Husholdninger, 1410=- - 1410: Husholdninger - personligt ejede virksomheder, 1430=- - 1430: Husholdninger - lønmodtagere, pensionister mv.]
- rente: values [ALLE=Variabelt og fast forrentet i alt, J=Fast forrentet, N=Variabelt forrentet]
- renteref: values [ALLE=I alt, J=Tilknyttet referencerente, N=Ikke tilknyttet referencerente]
- afdrag: values [ALLE=I alt]
- formaal1: values [ALLE=Alle formål, B=Boligformål for udlån til husholdninger, F=Forbrugerkredit for udlån til husholdninger, A=Andet formål for udlån til husholdninger]
- tid: date range 2013-09-01 to 2025-09-01

notes:
- 7 dimension columns — every non-target dimension must be filtered to 'ALLE' to avoid overcounting.
- data: filter to data='ULT' for balance amounts.
- instrnat: AL00=total; AL20/AL30/AL40/AL99 are instrument sub-types.
- indsek hierarchy: 1114=total; 1100, 1400 (with sub-groups 1410, 1430) are components.
- rente: ALLE=total; J=fast forrentet, N=variabelt. Sum of J+N = ALLE.
- renteref: ALLE=total; J/N are sub-categories.
- afdrag: only ALLE in this table — no afdrag breakdown (use dnpuddk2 for afdrag detail).
- formaal1: ALLE=all purposes; B/F/A apply to husholdninger only.
- Vs. dnpuddk2: same dimensions except dnpuddk3 has instrnat but no rentefix1; dnpuddk2 has rentefix1 but no instrnat.
- To get a single total: instrnat='AL00', data='ULT', indsek='1114', rente='ALLE', renteref='ALLE', afdrag='ALLE', formaal1='ALLE'.