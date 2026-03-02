table: fact.hnrb
description: Syntetisk forhistorie til aktuelle nationalregnskabstals befolkningstal efter version, population og tid
measure: indhold (unit 1.000)
columns:
- version: values [1=1. Version, 2=2. Version, 3=3. Version, 4=4. Version, 5=5. Version, 6=6. Version, 7=7. Version, 8=8. Version, 9=9. Version, 10=10. Version]
- popu: values [EMPM_DC=Samlet antal beskæftigede (antal), EMPM_NC=Beskæftigede med bopæl i Danmark, POP=Gennemsnitsbefolkning]
- tid: date range 1870-01-01 to 2024-01-01

notes:
- Despite the doc listing 10 versions, in practice only version=1 is present. Do not filter on version.
- The three popu series have very different time coverage: POP (Gennemsnitsbefolkning) goes back to 1870, EMPM_DC (total employed) from 1903, EMPM_NC (employed residents) only from 1971.
- Always filter to a single popu value. Each row is an independent series; summing across popu values is meaningless.
- Paired with hnr1: use hnrb for per-capita BNP calculations (hnr1.indhold / hnrb.indhold where popu='POP').