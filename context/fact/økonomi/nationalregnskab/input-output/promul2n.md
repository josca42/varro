table: fact.promul2n
description: Produktionsmultiplikator efter multiplikatortype, anvendelsesfordelt stød, branchefordelt effekt og tid
measure: indhold (unit Mio. kr.)
columns:
- multitype: values [DIR=Direkte effekt, SIMP=Simpel multiplikator, TOTAL=Total multiplikator]
- anvforst: values [ACP01110=01110 Brød og kornprodukter, ACP01120=01120 Kød, ACP01130=01130 Fisk, ACP01141=01141 Mælk, fløde, yoghurt mv., ACP01145=01145 Ost ... ABI5173=Computer software, ABI5179=Originalværker indenfor kunst og underholdning mv., AL5200=Lagre, AV5300=Værdigenstande, AE6000=Eksport]
- brancheeff: join dim.nr_branche on brancheeff=kode [approx]
- tid: date range 2020-01-01 to 2022-01-01
dim docs: /dim/nr_branche.md

notes:
- Same as promul1n but the shock is in a final demand category (`anvforst`) rather than an industry. Use this when the question involves "what if households spend more on X" rather than "what if industry Y produces more".
- **multitype must be filtered** (DIR, SIMP, TOTAL). See promul1n notes.
- **anvforst** (shocked final demand): 142 detailed A-prefixed codes covering household consumption (ACP01xxx), investment categories (ABI, ACOMI), and exports (AE6000). No dim join. Use ColumnValues("promul2n", "anvforst") to browse. These correspond to the detailed final demand breakdown in naiovb/naio1 `anvendelse`.
- **brancheeff** (industry receiving effect): same V-prefixed join as promul1n — `SUBSTRING(f.brancheeff, 2) = d.kode`.