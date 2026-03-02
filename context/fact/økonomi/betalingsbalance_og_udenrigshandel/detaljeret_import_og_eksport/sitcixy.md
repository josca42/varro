table: fact.sitcixy
description: Indeks for importen og eksporten efter im- og eksport, indekstype, SITC-hovedgrupper og tid
measure: indhold (unit Indeks)
columns:
- indud: values [1=Import, 2=Eksport]
- indekstype: values [KVANTUM=Kvantumindeks, ENHED=Enhedsværdiindeks]
- sitc: join dim.sitc on sitc=kode; levels [1]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/sitc.md

notes:
- indekstype is a MEASUREMENT SELECTOR: KVANTUM or ENHED. Always filter to one — never sum across both.
- sitc at niveau 1 (11 SITC afdelinger). No seasonal adjustment column — simpler than sitcixm.
- Annual data 2007–2024. For monthly series with seasonal adjustment option see sitcixm.
- Indices are base-year scaled values; do not sum across sitc groups.