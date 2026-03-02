table: fact.amr2
description: Befolkningens tilknytning til arbejdsmarkedet (fuldtidspersoner) efter socioøkonomisk status, køn, alder, herkomst og tid
measure: indhold (unit Antal)
columns:
- socio: values [21=Ordinær beskæftigelse i alt, 3=Støttet beskæftigelse med løn, 4=Midlertidigt fravær fra beskæftigelse, 50=Arbejdsløse, 80=Støttet beskæftigelse uden løn ... 150=Folkepension, 155=Anden pension, 165=Personer under uddannelse, 170=Børn og unge (ikke under uddannelse), 175=Øvrige uden for arbejdsstyrken]
- kon: values [M=Mænd, K=Kvinder]
- alder: values [-15=Under 16 år, 16-19=16-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-66=65-66 år, 67-=67 år og derover]
- herkomst: values [999=Personer med dansk oprindelse, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande]
- tid: date range 2008-01-01 to 2023-01-01

notes:
- National level only — no regional breakdown. Use amr1 for kommuner/regional queries.
- kon has only M and K (no TOT); alder has 13 age bands (no total). Sum all categories you don't filter on.
- herkomst 5 values: 999=Dansk oprindelse, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande. To get all non-Danish origin: WHERE herkomst IN ('24','25','34','35').
- Same 26 mutually exclusive socio codes as amr1 — summing all gives full national population for the given kon/alder/herkomst/tid cell.
- 31K rows (vs amr1's 605K) — small table, fully granular, no pre-aggregated totals.