table: fact.flyv34
description: Flyrejser med rute- og charterfly mellem større, offentlige, betjente lufthavne og udlandet efter lufthavn, destinationsland, retning og tid
measure: indhold (unit 1.000 stk.)
columns:
- lufthavn: values [10010=LUFTHAVNE IALT, 10015=København, 10020=Billund, 10070=Øvrige lufthavne]
- desti: values [IA=I alt, FR=Frankrig og Monaco, DE=Tyskland, GB=Storbritannien, ES=Spanien, NO=Norge, SE=Sverige, EUA=Europa i øvrigt, ANL=Andre lande]
- ret: values [0=I alt, 3=Ankommende, 5=Afrejsende]
- tid: date range 2004-01-01 to 2024-01-01

notes:
- ret is a measurement selector with a total: ret=0 (I alt) = ret=3 (Ankommende) + ret=5 (Afrejsende). Always filter to one ret value to avoid double-counting.
- desti=IA is the total across all destinations. The 8 other codes are: 6 named countries plus EUA (Europe, other) and ANL (other countries) — they should sum to IA.
- lufthavn only has 3 individual codes (KBH, Billund, Øvrige) plus the total — less granular than flyv31/32. Use flyv32 if per-airport detail is needed.
- International routes only. Annual data.
