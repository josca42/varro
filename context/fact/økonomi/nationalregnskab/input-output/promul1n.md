table: fact.promul1n
description: Produktionsmultiplikator efter multiplikatortype, branchefordelt stød, branchefordelt effekt og tid
measure: indhold (unit Mio. kr.)
columns:
- multitype: values [DIR=Direkte effekt, SIMP=Simpel multiplikator, TOTAL=Total multiplikator]
- branchest: join dim.nr_branche on branchest=kode [approx]
- brancheeff: join dim.nr_branche on brancheeff=kode [approx]
- tid: date range 2020-01-01 to 2022-01-01
dim docs: /dim/nr_branche.md

notes:
- Production multipliers: the output effect per additional unit of demand shock in an industry (branchest) across all affected industries (brancheeff).
- **multitype must be filtered to one value** — DIR=direct effect only, SIMP=includes first-round suppliers, TOTAL=full supply chain. For economic impact analysis, typically use TOTAL.
- **branchest** (shocked industry): 117 V-prefixed 6-digit codes only. Most do NOT match dim.nr_branche (only 19 of 117 match niveau 5). Use ColumnValues("promul1n", "branchest") to see codes with their inline text labels — dim join is not reliable for branchest.
- **brancheeff** (industry receiving effect): V-prefixed, full hierarchy (all niveaux). Join via `SUBSTRING(f.brancheeff, 2) = d.kode`. Filter `d.niveau` to control aggregation. Use `brancheeff = 'V'` to get the total economy-wide effect.
- Only 3 years of data (2020–2022). Use for structural cross-section analysis, not trend.
- Interpretation example: `branchest='V010000'`, `brancheeff='V'`, `multitype='TOTAL'`, `indhold≈1.196` means 1 kr extra demand in agriculture generates ~1.20 kr production economy-wide.