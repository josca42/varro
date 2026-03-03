table: fact.laby04
description: Familier m/u børn i procent af alle familier i samme kommune eller kommunegruppe efter område, familietype og tid
measure: indhold (unit Pct.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2, 3]
- famtyp: values [TOT=I alt, EUHB=Enlige uden hjemmeboende børn, EMHB=Enlige med hjemmeboende børn, PUHB=Par uden hjemmeboende børn, PMHB=Par med hjemmeboende børn]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- indhold is Pct. (percentage) not counts — these are rates, not counts. Never SUM across omrade or famtyp.
- famtyp=TOT always equals 100.0 — it is the "I alt" total and confirms the other values partition to 100%. The four specific types (EMHB, EUHB, PMHB, PUHB) sum to 100: e.g., København in 2025: 5.9+62.7+13.9+17.5=100.
- omrade joins dim.nuts at niveau 2 (11 landsdele) and niveau 3 (99 kommuner). omrade='0' is the national total. No niveau 1 (regioner) — use niveau 2 for broader regional breakdowns. Use ColumnValues("nuts", "titel", for_table="laby04") to see available codes.
- This is the right table when you want "what share of families in [kommune/landsdel] have children" or "breakdown of family types as percentages."
- Data goes back to 2007 — shorter series than fam44n (1986). For trend analysis before 2007, switch to fam44n and compute percentages from counts.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.