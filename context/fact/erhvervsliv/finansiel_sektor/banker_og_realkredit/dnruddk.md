table: fact.dnruddk
description: Realkreditudlån til danske modparter efter værdier, datatype, sektor, rentetype, afdrag, valuta, ejendomskategori og tid
measure: indhold (unit Mio. kr.)
columns:
- vaerdi1: values [NOM=Nominel værdi, MARKEDS=Markedsværdi]
- data: values [ULTIMO=Ultimobalance, NETTOTRANS=Nettotransaktioner, VALUTAKURS=Valutakursreguleringer, REKLAS=Reklassifikationer, BORSKURS=Børskursreguleringer]
- sektornat: values [1000=1000: Alle indenlandske sektorer, 1100=- 1100: Ikke-finansielle selskaber, 1110=- 1110: Offentlig del af ikke-finansielle selskaber, 1120=- 1120: Privat del af ikke-finansielle selskaber, 1200=- 1200: Finansielle selskaber, 1300=- 1300: Offentlig forvaltning og service, 1400=- 1400: Husholdninger, 1410=-  - 1410: Husholdninger - personligt ejede virksomheder, 1430=-  - 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=- 1500: Nonprofitinstitutioner rettet mod husholdninger]
- rentetype: values [ALLE=I alt, J=Fastforrentet, N=Variabelt forrentet]
- afdrag: values [ALLE=I alt, J=Med afdrag, N=Uden afdrag]
- valuta: values [Z01=Alle valutaer, DKK=DKK, X00=Udenlandsk valuta i alt]
- ejenkatnat: values [ALLE=Alle ejendomskategorier, E1=Ejerbolig og fritidshuse, E2=Alment boligbyggeri, E3=Private udlejningsejendomme, E4=Landbrug mv., E5=Industri og håndværk mv., E6=Kontor og forretning, E7=Ejendomme til sociale, kulturelle og undervisningsmæssige formål, E8=Ubebyggede grunde]
- tid: date range 2022-12-01 to 2025-09-01

notes:
- Very short time series: only from 2022-12-01. For longer history use dnruddkb (from 2014).
- vaerdi1 selects the valuation method: NOM=nominal value, MARKEDS=market value. These are different valuations of the same loans — never sum them. Pick one; NOM is typical for outstanding stock comparisons.
- data is a measurement-type selector: ULTIMO=end-of-period stock. Other values (NETTOTRANS, VALUTAKURS, REKLAS, BORSKURS) are adjustment flows. Filter to data='ULTIMO' for balance.
- 7 dimension columns — every non-target must be filtered: vaerdi1, data, sektornat, rentetype, afdrag, valuta, ejenkatnat.
- sektornat: 1000=alle indenlandske sektorer (total). All other codes are sub-components. Don't sum sub-sectors with '1000'.
- rentetype: ALLE=total; J+N are sub-categories.
- afdrag: ALLE=total; J=med afdrag, N=uden afdrag (afdragsfrie lån).
- valuta: Z01=alle valutaer, DKK, X00=udenlandsk valuta. Z01 is the typical total.
- ejenkatnat: ALLE=alle ejendomskategorier; E1-E8 are property type sub-categories.
- To get a single total: vaerdi1='NOM', data='ULTIMO', sektornat='1000', rentetype='ALLE', afdrag='ALLE', valuta='Z01', ejenkatnat='ALLE'.