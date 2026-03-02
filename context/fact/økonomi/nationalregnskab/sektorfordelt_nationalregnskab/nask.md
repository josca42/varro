table: fact.nask
description: Akkumulations- og statuskonti, investering og beholdning af faste aktiver, efter beholdning / strøm, aktiv, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- behold: values [LSN=AN.11 Faste aktiver, nettobeholdning, primo året, P51N=P.51n Faste nettoinvesteringer, K3A7=K3+K.7 Andre ændringer i ikke-finansielle aktiver, LEN=AN.11 Faste aktiver, nettobeholdning ultimo året]
- aktiv: values [N11=Faste aktiver, N111=Boliger, N1121=Andre bygninger, N1122_3=Anlæg, N1131=Transportmidler, N11P=ICT udstyr, andre maskiner og inventar samt våbensystemer, N115=Stambesætninger mv., N117=Intellektuelle rettigheder]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. 7 sectors: S11, S12, S13, S14, S15, plus aggregates S1=Hele økonomien and S1M=S.14+S.15. No S2 (rest of world). Use ColumnValues("nask", "sektor") for labels.
- behold (stock/flow type) values are NOT additive: LSN=opening net stock, P51N=net investment, K3A7=other volume changes, LEN=closing net stock. The identity is: LEN = LSN + P51N + K3A7. Always filter to one behold value — never sum across them.
- aktiv (asset type): N11=total fixed assets (aggregate of all subtypes). N111=housing, N1121=other buildings, N1122_3=civil engineering, N1131=transport, N11P=ICT/machinery/weapons, N115=livestock, N117=intellectual property. Summing subtypes equals N11.
- Typical query: WHERE behold='LEN' AND aktiv='N11' to get total net capital stock at year-end by sector.