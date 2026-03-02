table: fact.ligedi10
description: Ligestillingsindikator for regeringer efter regeringer, indikator og tid
measure: indholm (unit -)
columns:
- regering: values [1=Deuntzer (1901), 2=Christensen I (1905), 3=Christensen II (1908), 4=Neergaard I (1908), 5=Holstein-Ledreborg (1909) ... 55=Helle Thorning-Schmidt II (2014), 56=Lars Løkke Rasmussen II (2015), 57=Lars Løkke Rasmussen III (2016), 58=Mette Frederiksen I (2019), 59=Mette Frederiksen II (2022)]
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- tid: date range 2022-01-01 to 2022-01-01

notes:
- tid=2022-01-01 is the publication/release date, not a filter on year. All 59 Danish governments since 1901 are available — browse using the regering column. Do not filter by tid (there is only one value).
- regering values are sequential integers (1–59) corresponding to governments in chronological order. The text label includes the government name and start year in parentheses.
- indikator: LA1=share of men (%), LA2=share of women (%), LA3=LA1−LA2. Never sum across indikator. Pick one.
- This table is about cabinet gender composition, not election results or candidates.
