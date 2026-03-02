table: fact.ppp1
description: Prisniveau indeks for fødevarer EU=100 efter varegruppe, land og tid
measure: indhold (unit -)
columns:
- varegr: values [A010101=Fødevarer, A01010101=Brød og kornprodukter, A01010102=Kød, A01010103=Fisk, A01010104=Mælk, ost og æg, A01010105=Olier og fedtstoffer, A01010106=Frugt, grøntsager og kartofler, A010102=Ikke-alkoholiske drikkevarer, A010201=Alkoholiske drikkevarer, A010202=Tobak]
- land: join dim.lande_uhv on land=kode [approx]; levels [4]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/lande_uhv.md

notes:
- Simplest of the three PPP tables — no measurement selector column. All values are prisniveauindeks with EU=100. Good for straightforward food price level comparisons.
- `varegr` has 10 codes at exactly 2 levels: A010101 (Fødevarer, parent) and 6 subcategories (A01010101–A01010106 for food subtypes), plus A010102 (Ikke-alkoholiske drikkevarer), A010201 (Alkoholiske drikkevarer), A010202 (Tobak). Don't include both A010101 and its children in the same aggregation.
- `land` joins dim.lande_uhv at niveau=4 for 30 countries. DK (Danmark) is the only unmatched code — reference it directly as `land='DK'`.
- This table has the longest time range for food: 2006–2024. Use ppp (2000–2023) if you need pre-2006 data or non-food categories.