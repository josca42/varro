table: fact.firegn2
description: Regnskabsstatistik for fiskeri (gennemsnit pr. enhed) efter fartøjslængde, regnskabsposter og tid
measure: indhold (unit -)
columns:
- farlaengd: values [9=ALLE VIRKSOMHEDER, 10=FARTØJER UNDER 12 METER, 40=Garn/krog under 12 m, 48=Jolle/ruse under 12 m, 50=Snur/garn/trawl under 12 m ... 20=FARTØJER 40,0 METER OG OVER, 78=Trawl industri over 40 m, 82=Not/trawl andet over 40 m, 84=HESTEREJEFISKERI, 86=MUSLINGEFISKERI]
- regnskposter: values [Q100=Q.1 Population, antal, Q105=Q.2  Stikprøve, antal, A100=A.1 Erhvervsaktiver, primo, 1000 kr, A105=A.2 Fartøjets tonnage, bruttoton, A110=A.3 Fartøjsindsats, havdage ... O125=O.3.2 Betalt skat, 1000 kr., O130=O.3.3 Akkord på gæld, 1000 kr., O135=O.3.4 Andre engangsposter, 1000 kr., O140=O.4 Indskud fra ejere, 1000 kr., O145=O.5 Saldo ultimo]
- tid: date range 2009-01-01 to 2023-01-01

notes:
- firegn2 holds AVERAGES per vessel (gennemsnit pr. enhed). Contrast with firegn1 which holds totals. Use firegn2 to compare vessel profitability across size segments; use firegn1 for sector totals.
- Same farlaengd two-tier hierarchy as firegn1: size-class aggregates (9, 10, 12, 14, 16, 18, 20) vs gear-type subcategories (40-86). Filter to one tier — summing or averaging across both gives wrong results.
- Same 204 regnskposter accounting items as firegn1, but values here are per-vessel averages. Do not sum across regnskposter.
- Q100 (population antal) and Q105 (stikprøve antal) are counts of vessels in each segment, not financial figures — useful for context but not monetary.