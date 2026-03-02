table: fact.dnbskk
description: Kontantautomater og kortterminaler efter enheder og tid
measure: indhold (unit Antal)
columns:
- enhed1: values [ATM=1 Kontantautomater, i alt, ATMINDSKUD=1.1 Heraf kontantautomater med mulighed for indskud, ATMOVERF=1.2 Heraf kontantautomater med mulighed for kontooverførsel, ATMALONE=1.3 Heraf kontantautomater uden tilknytning til en bankfilial, POS=2 Kortterminaler, i alt, POSNFC=2.1 Heraf kortterminaler til kontaktløse betalinger, POSHAANDH=2.2 Heraf håndholdte kortterminaler]
- tid: date range 2016-01-01 to 2025-04-01

notes:
- enhed1 is hierarchical with two parent groups: ATM (kontantautomater i alt) and POS (kortterminaler i alt). Their children: ATM→ATMINDSKUD, ATMOVERF, ATMALONE; POS→POSNFC, POSHAANDH. Never sum a parent with its children — e.g. ATM+ATMINDSKUD double-counts. Pick either the parent (for totals) or specific subtypes.
- No data/unit selector column — all indhold values are raw counts (Antal, i.e. physical number of machines). Simple to query; just pick the enhed1 value you want.
- Example: total ATMs and card terminals over time: SELECT tid, enhed1, indhold FROM fact.dnbskk WHERE enhed1 IN ('ATM','POS') ORDER BY tid;