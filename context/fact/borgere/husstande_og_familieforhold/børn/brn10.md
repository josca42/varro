table: fact.brn10
description: Børn og unge (alle 0-29-årige) 1. januar, der har mistet forældre ved dødsfald efter område, alder, mor status, far status, status på begge forældre og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 25=25 år, 26=26 år, 27=27 år, 28=28 år, 29=29 år]
- morstat: values [MU=Mor ukendt, DIA=Død i det forgangne år, DT=Død tidligere, IRD=Ingen registrerede dødsfald]
- farstat: values [FU=Far ukendt, DIA=Død i det forgangne år, DT=Død tidligere, IRD=Ingen registrerede dødsfald]
- forst: values [IRD=Ingen registrerede dødsfald, BFDIA=En eller begge forældre død i det forgangne år , FDT=En forælder død tidligere, BFDT=Begge forældre død tidligere]
- tid: date range 2001-01-01 to 2025-01-01
dim docs: /dim/nuts.md
notes:
- omrade has four groups: '0' (national total, not in dim.nuts — use omrade='0' directly), niveau 1 (5 regioner), niveau 2 (11 landsdele), niveau 3 (99 kommuner). This is the only børn table with niveau 2 (landsdele). Filter to one niveau when joining dim.nuts.
- alder covers 0–29 (broadest of all børn tables, extending into young adults).
- morstat/farstat codes here differ from brn9: DIA=died in the past year, DT=died earlier, IRD=no registered deaths, MU/FU=unknown parent. Use DIA+DT combined to get all children with deceased parent.
- forst is a convenient combined summary of morstat+farstat: IRD=neither dead, BFDIA=one or both died this year, FDT=one died earlier, BFDT=both died earlier. For simple "orphan" queries, filter forst directly rather than combining morstat and farstat.
- morstat, farstat, and forst are partially redundant — do not sum across all three.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
