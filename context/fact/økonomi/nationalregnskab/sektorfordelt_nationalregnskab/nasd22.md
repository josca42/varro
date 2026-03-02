table: fact.nasd22
description: 2.2 Fordeling af 
sekundær indkomst (detaljeret) efter transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B5GK=B.5g Primær bruttoindkomst, D5_7K=D.5-D.7 Modtaget løbende overførsler, D5K=D.5 Modtaget løbende indkomst- og formueskatter mv., D51K=D.51 Modt Indkomstskatter, D59K=D.59 Modtaget andre løbende skatter ... D75D=D.75 Betalt diverse løbende overførsler, D76D=D.76 Betalt moms- og BNI-baserede egne EU-indtægter, TP=I alt bruttoudgifter, B6GD=B.6g Disponibel bruttoindkomst, B6ND=B.6n Disponibel nettoindkomst]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. Full subsector breakdown including S122A123. Use ColumnValues("nasd22", "sektor") for labels.
- Detailed secondary income distribution table (chapter 2.2, 1995-2024). Covers the full tax/transfer redistribution: taxes received (D5K, D2K), subsidies paid (D3D), social contributions and benefits (D61-D62), and other current transfers. B6GD=Disponibel bruttoindkomst is the bottom line.
- TP=I alt bruttoudgifter is a derived total row, not a specific ESA transaction — it equals the sum of all D-suffix (paid) items. Filter it out when summing.