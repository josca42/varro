table: fact.nahb
description: Beskæftigelse og befolkning efter socioøkonomisk status og tid
measure: indhold (unit Antal)
columns:
- socio: values [EMPM_DC=Samlet antal beskæftigede (antal), EMPM_NC=Beskæftigede med bopæl i Danmark, POP=Gennemsnitsbefolkning]
- tid: date range 1966-01-01 to 2024-01-01
notes:
- Simple table — only 3 socio values and no measurement selectors. Each socio×tid combination has exactly one row.
- socio values: EMPM_DC=samlet antal beskæftigede (inkl. grænsearbejdere), EMPM_NC=beskæftigede med bopæl i Danmark, POP=gennemsnitsbefolkning. These measure different things — EMPM_DC and EMPM_NC differ by cross-border workers.
- Annual from 1966. Quarterly with saeson: nkhb.
