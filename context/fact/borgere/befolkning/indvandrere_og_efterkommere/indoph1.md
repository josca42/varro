table: fact.indoph1
description: Indvandrere 1. januar efter første opholdsgrundlag, område og tid
measure: indhold (unit Antal)
columns:
- ophgr1: values [0=I alt, 13=Asyl mv., 14=Familiesammenføring til flygtning, 15=Familiesammenføring til dansk/nordisk statsborger, 16=Familiesammenføring til udenlandsk statsborger, 501=Arbejde til EU-borger, 502=Arbejde til ikke-EU-borger, 601=Studier - herunder praktikanter - til EU-borger, 602=Studier - herunder praktikanter - til ikke-EU-borger, 901=Øvrige EU-borgere, 701=Au pair, 52=Ukraine (særlov), 801=Andet, 999=Nordiske statsborgere]
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade=0 is the national total ("I alt") — not in dim.nuts. dim.nuts covers niveau=1 (5 regioner) and niveau=3 (98 kommuner present in this table).
- ophgr1 = første opholdsgrundlag (the ORIGINAL permit type when the person first arrived). Use ophgr1=0 for all permit types combined.
- ophgr1 and ophgr2 (in indoph3) differ: ophgr1 is the first/original permit, ophgr2 is the current permit. Nordiske statsborgere (999) and Ukraine særlov (52) are specific categories.
- Compare with indoph3 (nuværende opholdsgrundlag) to see how permit statuses have changed.
- This table covers immigrants only (indvandrere) — not descendants or persons of Danish origin.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.