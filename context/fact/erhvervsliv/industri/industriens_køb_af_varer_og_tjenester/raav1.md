table: fact.raav1
description: Industriens køb af varer efter varegruppe (2 cifre), branche (DB07), enhed og tid
measure: indhold (unit -)
columns:
- vargr2: values [991=I alt, køb af råvarer, komponenter og hjælpestoffer, 1=01 Levende dyr, 2=02 Kød og spiseligt slagteaffald, 3=03 Fisk og krebsdyr, bløddyr og andre hvirvelløse vanddyr, 4=04 Mælk og mejeriprodukter; fugleæg; naturlig honning; spiselige animalske produkter, ikke andetste ... 93=93 Våben og ammunition samt dele og tilbehør dertil, 94=94 Møbler, madrasser, dyner o.l.; lamper, belysningsartikler; lysskilte og navneplader o.l.; præfab, 95=95 Legetøj, spil og sportsartikler samt dele og tilbehør dertil, 96=96 Diverse, 0=00 Handelsvarer, samt ikke fordelte varer]
- branche07: join dim.nr_branche on branche07=kode [approx]; levels [1, 2, 3]
- enhed: values [V=Værdi (1000 kr.), P=Andel i pct. af omsætning]
- tid: date range 2002-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md

notes:
- enhed is a selector: V=Værdi (1.000 kr.), P=Andel i pct. af omsætning. Always filter to one. Shares (P) should never be summed.
- vargr2 991=I alt (total raw material/component purchases), 0=Handelsvarer samt ikke fordelte varer. Filter to avoid summing aggregates with components. Note: the 991 total row does not equal the sum of individual vargr2 components — DST suppresses some cells for confidentiality. Use vargr2='991' for totals rather than aggregating from components.
- branche07 join with dim.nr_branche: two codes are custom aggregates not in the dim — BC (=B+C combined, confirmed) and CDE (unclear composition; value of 61M in 2023 is far less than C alone at 463M, likely D+E only). Filter them out if you only want individually-reported sectors.
- Single-letter codes B and C match multiple niveaux in dim.nr_branche (B at 1,2,3; C at 1,2). Joining without a niveau filter multiplies rows (3x for B, 2x for C). Use niveau=1 to label B and C. Sub-sector codes CA–CM only exist at niveau=3. Since no single niveau covers all codes, best approach is: join with niveau=1 (labels B, C; leaves CA–CM as NULL) and COALESCE with the branche07 code, or skip the dim join and label branches manually.
- Use ColumnValues("nr_branche", "titel", for_table="raav1") to see the 13 matchable codes with their labels.