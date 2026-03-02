table: fact.firegn1
description: Regnskabsstatistik for fiskeri (total) efter fartøjslængde, regnskabsposter og tid
measure: indhold (unit -)
columns:
- farlaengd: values [9=ALLE VIRKSOMHEDER, 10=FARTØJER UNDER 12 METER, 40=Garn/krog under 12 m, 48=Jolle/ruse under 12 m, 50=Snur/garn/trawl under 12 m ... 20=FARTØJER 40,0 METER OG OVER, 78=Trawl industri over 40 m, 82=Not/trawl andet over 40 m, 84=HESTEREJEFISKERI, 86=MUSLINGEFISKERI]
- regnskposter: values [Q100=Q.1 Population, antal, Q105=Q.2  Stikprøve, antal, A100=A.1 Erhvervsaktiver, primo, 1000 kr, A105=A.2 Fartøjets tonnage, bruttoton, A110=A.3 Fartøjsindsats, havdage ... O125=O.3.2 Betalt skat, 1000 kr., O130=O.3.3 Akkord på gæld, 1000 kr., O135=O.3.4 Andre engangsposter, 1000 kr., O140=O.4 Indskud fra ejere, 1000 kr., O145=O.5 Saldo ultimo]
- tid: date range 2009-01-01 to 2023-01-01

notes:
- firegn1 holds TOTALS (aggregate sums for all vessels in each segment). Contrast with firegn2 which holds averages per vessel. Use firegn1 for absolute amounts (total revenue, total costs), firegn2 for per-vessel comparisons.
- farlaengd has a two-tier hierarchy. Size-class aggregates (UPPERCASE): 9=alle, 10=under 12m, 12=12-14.9m, 14=15-17.9m, 16=18-23.9m, 18=24-39.9m, 20=40m+. Gear/type subcategories within each size class (lowercase labels): codes 40-86. Never sum across both tiers — filter to one tier only. For a by-size breakdown, use codes 9/10/12/14/16/18/20.
- regnskposter has 204 distinct accounting line items spanning balance sheet (A), income (B), costs, and financial ratios. Each line item is a different financial concept with its own unit (1000 kr, bruttoton, havdage, etc.) — read the label carefully. Never aggregate across regnskposter.
- ColumnValues("firegn1", "regnskposter") returns the full list of accounting line items with codes and labels.