table: fact.lbesk43
description: Lønmodtagere efter enhed, herkomst, køn, alder og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- herkomst: join dim.herkomst on herkomst=kode::text [approx]; levels [1]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder, UDK=Uoplyst køn, uden bopæl i Danmark]
- alder: values [TOT=Alder i alt, U15=Under 15 år, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6064=60-64 år, 6574=65-74 år, 75OV=75 år og derover, UDK=Uoplyst alder, uden bopæl i Danmark]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/herkomst.md
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- WARNING: dim.herkomst join is mostly broken (only code 1 matches). herkomst uses a more granular coding than dim.herkomst: 1=Dansk oprindelse, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande, TOT=I alt, UDK=Uoplyst. Treat as inline — do NOT join dim.herkomst.
- Note: 24+25 together = all indvandrere; 34+35 = all efterkommere. This table gives the vestlig/ikke-vestlig split not available in dim.herkomst.
- Filter all dimensions to avoid overcounting: filter tal, herkomst (exclude TOT/UDK unless needed), kon (exclude TOT unless summing), alder (exclude TOT unless summing).
- alder groups: U15, 1519, 2024, 2529, 3034, 3539, 4044, 4549, 5054, 5559, 6064, 6574, 75OV — 5-year bands (not individual ages). TOT=sum of all.
