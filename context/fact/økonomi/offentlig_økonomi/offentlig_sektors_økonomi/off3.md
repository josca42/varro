table: fact.off3
description: Offentlig forvaltning og service, udgifter og indtægter efter udgifter/indtægter, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- ui: values [1.1=1.1. Aflønning af ansatte, 1.2=1.2. Forbrug i produktionen, 1.3=1.3. Andre produktionsskatter, 1.4=1.4. Sociale ydelser i naturalier, 1.5=1.5. Renter mv. ... 2.15.3.2=2.15.3.2. Udland i øvrigt, 2.16=2.16. Kapitalindtægter i alt (14+15), 2.17=2.17. Drifts- og kapitalindtægter i alt (13+16), 2.18=2.18. Driftsoverskud=bruttoopsparing (2.13-1.8), 2.19=2.19. Offentlig saldo=fordringserhvervelse, netto (2.17-1.17)]
- sektor: values [TOTAL=Offentlig forvaltning og service, S=Stat, F=Sociale kasser og fonde, K+R=Kommuner og regioner, R=Regioner, K=Kommuner]
- tid: date range 1971-01-01 to 2024-01-01
notes:
- ui is a hierarchical account-plan with up to 4 depth levels. Key summary rows: 1.17=Drifts- og kapitaludgifter i alt (all expenditure), 2.17=Drifts- og kapitalindtægter i alt (all revenue), 2.19=Offentlig saldo (public balance). Don't sum all ui values — they overlap heavily across levels. Pick a specific level or an explicit aggregate row.
- sektor: TOTAL aggregates S+F+K+R. Do not sum TOTAL together with subsectors. Note K+R is Kommuner+Regioner combined, which overlaps with separate R and K values.
- Annual (1971–2024). For quarterly use off3k; for revision comparisons use voff3.
