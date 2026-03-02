table: fact.kv2bib3
description: Barrierer for brug af biblioteket efter årsag, køn og tid
measure: indhold (unit Pct.)
columns:
- aarsag: values [40000=Det interesserer mig ikke, 40010=Jeg foretrækker at købe bøgerne, 40020=Jeg har ikke tid, 40030=Jeg har ikke nogen at følges med, 40040=Det er for svært at komme dertil, 40050=Det er ikke børnevenligt, 40060=Jeg er mere et hjemmemenneske, 40070=Det er ikke handicapvenligt, 40080=Jeg foretrækker at læse eller lytte til digitale bøger, 41800=Andre årsager]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- Survey data (% of non-library-users citing each barrier). Only 2024, no geographic breakdown, no age breakdown.
- aarsag values are NOT mutually exclusive — each percentage is an independent rate among non-users. Never sum across aarsag.
- kon: 10=Køn i alt, 1=Mænd, 2=Kvinder (numeric codes).
- To get a simple ranking of barriers: SELECT aarsag, indhold FROM fact.kv2bib3 WHERE kon=10 AND tid='2024-01-01' ORDER BY indhold DESC.
