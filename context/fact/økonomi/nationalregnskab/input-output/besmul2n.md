table: fact.besmul2n
description: Beskæftigelsesmultiplikator efter multiplikatortype, anvendelsesfordelt stød, branchefordelt effekt, beskæftigelse og tid
measure: indhold (unit Antal)
columns:
- multitype: values [DIR=Direkte effekt, SIMP=Simpel multiplikator, TOTAL=Total multiplikator, TYPEI=Type I multiplikator, TYPEII=Type II multiplikator]
- anvforst: values [ACP01110=01110 Brød og kornprodukter, ACP01120=01120 Kød, ACP01130=01130 Fisk, ACP01141=01141 Mælk, fløde, yoghurt mv., ACP01145=01145 Ost ... ABI5173=Computer software, ABI5179=Originalværker indenfor kunst og underholdning mv., AL5200=Lagre, AV5300=Værdigenstande, AE6000=Eksport]
- brancheeff: join dim.nr_branche on brancheeff=kode [approx]
- beskaeftig: values [BESK1=Beskæftigede, BESK2=Beskæftigede lønmodtagere, BESK3=Fuldtidsbeskæftigede, BESK4=Fuldtidsbeskæftigede lønmodtagere]
- tid: date range 2020-01-01 to 2022-01-01
dim docs: /dim/nr_branche.md

notes:
- Same as besmul1n but shock is in a final demand category (`anvforst`) rather than an industry. Use when the question is "how many jobs does household spending on X support?".
- **multitype and beskaeftig must both be filtered**. See besmul1n notes.
- **anvforst**: 142 detailed A-prefixed final demand codes (same set as promul2n). No dim join. Use ColumnValues("besmul2n", "anvforst").
- **brancheeff**: V-prefixed, join via `SUBSTRING(f.brancheeff, 2) = d.kode`.