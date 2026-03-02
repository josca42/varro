table: fact.nabk19
description: Akkumulations- og statuskonti, investering og beholdning af faste aktiver (19a2-gruppering) efter beholdning / strøm, aktiv, branche, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- behold: values [LSN=AN.11 Faste aktiver, nettobeholdning, primo året, LSG=Faste aktiver, bruttobeholdning, primo året, P51G=P.51g Faste bruttoinvesteringer, P51C=P.51c Forbrug af fast realkapital, K3=K.3 Tab ved katastrofer, K7=K.7 Nominelle kapitalgevinster og -tab, K72=heraf K.7.2 Reale kapitalgevinster og -tab, LEN=AN.11 Faste aktiver, nettobeholdning ultimo året, LEG=Faste aktiver, bruttobeholdning, ultimo året]
- aktiv: values [N11=Faste aktiver, N111=Boliger, N1121=Andre bygninger, N1122_3=Anlæg, N1131=Transportmidler, N11P=ICT udstyr, andre maskiner og inventar samt våbensystemer, N115=Stambesætninger mv., N117=Intellektuelle rettigheder]
- branche: join dim.nr_branche on branche=kode [approx]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- branche join: `JOIN dim.nr_branche d ON d.kode = substring(f.branche from 2) AND d.niveau = 2`. Strip V prefix only — niveau-2 codes have no hyphens. 21 sectors + V + VMEMO.
- behold controls what indhold measures — never sum across behold. Mix of opening/closing stocks and flows (P51G=investment, P51C=depreciation, K3/K7/K72=adjustments).
- aktiv selects asset type. N11=all fixed assets (total).
- prisenhed must be filtered. K3, K7, K72 are V-only and cover fewer years.