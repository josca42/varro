table: fact.inpmul1n
description: Inputmultiplikator efter multiplikatortype, branchefordelt stød, branchefordelt effekt, input og tid
measure: indhold (unit Mio. kr.)
columns:
- multitype: values [DIR=Direkte effekt, SIMP=Simpel multiplikator, TOTAL=Total multiplikator, TYPEI=Type I multiplikator, TYPEII=Type II multiplikator]
- branchest: join dim.nr_branche on branchest=kode [approx]
- brancheeff: join dim.nr_branche on brancheeff=kode [approx]
- input: values [INDK=Indkomst (aflønning af ansatte), IMP=Import, BVT=Bruttoværditilvækst (BVT)]
- tid: date range 2020-01-01 to 2022-01-01
dim docs: /dim/nr_branche.md

notes:
- Input multipliers: how much income (wages), import, or gross value added (BVT) is generated per 1 mio. kr. demand shock in an industry.
- **multitype must be filtered** (DIR, SIMP, TOTAL, TYPEI, TYPEII). Usually use TOTAL.
- **input must be filtered** — INDK=Indkomst/aflønning af ansatte (wages), IMP=Import, BVT=Bruttoværditilvækst. These are three independent measures; always filter to one.
- **branchest**: 117 V-prefixed 6-digit codes. Dim join unreliable; use ColumnValues("inpmul1n", "branchest").
- **brancheeff**: V-prefixed full hierarchy. Join via `SUBSTRING(f.brancheeff, 2) = d.kode`.