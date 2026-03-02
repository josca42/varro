table: fact.fodpm
description: Levendefødte efter moders alder, levendefødtnummer og tid
measure: indhold (unit Antal)
columns:
- modersalder: values [10=10 år, 11=11 år, 12=12 år, 13=13 år, 14=14 år ... 60=60 år, 61=61 år, 62=62 år, 63=63 år, 64=64 år]
- lfnr: values [1=1. barn, 2=2. barn, 3=3. barn, 4=4. barn, 5=5. barn, 6=6. barn, 7=7. barn, 8+=8. barn og flere, 99=Uoplyst]
- tid: date range 2007-01-01 to 2024-01-01
notes:
- No total rows in either column. modersalder holds individual ages (actual range 13–61, sparser at extremes; the listed range 10–64 is wider than what's actually in the data). lfnr is birth-order 1–7 and 8+ — the listed 99=Uoplyst is absent from the actual data.
- All lfnr categories are mutually exclusive (each birth is counted once). SUM all rows for a given tid and modersalder to get total births at that mother's age.
- Use fodpf for the equivalent table broken down by father's age instead of mother's age.
