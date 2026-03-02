table: fact.mrs1
description: Grønne afgifter efter branche, miljøkategori og tid
measure: indhold (unit Mio. kr.)
columns:
- branche: join dim.nr_branche on branche=kode [approx]
- skatteart: values [6=I alt inkl. skat på ressourcerente, 0=I alt ekskl. skat på ressourcerente, 3=Forureningsafgifter, 1=Energiafgifter, 5=Transportafgifter, 4=Ressourceafgifter, 2=Skat på ressourcerente]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- branche uses a non-standard coding: V-prefix for industry codes (V01000 → 01000 in dim.nr_branche), underscore instead of hyphen for combined sectors (VD_E → D-E in dim). Special aggregate codes with M-prefix: MTOT=total, MV=brancher i alt, MHUSHOLD=husholdninger, MANDANV=andre endelige anvendelser — these don't join to dim.nr_branche.
- Correct dim join: JOIN dim.nr_branche d ON TRIM(d.kode) = REPLACE(REGEXP_REPLACE(f.branche, '^V', ''), '_', '-'). Note TRIM is needed because niveau 5 codes in dim.nr_branche have a trailing space.
- dim.nr_branche has 5 hierarchy levels. Use for_table filtering: ColumnValues("nr_branche", "titel", for_table="mrs1") to see which codes appear in this table. The table spans niveaus 1–5 — filter d.niveau to pick a consistent aggregation level.
- skatteart: 6 = I alt inkl. ressourcerente (grand total), 0 = I alt ekskl. ressourcerente. Components: 1=Energi, 3=Forurening, 4=Ressource, 5=Transport, 2=Skat på ressourcerente. Sum of 1+3+4+5 = 0, and 0+2 = 6. Filter to one value — don't sum multiple skatteart rows.
- For national totals without branche breakdown: use mreg21 instead (longer series, cleaner structure).