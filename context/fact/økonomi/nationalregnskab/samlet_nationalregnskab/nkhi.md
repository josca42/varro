table: fact.nkhi
description: Bruttoinvesteringer efter aktiv, prisenhed, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- aktiv: values [N111=Boliger, N1121=Andre bygninger, N1122_3=Anlæg, N1131=Transportmidler, N11P=ICT udstyr, andre maskiner og inventar samt våbensystemer, N115=Stambesætninger mv., N117=Intellektuelle rettigheder, N11G=Faste bruttoinvesteringer, N12_13=Lagerforøgelser mv., N12=Lagre, N13=Værdigenstande, P5G=Bruttoinvesteringer, P51C=Forbrug af fast realkapital, P5N=Nettoinvesteringer, N11NOF=Nyinvesteringer i offentlig forvaltning og service (memopost)]
- prisenhed: values [V=Løbende priser, LKV=2020-priser, kædede værdier]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01
notes:
- TWO measurement selectors: prisenhed (V/LKV) and saeson (N/Y). Always filter both or row counts quadruple.
- Quarterly gross investment from 1990. Annual equivalent: nahi (from 1966).
- Same aktiv hierarchy as nahi — N11G=total fixed investment, P5G=broadest total. Do not mix totals and components.
