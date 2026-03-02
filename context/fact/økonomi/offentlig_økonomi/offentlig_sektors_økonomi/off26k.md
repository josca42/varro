table: fact.off26k
description: Offentlig forvaltning og service, forbrugsudgift efter udgifter og tid
measure: indhold (unit Mio. kr.)
columns:
- udgift: values [1=1. Aflønning af ansatte, 2=2. Forbrug af fast realkapital, 3=3. Forbrug i produktion, 4=4. Andre produktionsskatter, 5=5. Andre produktionssubsidier, 6=6. Produktion (1+2+3+4+5), 7=7. Sociale ydelser i naturalier, 8=8. Salg af varer og tjenester, 9=9. Egenproduktion overført til investering, 10=10. Forbrugsudgifter (6+7+8+9)]
- tid: date range 1999-01-01 to 2025-04-01

notes:
- Quarterly version of off26 (1999Q1–2025Q4). No sektor breakdown.
- udgift: 10=Forbrugsudgifter i alt (= 6+7+8+9). Note off26k does NOT include 10.1 (individuel) and 10.2 (kollektiv) — only the total 10. Also 6=Produktion (=1+2+3+4+5), so components and totals overlap.
- tid is quarterly: 1999-01-01=Q1, 1999-04-01=Q2, etc.