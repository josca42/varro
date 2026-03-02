table: fact.nasd23
description: 2.4.1 Anvendelse (forbrug og opsparing) af disponibel indkomst (detaljeret) efter transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B6GK=B.6g Disponibel bruttoindkomst, D8K=D.8 Modtaget korrektion for ændringer i pensionsrettigheder, P3D=P.3 Samlede udgifter til forbrug, P31D=P.31 Udgifter til individuelt forbrug, P32D=P.32 Udgifter til kollektivt forbrug, D8D=D.8 Betalt korrektion for ændringer i pensionsrettigheder, B8GD=B.8g Bruttoopsparing, P51C3D=P.51c Forbrug af fast realkapital, B8ND=B.8n Nettoopsparing, B12K=B.12 Saldo på udlandskontoens løbende poster]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. Full subsector breakdown including S122A123. Use ColumnValues("nasd23", "sektor") for labels.
- Detailed use-of-income account (chapter 2.4.1, 1995-2024). Shows how disposable income is used: B6GK=starting point, P3D=total consumption expenditure (P31D individual + P32D collective), D8=pension adjustment, B8GD=gross saving. Annual equivalent of chapter 2.4 in naso2.
- Note: this covers consumption expenditure (P.3), not actual consumption (P.4). For actual consumption including in-kind transfers use nas3/nks3.