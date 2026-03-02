table: fact.nasd24
description: 3.1 Kapital, investering mv. (detaljeret) efter transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B8GK=B.8g Bruttoopsparing, B12K=B.12 Saldo på udlandskontoens løbende poster, D9K=D.9r Modtaget kapitaloverførsler, D91K=D.91r Modtaget kapitalskatter, D92K=D.92r Modtaget investeringstilskud, D99K=D.99r Modtaget andre kapitaloverførsler, D9D=D.9p Betalt kapitaloverførsler, D91D=D.91p Betalt kapitalskatter, D92D=D.92p Betalt investeringstilskud, D99D=D.99p Betalt andre kapitaloverførsler, P51C4D=P.51c Forbrug af fast realkapital, B101GD=B.101 Ændringer i nettoformue forårsaget af opsparing og kapitaloverførsler, P51GD=P.51g Faste bruttoinvesteringer, P51GD_N111=Heraf boliginvesteringer, P51C5D=P.51c Forbrug af fast realkapital, P52D=P.52 Lagerforøgelser, P53D=P.53 Anskaffelser minus afhændelser af værdigenstande, NPD=NP Anskaffelser af ikke-finansielle ikke-producerede aktiver, netto, B9D=B.9 Fordringserhvervelse, netto]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. Full subsector breakdown including S122A123. Use ColumnValues("nasd24", "sektor") for labels.
- Detailed capital account (chapter 3.1, 1995-2024). Covers the bridge from saving to net lending: saving (B8GK), capital transfers received/paid (D9K/D9D), gross investment (P51GD including housing P51GD_N111), inventory changes (P52D), and final net lending position (B9D).
- P51CD appears twice in the column list (P51C4D and P51C5D) — both represent capital consumption (CFC) used at different points in the account. P51C4D is CFC in the capital finance account; P51C5D is CFC as shown in investment. Use P51GD for gross investment, subtract P51C5D for net.