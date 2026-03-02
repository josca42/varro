table: fact.nasd12
description: 2.1.1 Indkomstdannelse (detaljeret) efter transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B1GK=B.1g  Bruttoværditilvækst, BVT, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, D29D=D.29 Andre produktionsskatter, D39D=D.39 Andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, D11D=D.11 Løn, D12D=D.12 Arbejdsgiverbidrag til sociale ordninger, D121D=D.121 Faktiske arbejdsgiverbidrag til sociale ordninger, D122D=D.122 Imputerede arbejdsgiverbidrag til sociale ordninger, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst, B2GD=B.2g Bruttooverskud af produktion, B3GD=B.3g Blandet bruttoindkomst, P51CD=P.51c Forbrug af fast realkapital, B2A3ND=B.2n+B.3n Nettooverskud af produktion og blandet indkomst, B2ND=B.2n Nettooverskud af produktion, B3ND=B.3n Blandet nettoindkomst]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. Full subsector breakdown including S122A123 (S.122+S.123 combined, no dim.esa match). Use ColumnValues("nasd12", "sektor") for labels.
- Detailed income formation table (chapter 2.1.1, 1995-2024). Covers the labour cost breakdown in detail: D1D=total, D11D=wages, D12D=employer social contributions with D121D (actual) and D122D (imputed). For overview use naso1.
- Key: B1GFD=Bruttofaktorindkomst (=BVT minus production taxes+subsidies). B2A3GD=Bruttooverskud (residual to capital and self-employed).