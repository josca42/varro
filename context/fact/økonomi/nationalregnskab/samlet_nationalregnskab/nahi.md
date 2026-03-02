table: fact.nahi
description: Bruttoinvesteringer efter aktiv, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- aktiv: values [N111=Boliger, N1121=Andre bygninger, N1122_3=Anlæg, N1131=Transportmidler, N11P=ICT udstyr, andre maskiner og inventar samt våbensystemer, N115=Stambesætninger mv., N117=Intellektuelle rettigheder, N11G=Faste bruttoinvesteringer, N12_13=Lagerforøgelser mv., N12=Lagre, N13=Værdigenstande, P5G=Bruttoinvesteringer, P51C=Forbrug af fast realkapital, P5N=Nettoinvesteringer, N11NOF=Nyinvesteringer i offentlig forvaltning og service (memopost)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2024-01-01
notes:
- prisenhed is a measurement selector (V/LAN) — filter to one value or row counts double.
- aktiv codes are hierarchical: N11G=faste bruttoinvesteringer (total fixed), P5G=bruttoinvesteringer (broadest, including inventories and valuables), P5N=nettoinvesteringer. Individual asset types (N111, N1121, etc.) sum to N11G. Pick one level — do not mix totals and components.
- N11NOF=nyinvesteringer i offentlig forvaltning (memo item) — separate from the main accounting hierarchy.
- Annual from 1966. Quarterly with saeson: nkhi. For the full capital account (with stocks, revaluations, etc.) use nahk.
