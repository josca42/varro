<fact tables>
<table>
id: naiovb
description: Importkorrigerede vækstbidrag efter anvendelse og tid
columns: anvendelse, tid (time), indhold (unit Procentpoint)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: naio1
description: Input-output tabel. Tilgang fra brancher fordelt på anvendelse og prisenhed efter tilgangstype, tilgang fra branche, anvendelse, prisenhed og tid
columns: tilgang1, tilgang2, anvendelse, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 1966-01-01 to 2022-01-01
</table>
<table>
id: naio1f
description: Input-output tabel. Tilgang fra brancher fordelt på anvendelse og prisenhed. (69-gruppering) efter tilgangstype, tilgang fra branche, anvendelse, prisenhed og tid
columns: tilgang1, tilgang2, anvendelse, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 1966-01-01 to 2024-01-01
</table>
<table>
id: naio2
description: Input-output tabel. Ikke branchefordelt import efter anvendelse og prisenhed efter tilgangstype, anvendelse, prisenhed og tid
columns: tilgang1, anvendelse, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 1966-01-01 to 2022-01-01
</table>
<table>
id: naio2f
description: Input-output tabel. Ikke branchefordelt import efter anvendelse og prisenhed. (69-gruppering) efter tilgangstype, anvendelse, prisenhed og tid
columns: tilgang1, anvendelse, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 1966-01-01 to 2024-01-01
</table>
<table>
id: naio3
description: Input-output tabel. Primære input fordelt efter anvendelse og prisenhed efter tilgangstype, anvendelse, prisenhed og tid
columns: tilgang1, anvendelse, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 1966-01-01 to 2022-01-01
</table>
<table>
id: naio3f
description: Input-output tabel. Primære input fordelt efter anvendelse og prisenhed. (69-gruppering) efter tilgangstype, anvendelse, prisenhed og tid
columns: tilgang1, anvendelse, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 1966-01-01 to 2024-01-01
</table>
<table>
id: naio4
description: Input-output tabel. Totaler for tilgang fordelt efter anvendelse og prisenhed efter tilgangstype, anvendelse, prisenhed og tid
columns: tilgang1, anvendelse, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 1966-01-01 to 2022-01-01
</table>
<table>
id: naio4f
description: Input-output tabel. Totaler for tilgang fordelt efter anvendelse og prisenhed. (69-gruppering) efter tilgangstype, anvendelse, prisenhed og tid
columns: tilgang1, anvendelse, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 1966-01-01 to 2024-01-01
</table>
<table>
id: naio5
description: Beskæftigelse og timer efter socioøkonomisk status, branche og tid
columns: socio, branche, tid (time), indhold (unit -)
tid range: 1966-01-01 to 2022-01-01
</table>
<table>
id: naio5f
description: Beskæftigelse og timer (69-gruppering) efter socioøkonomisk status, branche og tid
columns: socio, branche, tid (time), indhold (unit -)
tid range: 1966-01-01 to 2024-01-01
</table>
<table>
id: promul1n
description: Produktionsmultiplikator efter multiplikatortype, branchefordelt stød, branchefordelt effekt og tid
columns: multitype, branchest, brancheeff, tid (time), indhold (unit Mio. kr.)
tid range: 2020-01-01 to 2022-01-01
</table>
<table>
id: promul2n
description: Produktionsmultiplikator efter multiplikatortype, anvendelsesfordelt stød, branchefordelt effekt og tid
columns: multitype, anvforst, brancheeff, tid (time), indhold (unit Mio. kr.)
tid range: 2020-01-01 to 2022-01-01
</table>
<table>
id: besmul1n
description: Beskæftigelsesmultiplikator efter multiplikatortype, branchefordelt stød, branchefordelt effekt, beskæftigelse og tid
columns: multitype, branchest, brancheeff, beskaeftig, tid (time), indhold (unit Antal)
tid range: 2020-01-01 to 2022-01-01
</table>
<table>
id: besmul2n
description: Beskæftigelsesmultiplikator efter multiplikatortype, anvendelsesfordelt stød, branchefordelt effekt, beskæftigelse og tid
columns: multitype, anvforst, brancheeff, beskaeftig, tid (time), indhold (unit Antal)
tid range: 2020-01-01 to 2022-01-01
</table>
<table>
id: inpmul1n
description: Inputmultiplikator efter multiplikatortype, branchefordelt stød, branchefordelt effekt, input og tid
columns: multitype, branchest, brancheeff, input, tid (time), indhold (unit Mio. kr.)
tid range: 2020-01-01 to 2022-01-01
</table>
<table>
id: inpmul2n
description: Inputmultiplikator efter multiplikatortype, anvendelsesfordelt stød, branchefordelt effekt, input og tid
columns: multitype, anvforst, brancheeff, input, tid (time), indhold (unit Mio. kr.)
tid range: 2020-01-01 to 2022-01-01
</table>
</fact tables>

notes:
- **naio1–4 vs naio1f–4f**: The "f" suffix = 69-gruppering (niveau 4, 5-digit industry codes). Non-f tables include full DB07 detail (117+ 6-digit codes) but only to 2022. F-tables cover to 2024. Prefer f-tables unless sub-69-group detail is needed.
- **naio1/naio1f**: Full symmetric IO table (industry × industry + final demand). Use for input-output analysis, supply chain tracing, or detailed industry structure. Has two prefixed industry columns (`tilgang2` = supply-side, `anvendelse` = demand-side/final demand).
- **naio2/naio2f**: Non-industry-allocated imports (tourism, Nordsø oil, unspecified). Feeds into naio4 totals. Rarely queried standalone.
- **naio3/naio3f**: Primary inputs (wages D1, gross surplus B2A3G, taxes) by industry. Use for "wages/taxes/GVA by sector" questions.
- **naio4/naio4f**: Column totals of the IO table. Use for quick total supply/demand by industry without joining naio1+naio2+naio3.
- **naio5/naio5f**: Employment and hours by industry (back to 1966). Use for labor market by sector. `socio` is a 9-value measurement selector — always filter to one.
- **naiovb**: Import-corrected growth contributions by final demand category (percentage points, 2006–2024). Use for "what drove GDP growth?" questions. No dim joins.
- **Multiplier tables (promul, besmul, inpmul)**: Economic impact analysis, 2020–2022 only. Three families: production (promul), employment (besmul), input/income (inpmul). Within each family: "1n" = industry shock (branchest), "2n" = final demand shock (anvforst). Always filter `multitype`; also filter `beskaeftig` (besmul) or `input` (inpmul).
- **Universal coding pattern for all tables**: Industry/branch columns use a letter prefix (T=Tilgang, A=Anvendelse, V=Virksomhed). The documented dim joins `f.column = d.kode` do NOT work. Always strip the first character: `SUBSTRING(f.column, 2) = d.kode`. Use `d.niveau` to control hierarchy (niveau 1=13 top groups, niveau 4=69-gruppering, niveau 5=117 codes).
- **prisenhed** (naio1–4 only): Always filter to V (løbende priser) or Y (foregående års priser) — forgetting silently doubles all values.
- **tilgang1** (naio1–4): Always filter — contains 3–6 supply/input type categories that are not additive (or where one is the sum of the others).