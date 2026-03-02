table: fact.oeko77
description: Salg til foodservice efter varetype, varegruppe, enhed og tid
measure: indhold (unit -)
columns:
- vartyp: values [10=Alle varer, 20=Økologiske varer, 30=Konventionelle varer]
- varegr: values [00=ALLE VARER, A=A. FROSTVARER, A1=A1. Fjerkræ, frost, A2=A2. Okse- og kalvekød, frost, A3=A3. Svinekød, frost ... E2=E2. Okse- og kalvekød, E3=E3. Svinekød, E4=E4. Kødpålæg og andre forarbejdede kødprodukter, E5=E5. Fisk og skaldyr, E6=E6. Andet kød og fisk]
- maengde6: values [30=Mio. kr., 35=Ton]
- tid: date range 2021-01-01 to 2024-01-01

notes:
- vartyp is a type selector: 10=Alle varer (total), 20=Økologiske varer, 30=Konventionelle varer. Confirmed: vartyp=10 equals vartyp=20 + vartyp=30 exactly. Never sum all three vartyp values together. For organic foodservice share, use vartyp=20.
- varegr has a two-level hierarchy: 00=ALLE VARER (grand total), then 5 main categories (A=Frostvarer, B=Kolonialvarer, C=Mejeriprodukter og æg, D=Frugt og grønt, E=Kød og fisk), then sub-categories (A1–A9, B1–B8, C1–C6, D1–D5, E1–E6). Pick one level — don't mix varegr=A with varegr=A1 in a sum.
- maengde6 is a unit selector: 30=Mio. kr., 35=Ton. Always filter to one unit.
- Shortest time series in this subject (2021–2024, only 4 years). Use oeko88 instead if you need data back to 2017.
- For organic share by product category: WHERE vartyp=20 AND varegr IN ('A','B','C','D','E') AND maengde6=30 gives the 5 main categories in value.