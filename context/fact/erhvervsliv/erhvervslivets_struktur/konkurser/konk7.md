table: fact.konk7
description: Erklærede konkurser efter beskæftigede og tid
measure: indhold (unit Antal)
columns:
- besk: values [000=Konkurser i alt, BES1=Ingen beskæftigelse indberettet, BES2=0-9 ansatte, BES3=10-19 ansatte, BES4=20+ ansatte]
- tid: date range 2009-01-01 to 2025-09-01

notes:
- besk='000' is the national total. BES1–BES4 sum to it, so exclude '000' when breaking down by size.
- BES1 (ingen beskæftigelse indberettet) overlaps conceptually with nulvirksomheder in konk8/virktyp1. BES2–BES4 (0-9, 10-19, 20+ ansatte) reflect actual employment size bands at time of bankruptcy.