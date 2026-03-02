table: fact.nabk10
description: Akkumulations- og statuskonti, investering og beholdning af faste aktiver (10a3-gruppering) efter beholdning / strøm, aktiv, branche, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- behold: values [LSN=AN.11 Faste aktiver, nettobeholdning, primo året, LSG=Faste aktiver, bruttobeholdning, primo året, P51G=P.51g Faste bruttoinvesteringer, P51C=P.51c Forbrug af fast realkapital, K3=K.3 Tab ved katastrofer, K7=K.7 Nominelle kapitalgevinster og -tab, K72=heraf K.7.2 Reale kapitalgevinster og -tab, LEN=AN.11 Faste aktiver, nettobeholdning ultimo året, LEG=Faste aktiver, bruttobeholdning, ultimo året]
- aktiv: values [N11=Faste aktiver, N111=Boliger, N1121=Andre bygninger, N1122_3=Anlæg, N1131=Transportmidler, N11P=ICT udstyr, andre maskiner og inventar samt våbensystemer, N115=Stambesætninger mv., N117=Intellektuelle rettigheder]
- branche: join dim.nr_branche on branche=kode [approx]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- branche join: same V-prefix/underscore pattern — `JOIN dim.nr_branche d ON d.kode = replace(substring(f.branche from 2), '_', '-') AND d.niveau = 1`. 13 niveau-1 sectors + V + VMEMO.
- behold controls what indhold measures — never sum across behold. It mixes opening/closing stocks and flows: LSN/LSG = net/gross capital stock start of year; LEN/LEG = net/gross capital stock end of year; P51G = gross fixed capital formation (investment); P51C = depreciation; K3/K7/K72 = exceptional losses and capital gains.
- aktiv selects asset type. N11=all fixed assets (total). Use N11 for aggregate, or narrow to N111=dwellings, N1121=buildings, N1131=transport, N11P=ICT+machinery, N117=intellectual property.
- prisenhed must be filtered (V or LAN). K3, K7, K72 are V-only and cover fewer time periods.
- Sample — gross investment by sector in 2023: `WHERE behold = 'P51G' AND aktiv = 'N11' AND prisenhed = 'V' AND tid = '2023-01-01' AND branche NOT IN ('V','VMEMO')`