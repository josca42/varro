table: fact.ligeli2
description: Ligestillingsindikator for løngab efter indikator, arbejdsfunktion, alder og tid
measure: indhold (unit Pct.)
columns:
- indikator: values [4=Kvinders andel af mænds løn (pct.), 5=Løngab (pct.)]
- arbfunk: values [TOT=TOT I alt, 0=0 Militært arbejde, 01=01 Militært arbejde på officersniveau, 011=011 Militært arbejde på officersniveau, 0110=0110 Militært arbejde på officersniveau ... 962=962 Andet manuelt arbejde, 9621=9621 Kurérarbejde og transport af bagage, 9622=9622 Forefaldende arbejde, 9623=9623 Måleraflæsning og tømning af salgsautomater, 9629=9629 Andet manuelt arbejde]
- alder: values [TOT=Alder i alt, 1819=18-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- tid: date range 2010-01-01 to 2024-01-01
notes:
- indikator is a measurement-type selector: 4=women's share of men's pay (pct.), 5=pay gap (pct.). ALWAYS filter to one value — every arbfunk/alder appears twice.
- arbfunk has 601 values across 4 ISCO hierarchy levels: 1-digit (0-9, 10 values), 2-digit (01-96, ~40 values), 3-digit (011-962), 4-digit (0110-9629). Mixing levels in a GROUP BY will massively double-count. Filter to one level: WHERE length(arbfunk)=1 for ISCO major groups, OR length(arbfunk)=2 for sub-major, etc. Or use arbfunk='TOT' for overall. ColumnValues("ligeli2", "arbfunk") gives all 601 codes.
- alder: TOT=all, 1819, 2029, 3039, 4049, 5059, 6099 (6 broad bands). Filter to TOT for all ages.
- Annual from 2010. Useful for gender pay gap breakdown by occupation type and age.
