table: fact.ligeab1
description: Befolkningen (16-64 år) efter socioøkonomisk status, herkomst, familietype, køn, alder og tid
measure: indhold (unit Antal)
columns:
- socio: values [TOT=I alt, 00=Beskæftigede, 50=Arbejdsløse, 55=Uden for arbejdsstyrken]
- herkomst: values [0=I alt, 10=Personer med dansk oprindelse, 21=Indvandrere i alt, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 31=Efterkommere i alt, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande]
- famtype: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, EMHB=Enlige med hjemmeboende børn, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, PMHB=Par med hjemmeboende børn, U9=Uoplyst familietype]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 16-17=16-17 år, 18-19=18-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år]
- tid: date range 2008-01-01 to 2023-01-01

notes:
- herkomst includes intermediate totals: 21=Indvandrere i alt, 31=Efterkommere i alt alongside sub-groups (24/25 and 34/35). Do not sum totals + sub-groups: 21 already includes 24+25. Use either 21/31 or the sub-groups, not both.
- famtype includes sub-totals: F1/F2/E1/P1 are category totals; EUHB/EMHB/PUHB/PMHB are sub-types within those. Do not mix total and sub-type codes in the same SUM.
- socio is simplified to 4 values: TOT=I alt, 00=Beskæftigede, 50=Arbejdsløse, 55=Uden for arbejdsstyrken.
- kon has TOT=I alt.
- Population scope is 16-64 år only (unlike ras201/ras202 which cover broader age ranges).
- National level only. Use ligeab2 for regional breakdown with famtype.