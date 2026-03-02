table: fact.off26
description: Offentlig forvaltning og service, forbrugsudgift efter udgifter, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- udgift: values [1=1. Aflønning af ansatte, 2=2. Forbrug af fast realkapital, 3=3. Forbrug i produktion, 4=4. Andre produktionsskatter, 5=5. Andre produktionssubsidier, 6=6. Produktion (1+2+3+4+5), 7=7. Sociale ydelser i naturalier, 8=8. Salg af varer og tjenester, 9=9. Egenproduktion overført til investering, 10=10. Forbrugsudgifter (6+7+8+9), 10.1=10.1. Individuel andel af forbrugsudgifter, 10.2=10.2. Kollektiv andel af forbrugsudgifter]
- sektor: values [TOTAL=Offentlig forvaltning og service, S=Stat, F=Sociale kasser og fonde, K+R=Kommuner og regioner, R=Regioner, K=Kommuner]
- tid: date range 1971-01-01 to 2024-01-01
notes:
- udgift: 10=Forbrugsudgifter i alt (=6+7+8+9), with 10.1=Individuel andel and 10.2=Kollektiv andel as sub-items of 10. Don't sum 10+10.1+10.2 — that triples the total. Also 6=Produktion (=1+2+3+4+5), so don't sum components with their subtotal.
- sektor: TOTAL aggregates all subsektors. Do not mix TOTAL with S/F/K+R/R/K.
- Annual (1971–2024). Quarterly version without sektor breakdown: off26k.
