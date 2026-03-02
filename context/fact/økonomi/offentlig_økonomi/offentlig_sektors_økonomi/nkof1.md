table: fact.nkof1
description: Udgifter til offentligt forbrug efter transaktion, prisenhed, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [D1D=1. Aflønning af ansatte, P51CD=2. Forbrug af fast realkapital, P2D=3. Forbrug i produktion, D29X39D=4+5. Andre produktionsskatter og -subsidier, netto, P1K=6. Produktion  (1+2+3+4+5), P31MD=7. Sociale ydelser i naturalier, P11A12A131K=8+9. Salg af varer og tjenester samt egenproducerede investeringer, P3D=10. Forbrugsudgifter, P31D=10.1. Individuelt forbrug, P32D=10.2. Kollektivt forbrug]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1999-01-01 to 2025-04-01

notes:
- Two measurement selectors: prisenhed (V/LAN) and saeson (N/Y). Every transakt×tid row appears 4 times (2 prisenhed × 2 saeson). Always filter both: e.g. WHERE prisenhed='V' AND saeson='N'.
- transakt: same hierarchical structure as nof1. P3D=total forbrugsudgifter (P31D+P32D). Don't mix totals with components.
- Quarterly (1999Q1–2025Q4). Longer series than nof1 (annual from 2014).