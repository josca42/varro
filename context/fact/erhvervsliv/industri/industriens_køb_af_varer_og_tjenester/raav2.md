table: fact.raav2
description: Industriens køb af emballage efter varegruppe (6 cifre), branche (DB07), enhed og tid
measure: indhold (unit 1.000 kr.)
columns:
- vargr6: values [992=I alt, køb af emballage, 39E=Emballage af plast, 392090=392090 Folie af plast, 392391=392391 Baljer og spande af plast, 392392=392392 Ballonner, flasker, dunke o.l. beholdere af plast ... 761293=761293 Andre emballageartikler af aluminium, 83E=Anden emballage, 830990=830990 Emballageartikler af andre uædle metaller, 009691=009691 Emballageartikler af andre materialer end nævnte, 000300=000300 Ikke-fordelte emballageartikler]
- branche07: join dim.nr_branche on branche07=kode [approx]; levels [1, 2, 3]
- enhed: values [V=Værdi (1000 kr.), P=Andel i pct. af omsætning]
- tid: date range 2002-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md

notes:
- enhed is a selector: V=Værdi (1.000 kr.), P=Andel i pct. af omsætning. Always filter to one — P values are rates and must not be summed.
- vargr6 hierarchy: 992=grand total (I alt køb af emballage), codes with uppercase letter suffix (39E, 48E, 44E, 76E, 73E, 83E)=chapter-level aggregate groups, 6-digit numeric codes=detail level. Filter to one level to avoid double-counting.
- Same branche07 structure as raav1: 15 codes including custom aggregates BC (=B+C) and CDE (likely D+E only). Same niveau duplication issue when joining dim.nr_branche — use niveau=1 for B/C labels; CA–CM only at niveau=3. See raav1 notes for join strategy.