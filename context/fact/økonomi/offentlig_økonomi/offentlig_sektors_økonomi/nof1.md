table: fact.nof1
description: Udgifter til offentligt forbrug efter transaktion, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [D1D=1. Aflønning af ansatte, P51CD=2. Forbrug af fast realkapital, P2D=3. Forbrug i produktion, D29X39D=4+5. Andre produktionsskatter og -subsidier, netto, P1K=6. Produktion  (1+2+3+4+5), P31MD=7. Sociale ydelser i naturalier, P11A12A131K=8+9. Salg af varer og tjenester samt egenproducerede investeringer, P3D=10. Forbrugsudgifter, P31D=10.1. Individuelt forbrug, P32D=10.2. Kollektivt forbrug]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2014-01-01 to 2024-01-01

notes:
- prisenhed is a measurement selector: V=Løbende priser, LAN=2020-priser kædede værdier. Every transakt×tid row appears with both. Always filter to one.
- transakt: hierarchical. P3D=Forbrugsudgifter (code 10=total), P31D=Individuelt (10.1), P32D=Kollektivt (10.2). P3D = P31D + P32D. Also P1K=Produktion (=sum of codes 1+2+3+4+5). Don't sum totals with their components.
- Annual (2014–2024) — shorter series, national accounts format. For quarterly data with seasonal adjustment, use nkof1.