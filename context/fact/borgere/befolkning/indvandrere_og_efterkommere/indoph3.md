table: fact.indoph3
description: Indvandrere 1. januar efter nuværende opholdsgrundlag, område og tid
measure: indhold (unit Antal)
columns:
- ophgr2: values [0=I alt, 13=Asyl mv., 14=Familiesammenføring til flygtning, 15=Familiesammenføring til dansk/nordisk statsborger, 16=Familiesammenføring til udenlandsk statsborger, 501=Arbejde til EU-borger, 502=Arbejde til ikke-EU-borger, 601=Studier - herunder praktikanter - til EU-borger, 602=Studier - herunder praktikanter - til ikke-EU-borger, 901=Øvrige EU-borgere, 701=Au pair, 52=Ukraine (særlov), 801=Andet, 9998=Permanent opholdstilladelse, 999=Nordiske statsborgere]
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade=0 is the national total ("I alt") — not in dim.nuts. dim.nuts covers niveau=1 (5 regioner) and niveau=3 (98 kommuner).
- ophgr2 = nuværende opholdsgrundlag (CURRENT permit type). Adds code 9998=Permanent opholdstilladelse compared to ophgr1 in indoph1. Use ophgr2=0 for all permit types.
- Key difference from indoph1: ophgr1 shows the permit type when the person FIRST arrived; ophgr2 shows their CURRENT permit. Many asylum seekers will have moved to permanent residence (9998) over time.
- This table covers immigrants only (indvandrere), not descendants or persons of Danish origin.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.