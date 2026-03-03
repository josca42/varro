table: fact.penindb1
description: Personer med pensionsindbetalinger efter område, enhed, køn, alder, pensionstype og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- enhed: values [123=Personer med pensionstypen (antal), 124=Indbetalt beløb (1.000 kr.), 125=Gennemsnitlig indbetaling for alle personer (kr.), 126=Gennemsnitlig indbetaling for personer med pensionstype (kr.)]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- alder1: values [TOT=Alder i alt, 25UN=Under 25 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 65-=65 år og derover]
- pentyp: values [20=Alle som indbetaler på pensionordninger, 21=Arbejdsgiveradministrerede indbetalinger, 22=Privat tegnede indbetalinger]
- tid: date range 2005-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. All 3 hierarchy levels are present: niveau=1 (5 regioner), niveau=2 (11 landsdele), niveau=3 (98 kommuner). Code 0 = "hele landet" aggregate (not in dim table). Always filter d.niveau to pick one geographic level to avoid triple-counting the same persons.
- Use ColumnValues("nuts", "titel", for_table="penindb1") to see available regions/kommuner.
- enhed is a measurement selector — 4 different statistics for the same dimension combination. Always filter to one: 123=antal med pensionstypen, 124=indbetalt beløb (1.000 kr.), 125=gennemsnit for alle personer (kr.), 126=gennemsnit for kun dem med pensionstypen (kr.). Note 125 and 126 differ: 125 divides by all persons in the group, 126 only by those with the pension type.
- pentyp=20 (alle som indbetaler) is the total; 21=arbejdsgiveradministrerede, 22=privat tegnede. Components sum to total.
- alder1=TOT is the aggregate; remaining 5 bands start at "under 25" (no data for 0-24 individually). koen=MOK is the total.
- This is the only table with regional breakdown of pension contributions (indbetalinger) — use it for geographic comparisons. For pension wealth (formue) use penfor11/penfor20.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.