table: fact.nahk
description: Akkumulations- og statuskonti, investering og beholdning af faste aktiver efter beholdning / strøm, aktiv, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- behold: values [LSN=AN.11 Faste aktiver, nettobeholdning, primo året, LSG=Faste aktiver, bruttobeholdning, primo året, P51N=P.51n Faste nettoinvesteringer, P51G=P.51g Faste bruttoinvesteringer, P51C=P.51c Forbrug af fast realkapital, K3A7=K3+K.7 Andre ændringer i ikke-finansielle aktiver, K3=K.3 Tab ved katastrofer, K7=K.7 Nominelle kapitalgevinster og -tab, K72=heraf K.7.2 Reale kapitalgevinster og -tab, LEN=AN.11 Faste aktiver, nettobeholdning ultimo året, LEG=Faste aktiver, bruttobeholdning, ultimo året]
- aktiv: values [N11=Faste aktiver, N111=Boliger, N1121=Andre bygninger, N1122_3=Anlæg, N1131=Transportmidler, N11P=ICT udstyr, andre maskiner og inventar samt våbensystemer, N1132=ICT udstyr, N11321=IT-udstyr, N11322=Telekommunikationsudstyr, N11O=Andre maskiner og inventar samt våbensystemer, N115=Stambesætninger mv., N117=Intellektuelle rettigheder, N1171=Forskning og udvikling, N1172=Olie,gas,mineral efterforskning, N1173=Computer software, N1174T9=Originalværker indenfor kunst og underholdning mv.]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2024-01-01
notes:
- behold is a stock/flow type selector — the primary filter. Values: LSN/LSG=nettobeholdning/bruttobeholdning primo, LEN/LEG=nettobeholdning/bruttobeholdning ultimo, P51N/P51G=netto/bruttoinvesteringer, P51C=forbrug af fast realkapital (depreciation), K3A7/K3/K7/K72=andre ændringer. These are accounting categories, not additive across all values.
- prisenhed (V/LAN) doubles row counts — always filter to one value.
- aktiv codes are also hierarchical: N11=faste aktiver total, N111=boliger, N1121=andre bygninger, etc. Pick one level. For total: N11.
- For gross investment only (without balance sheet stocks), use nahi. Annual from 1966.
