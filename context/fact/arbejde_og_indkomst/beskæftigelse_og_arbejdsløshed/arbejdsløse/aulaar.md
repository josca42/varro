table: fact.aulaar
description: Fuldtidsledige (netto) efter køn, personer/pct. og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- perpct: values [L10=Procent af arbejdsstyrken, L9=Ledige (1000 personer)]
- tid: date range 1979-01-01 to 2024-01-01

notes:
- perpct is a measurement selector: L9=count in 1000 persons, L10=rate. Every (kon, tid) row appears twice. Always filter to one perpct.
- Longest historical series in the subject — back to 1979. National only, netto (dagpengeledige), no regional or demographic breakdown.
- "Netto" means dagpengemodtagere only (not including kontanthjælp or aktiverede). For bruttoledige use auf01/aulk01.