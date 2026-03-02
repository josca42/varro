table: fact.pris114
description: Nettoprisindeks efter varegruppe, enhed og tid
measure: indhold (unit Indeks)
columns:
- varegr: join dim.ecoicop_dst on varegr=kode [approx]; levels [1, 4, 5]
- enhed: values [100=Indeks, 200=Ændring i forhold til måneden før (pct.), 300=Ændring i forhold til samme måned året før (pct.)]
- tid: date range 2001-01-01 to 2025-09-01
dim docs: /dim/ecoicop_dst.md

notes:
- enhed is a measurement selector — every varegr×tid combination has 3 rows (100=indeks, 200=MoM%, 300=YoY%). Always filter: WHERE enhed=100 for the index level, enhed=200 for month-on-month, enhed=300 for year-on-year. Omitting this filter triples every count and makes sums meaningless.
- varegr uses a pris114-specific 5-digit coding scheme that does NOT reliably join to dim.ecoicop_dst. The dim join match rate is ~1%. Use ColumnValues("pris114", "varegr") or ColumnValues("pris114", "varegr", fuzzy_match_str="...") to browse the 385 product codes by their text labels instead.
- varegr hierarchy: 5="00 Nettoprisindeks i alt" (total), 10000-120000 are the 12 ECOICOP main groups (e.g. 10000="01 Fødevarer og ikke-alkoholiske drikkevarer"), then sub-groups have codes like 11000, 11100, 11110 (progressively finer). Special aggregate codes: 131000="13.1 Varer i alt", 132000="13.2 Tjenester i alt", 141005="14.1 NPI excl. energi og ikke-forbrugere", 151005="15.1 NPI excl. energi".
- varegr=5 (NPI i alt, enhed=100) matches the monthly headline series in pris116 from 2001 onward. For the full series back to 1980, use pris116 instead.