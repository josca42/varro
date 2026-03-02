table: fact.besmul1n
description: Beskæftigelsesmultiplikator efter multiplikatortype, branchefordelt stød, branchefordelt effekt, beskæftigelse og tid
measure: indhold (unit Antal)
columns:
- multitype: values [DIR=Direkte effekt, SIMP=Simpel multiplikator, TOTAL=Total multiplikator, TYPEI=Type I multiplikator, TYPEII=Type II multiplikator]
- branchest: join dim.nr_branche on branchest=kode [approx]
- brancheeff: join dim.nr_branche on brancheeff=kode [approx]
- beskaeftig: values [BESK1=Beskæftigede, BESK2=Beskæftigede lønmodtagere, BESK3=Fuldtidsbeskæftigede, BESK4=Fuldtidsbeskæftigede lønmodtagere]
- tid: date range 2020-01-01 to 2022-01-01
dim docs: /dim/nr_branche.md

notes:
- Employment multipliers: jobs supported per 1 mio. kr. demand shock in an industry (branchest) across all industries (brancheeff).
- **multitype must be filtered** — DIR, SIMP, TOTAL, TYPEI, TYPEII. Usually use TOTAL.
- **beskaeftig must be filtered** — BESK1=beskæftigede (headcount), BESK2=lønmodtagere, BESK3=fuldtidsbeskæftigede, BESK4=fuldtidsbeskæftigede lønmodtagere. Always filter to one.
- **branchest**: 117 V-prefixed 6-digit codes, mostly outside dim.nr_branche. Use ColumnValues("besmul1n", "branchest") for labels. Dim join unreliable for branchest.
- **brancheeff**: V-prefixed full hierarchy. Join via `SUBSTRING(f.brancheeff, 2) = d.kode`. Use `brancheeff = 'V'` for total economy-wide employment effect.