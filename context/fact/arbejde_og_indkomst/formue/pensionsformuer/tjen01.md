table: fact.tjen01
description: Optjent tjenestemandspension for aktive tjenestemænd efter sektor, enhed, køn, faggruppe aldersgrupper og tid
measure: indhold (unit -)
columns:
- sektor: values [100=Alle tjenestemænd, 105=Tjenestemænd ansat i staten, 110=Tjenestemænd ansat i Kommuner/regioner]
- enhed: values [100=Antal aktive tjenestemænd, 105=Værdi af optjent pension (1.000 kr.), 110=Værdi af gennemsnitlig optjent pension (1.000 kr.)]
- koen: values [0=Mænd og kvinder i alt, 1=Mænd, 2=Kvinder]
- faggrp: values [A=ALDERSGRUPPER I ALT, A1=Under 35 år, A2=Mellem 36 og 59 år, A3=Over 60 år, B=SAMTLIGE FAGGRUPPER ... B12=Pædagoger, B13=Domstolsvæsen, B14=Flytjenesten, B15=Apotekere, B16=Scandlines]
- tid: date range 2014-01-01 to 2023-01-01

notes:
- enhed is a measurement selector — every sektor/koen/faggrp/tid combination is repeated 3 times (antal, sum, gennemsnit). Always filter to exactly one enhed value. Summing across enhed gives meaningless results.
- faggrp encodes two alternative classification schemes in one column: A-prefix = aldersgrupper (A=total, A1=under 35, A2=36-59, A3=over 60), B-prefix = faggrupper (B=total, B1-B16 specific groups). Both schemes are present for every other dimension combination. Pick either A-rows OR B-rows — never sum across both. To get totals use A for age-breakdown or B for occupational-breakdown, filtering the other to its respective total (A or B).
- sektor=100 (Alle tjenestemænd) is the sum of 105 (staten) + 110 (kommuner/regioner). Filter to leaf codes to avoid double-counting.
- Sample query: aktive tjenestemænd i alt 2023 by faggruppe: WHERE enhed='100' AND faggrp LIKE 'B%' AND sektor='100' AND koen='0'.