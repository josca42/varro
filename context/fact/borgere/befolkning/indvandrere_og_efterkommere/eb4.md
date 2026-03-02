table: fact.eb4
description: Befolkningen 1. januar efter herkomst, køn, alder, oprindelsesland, område og tid
measure: indhold (unit Antal)
columns:
- herkomst: values [TOT=I alt, 5A=Personer med dansk oprindelse (ekskl. børn af efterkommere), 4=Indvandrere, 3A=Efterkommere (ekskl. børn af efterkommere), BAE=Børn af efterkommere]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [IALT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- ieland: values [0000=I alt, 5100=Danmark, V=Vestligt land, IV=Ikke-vestligt land]
- omrade: join dim.nuts on omrade=kode; levels [3]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- This is the unified population table including børn af efterkommere as a separate herkomst category (BAE). Use for comparisons across all herkomst groups including this 3rd-generation category.
- herkomst TOT=I alt is the total. Note 5A and 3A explicitly exclude børn af efterkommere — don't add BAE on top of 5A+4+3A+BAE when herkomst='TOT' is available.
- omrade is niveau=3 only (99 kommuner present, no national total). SUM across all kommuner for national count. No national aggregate code.
- ieland=0000 is "I alt". Other values are coarse (Danmark / Vestlig / Ikke-vestlig), not individual countries.
- alder in 5-year bands with IALT as total. No individual-year detail.
- Filter for overcounting: herkomst='TOT', kon='TOT', alder='IALT', ieland='0000' then group by omrade for regional totals.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. No omrade=0 in this table (all rows are kommuner).