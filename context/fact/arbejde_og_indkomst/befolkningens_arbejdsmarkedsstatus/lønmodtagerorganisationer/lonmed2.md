table: fact.lonmed2
description: Lønmodtagerorganisationernes medlemstal pr. 31.12 (Hovedorganisationer) efter medlemsorganisationer, køn og tid
measure: indhold (unit Antal)
columns:
- medorg: values [0=Medlemmer i alt, 5=FH Fagbevægelsens Hovedorganisation, 10=Ledernes hovedorganisation, 15=AC - Akademikernes Centralorganisation, 20=Uden for hovedorganisationerne]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- Simple, clean table. medorg=0 (Medlemmer i alt) is exactly the sum of the 4 main organizations (FH + Ledernes + AC + Uden for). No duplicate codes.
- Always filter koen to one value to avoid overcounting: koen='TOT' for all members, 'M'/'K' for gender breakdown.
- medorg covers: 0=grand total, 5=FH Fagbevægelsens Hovedorganisation (largest, ~1M+), 10=Ledernes (~77-115K), 15=AC Akademikernes (~178-342K), 20=Uden for hovedorganisationerne (~249-454K).
- Use this table (not lonmed3) when you want totals or want to compare the 4 main umbrella organizations.