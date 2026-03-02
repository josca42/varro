table: fact.skres2
description: Skatter der ikke indbetales, periodiseret efter skattetype og tid
measure: indhold (unit Mio. kr.)
columns:
- skatter: values [11A=Kapitaloverførsler fra skatter mv., 22=Produktskatter, 33=Andre produktionsskatter, 44=Indkomstskatter, 55=Andre løbende skatter, 66=Kapitalskatter, 77=Husholdninger, 88=Virksomheder]
- tid: date range 1995-01-01 to 2024-01-01

notes:
- The 8 skatter codes form two overlapping views of the same total. 11A = grand total. 22+33+44+55+66 = breakdown by tax type (verified: sum ≈ 11A). 77+88 = breakdown by sector husholdninger/virksomheder (verified: sum = 11A). Never sum all 8 codes together — you'd triple-count.
- Query pattern: pick one view. Tax-type breakdown: WHERE skatter IN ('22','33','44','55','66'). Sector split: WHERE skatter IN ('77','88'). Grand total: WHERE skatter = '11A'.
