table: fact.nkhc1
description: Forbrugsudgift efter forbrugsart, prisenhed, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- forbrugsart: values [P31DC=Husholdningers forbrugsudgift på dansk område, P33=Turistudgifter, P34=Turistindtægter, P31S14=Husholdningernes forbrugsudgifter, P31S15=Forbrugsudgifter i Non-profit institutioner rettet mod husholdninger (NPISH), P31S1M=Privatforbrug, P3S13=Offentlige forbrugsudgifter, P31S13=Offentlige individuelle forbrugsudgifter, P32S13=Offentlige kollektive forbrugsudgifter, P3=Samlede udgifter til forbrug, P41=Faktisk individuelt forbrug, P42=Faktisk kollektivt forbrug]
- prisenhed: values [V=Løbende priser, LKV=2020-priser, kædede værdier]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01
notes:
- TWO measurement selectors: prisenhed (V/LKV) and saeson (N/Y). Always filter both or row counts quadruple.
- Quarterly forbrugsudgift from 1990. Annual equivalent: nahc1 (from 1966).
- Same forbrugsart overlap as nahc1 — multiple codes are hierarchical aggregates. Pick the one level you need; do not sum all forbrugsart values.
