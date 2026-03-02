table: fact.ligeli3
description: Ligestillingsindikator for løngab efter indikator, arbejdstidens omfang, alder og tid
measure: indhold (unit Pct.)
columns:
- indikator: values [4=Kvinders andel af mænds løn (pct.), 5=Løngab (pct.)]
- arbomfang: values [TOT1=I alt, H=Heltid, D=Deltid]
- alder: values [IALT=Alder i alt, 1819=18-19 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6099=60 år og derover]
- tid: date range 2009-01-01 to 2024-01-01
notes:
- indikator is a measurement-type selector: 4=women's share of men's pay (pct.), 5=pay gap (pct.). ALWAYS filter to one value.
- arbomfang: TOT1=all, H=fuldtid (full-time), D=deltid (part-time). Filter to TOT1 for overall.
- alder here is finer than in ligeli2: IALT=total, then 5-year bands (1819, 2024, 2529, 3034, 3539, 4044, 4549, 5054, 5559, 6099). 10 bands vs 6 in ligeli2 — single-level flat column, no hierarchy issues.
- Annual from 2009. Useful for gender pay gap broken down by full-time vs part-time work, with finer age granularity than ligeli2.
