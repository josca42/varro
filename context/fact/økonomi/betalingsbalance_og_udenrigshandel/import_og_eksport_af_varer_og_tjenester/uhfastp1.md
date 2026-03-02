table: fact.uhfastp1
description: Udenrigshandel i faste priser månedlig (eksperimentel statistik) efter poster, im- og eksport, prisenhed, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- post: values [1.A.A=VARER, 1.A.A.1.0-4X2-3=Næringsmidler, drikkevarer, tobak mv., 1.A.A.1.3=Mineral, brændsels- og smørestoffer o.l., 1.A.A.1.5-9X78-79=Kemikaler, forarbejdede varer, maskiner og færdigvarer i alt]
- indud: values [1=Import, 2=Eksport]
- prisenhed: values [VRD_T=Løbende priser, MGD_T=2021-priser]
- saeson: values [1=Ikke sæsonkorrigeret, 2=Sæsonkorrigeret]
- tid: date range 2010-01-01 to 2025-09-01

notes:
- Experimental statistics (eksperimentel statistik) — use with caution.
- prisenhed is a measurement selector — every row exists twice: VRD_T (løbende priser) and MGD_T (2021-priser). Always filter to one: `prisenhed = 'VRD_T'` for current prices or `prisenhed = 'MGD_T'` for volume comparison. Forgetting this doubles all sums.
- saeson must also be filtered — both values exist for all combinations. Use `saeson = 1` for raw data.
- No land column — no geographic breakdown. Covers only VARER (1.A.A.*) — no tjenester.
- post is hierarchical: 1.A.A is the goods total; subcategories (1.A.A.1.0-4X2-3, 1.A.A.1.3, 1.A.A.1.5-9X78-79) are components. Do not sum across post levels — pick either the total (1.A.A) or individual sub-categories.
- Typical query: `WHERE prisenhed = 'MGD_T' AND saeson = 1 AND post = '1.A.A'` for total goods trade in constant 2021 prices.