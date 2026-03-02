table: fact.nkhb
description: Beskæftigelse og befolkning efter socioøkonomisk status, sæsonkorrigering og tid
measure: indhold (unit Antal)
columns:
- socio: values [EMPM_DC=Samlet antal beskæftigede (antal), EMPM_NC=Beskæftigede med bopæl i Danmark, POP=Gennemsnitsbefolkning]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01
notes:
- saeson (N/Y) doubles row counts — always filter. N=ikke sæsonkorrigeret, Y=sæsonkorrigeret.
- Quarterly employment and population from 1990. Annual equivalent: nahb (from 1966).
- Same 3 socio values as nahb: EMPM_DC vs EMPM_NC differ by cross-border workers; POP=gennemsnitsbefolkning.
