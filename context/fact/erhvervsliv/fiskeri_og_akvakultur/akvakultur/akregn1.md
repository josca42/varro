table: fact.akregn1
description: Regnskabsstatistik for akvakultur efter enhed, anlægstype, regnskabsposter og tid
measure: indhold (unit -)
columns:
- enhed: values [1=Total, 5=Gennemsnit pr. anlæg]
- anlaeg: values [0=Alle anlæg, 6=Traditionelle dambrug, 11=Anlæg med lav recirkulation , 12=Anlæg med middelhøj recirkulation, 13=Anlæg med høj recirkulation , 25=Havbrug, 36=Muslinge- og østersanlæg]
- regnskposter: values [Q100=Q.1 Population, antal, Q105=Q.2  Stikprøve, antal, A100=A.1 Erhvervsaktiver, primo, 1000 kr, A145=A.5 Yngel og sættefisk, ton, A150=A.6 Øjenæg, 1000 stk. ... O125=O.3.2 Betalt skat, 1000 kr., O130=O.3.3 Akkord på gæld, 1000 kr., O135=O.3.4 Andre engangsposter, 1000 kr., O140=O.4 Indskud fra ejere, 1000 kr., O145=O.5 Saldo ultimo]
- tid: date range 2017-01-01 to 2023-01-01

notes:
- enhed is a measurement selector: 1=Total (aggregate across all facilities in the sample), 5=Gennemsnit pr. anlæg (per-facility average). Every anlaeg×regnskposter×tid row is duplicated for each enhed. Always filter to one value. Use enhed=1 for sector totals, enhed=5 for per-facility comparisons.
- regnskposter has 170 codes covering different financial line items (assets, liabilities, income, costs, equity changes). Each code has its unit embedded in the label (e.g. "1000 kr", "ton", "1000 stk.", "pct"). Do not sum across different regnskposter codes — they have incompatible units. Always filter to a specific regnskposter.
- Use ColumnValues("akregn1", "regnskposter") to browse all 170 codes. Codes are grouped by letter prefix: Q=population/sample counts, A=assets, B=liabilities, C/D=income/costs (different facility types), E=employment, H=owner compensation, O=equity changes, P=ratios.
- anlaeg=0 is Alle anlæg (the aggregate). Other values are individual facility types. Do not sum anlaeg=0 with the parts.