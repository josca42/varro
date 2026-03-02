table: fact.ligefi7
description: Ligestillingsindikator for børn, der har adresse kun hos mor eller far efter indikator, alder og tid
measure: indhold (unit -)
columns:
- indikator: values [1=Børn, der har adresse hos far (pct.), 2=Børn, der har adresse hos mor (pct.), 3=Forskel mellem børn, der har adresse hos far og børn, der har adresse hos mor (procentpoint)]
- alder: values [TOT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år, 5=5 år, 6=6 år, 7=7 år, 8=8 år, 9=9 år, 10=10 år, 11=11 år, 12=12 år, 13=13 år, 14=14 år, 15=15 år, 16=16 år, 17=17 år]
- tid: date range 1980-01-01 to 2025-01-01
notes:
- indhold contains percentages, not counts (unit is "-"). Never sum across indikator values.
- indikator=1: % of children living only with father. indikator=2: % living only with mother. indikator=3: difference in percentage points (father % minus mother %). These are three independent derived statistics.
- alder has a TOT row but summing percentages across ages is meaningless — use TOT for the overall figure or filter to a specific age.
- No geography. Goes back to 1980 (same long history as ligefb7).
