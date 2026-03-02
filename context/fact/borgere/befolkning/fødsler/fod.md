table: fact.fod
description: Levendefødte efter moders alder, barnets køn og tid
measure: indhold (unit Antal)
columns:
- modersalder: values [10=10 år, 11=11 år, 12=12 år, 13=13 år, 14=14 år ... 60=60 år, 61=61 år, 62=62 år, 63=63 år, 64=64 år]
- barnkon: values [D=Drenge, P=Piger]
- tid: date range 1973-01-01 to 2024-01-01

notes:
- No total rows in either dimension. modersalder holds individual ages (actual range 12–61, sparser at extremes). barnkon is D/P only with no TOT. To get annual total births, SUM all rows for a given tid with no filtering needed.
- Longest series available for births-by-mother-age (from 1973). For births from 2007 onward with finer breakdown (origin, region, birth order), see fodie/fodpm/fodpf.