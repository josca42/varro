table: fact.frdk125
description: Befolkningsfremskrivning 2025 for hele landet efter herkomst, køn, alder og tid
measure: indhold (unit Antal)
columns:
- herkomst: join dim.herkomst on herkomst=kode [approx]
- kon: values [M=Mænd, K=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 101=101 år, 102=102 år, 103=103 år, 104=104 år, 105-=105 år og derover]
- tid: date range 2025-01-01 to 2070-01-01
dim docs: /dim/herkomst.md

notes:
- herkomst does NOT join dim.herkomst. The table uses its own inline codes (999=dansk oprindelse, 24=indvandrere vestlige, 25=indvandrere ikke-vestlige, 34=efterkommere vestlige, 35=efterkommere ikke-vestlige). Use ColumnValues("frdk125", "herkomst") to see the 5 categories. Ignore the dim.herkomst link.
- alder has no TOT row — only individual ages 0 to 105+. To get a total population, SUM across all ages. No aggregate row to filter on.
- kon has M and K only, no total. SUM across both to get all-gender totals.
- National-level only. For regional or kommune breakdown, use frld125 or frkm125 instead.