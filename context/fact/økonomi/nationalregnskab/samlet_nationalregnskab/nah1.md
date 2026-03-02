table: fact.nah1
description: 0 Varer og tjenester efter transaktion, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P1D=P.1 Produktion, P11D=P.11 Markedsmæssig produktion, P12D=P.12 Produktion til eget brug, P13D=P.13 Ikke-markedsmæssig produktion, P131D=P.131 Betaling for ikke-markedsmæssig produktion ... P53K=P.53 Anskaffelser minus afhændelser af værdigenstande, P6K=P.6 Eksport af varer og tjenester, P61K=P.61 Eksport af varer, P62K=P.62 Eksport af tjenester, TUPRK=Anvendelse i alt]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2024-01-01
notes:
- prisenhed is a measurement selector: V=løbende priser, LAN=2020-priser (kædede værdier). Every transakt×tid combination is repeated for each prisenhed — always filter to one value (e.g., WHERE prisenhed = 'V') or you silently double counts.
- transakt codes are national accounts supply/use entries at multiple levels of aggregation — not all additive. Use specific codes (e.g., B1GQD=BNP, P6K=total eksport). TUPRK='Anvendelse i alt' is the grand total of uses.
- Annual table back to 1966. For quarterly data with seasonal adjustment use nkh1 (from 1990). For BNP/production main aggregates only, nahl2 is more focused.
