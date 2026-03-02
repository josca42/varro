table: fact.aul02
description: Fuldtidsledige/ledighedsberørte efter type, ydelsestype, alder, køn, ledighedsgrad og tid
measure: indhold (unit Antal)
columns:
- type: values [FTM=Fuldtidsledige, DEL=Ledighedsberørte]
- ydelsestype: values [TOT=Bruttoledige, LDP=Nettoledige dagpengemodtagere, LKT=Nettoledige kontanthjælpsmodtagere, ADP=Aktiverede dagpengeberettigede, AKT=Aktiverede kontanthjælpsmodtagere (arbejdsmarkedsparate)]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- ledgrad: values [TOT=I alt, 0.001-0.100=0.001-0.100, 0.101-0.200=0.101-0.200, 0.201-0.300=0.201-0.300, 0.301-0.400=0.301-0.400, 0.401-0.500=0.401-0.500, 0.501-0.600=0.501-0.600, 0.601-0.700=0.601-0.700, 0.701-0.800=0.701-0.800, 0.801-0.900=0.801-0.900, 0.901-1.000=0.901-1.000]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- Superseded by aulk02 (same structure, updated to 2025).
- type: FTM=Fuldtidsledige vs DEL=Ledighedsberørte — two distinct concepts. Always filter to one.
- ledgrad buckets are mutually exclusive and sum to TOT. ledgrad only meaningful for DEL.
- ydelsestype: TOT is the aggregate. Filter to one.