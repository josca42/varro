table: fact.sitcixm
description: Indeks for udenrigshandel med varer efter im- og eksport, indekstype, sæsonkorrigering, SITC-hovedgrupper og tid
measure: indhold (unit Indeks)
columns:
- indud: values [1=Import, 2=Eksport]
- indekstype: values [KVANTUM=Kvantumindeks, ENHED=Enhedsværdiindeks]
- saeson2: values [1=Ikke sæsonkorrigeret, 2=Sæsonkorrigeret]
- sitc: join dim.sitc on sitc=kode; levels [1]
- tid: date range 2007-01-01 to 2025-09-01
dim docs: /dim/sitc.md

notes:
- indekstype is a MEASUREMENT SELECTOR: KVANTUM=volume index, ENHED=unit value index. These are independent measures — never sum. Always filter to one.
- saeson2 is a MEASUREMENT SELECTOR: 1=Ikke sæsonkorrigeret, 2=Sæsonkorrigeret. Always filter to one. Combined with indekstype, each sitc+indud+tid cell appears 4 times (2×2). Forgetting either selector gives 4× inflation.
- sitc is at niveau 1 (11 SITC afdelinger = coarse commodity divisions). No hierarchy issue.
- Monthly data 2007–2025. For annual without seasonal adjustment see sitcixy. For aggregate index without SITC breakdown see uhixm/uhixy.