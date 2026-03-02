table: fact.skov55a
description: Hugsten i skove og plantager i Danmark efter område, træsort og tid
measure: indhold (unit 1.000 m3)
columns:
- omrade: values [000=Hele landet, L4=Øerne, L3=Jylland]
- traesort: values [00010=Hugst i alt, 00020=Gavntræ i alt, 00030=Brænde i alt, 00050=Bøg i alt, BOGGAVN=Bøg - Gavntræ i alt, BOGBRAEND=Bøg - Brænde, 00060=Eg i alt, EGGAVN=Eg - Gavntræ i alt, EGBRAEND=Eg - Brænde, 00070=Andet løvtræ i alt, LOVGAVN=Andet løvtræ - Gavntræ i alt, LOVBRAEND=Andet løvtræ - Brænde, 00080=Nåletræ i alt, NALGAVN=Nåletræ - Gavntræ i alt, NALBRAEND=Nåletræ - Brænde]
- tid: date range 1950-01-01 to 1989-01-01

notes:
- omrade has only 3 values: 000=Hele landet, L3=Jylland, L4=Øerne. No dim.nuts join. This is a very coarse geographic split — national total or a simple Jylland/Øerne division only.
- traesort is hierarchical: 00010=Hugst i alt, 00020=Gavntræ i alt, 00030=Brænde i alt are top-level product aggregates. Species totals: 00050=Bøg i alt, 00060=Eg i alt, 00070=Andet løvtræ i alt, 00080=Nåletræ i alt. Species×product codes (BOGGAVN, BOGBRAEND, etc.) are the most granular. Do not sum across levels.
- Data is not annual throughout: 1950–1960 uses 5-year intervals (1950, 1955, 1960), then becomes annual from 1961 onward.
- This table covers 1950–1989 only. Use skov55 (2006–2023) for the modern series. There is no hugst data for 1990–2005 at this geographic resolution; skov6 covers 1990–2023 with the same omrade codes but adds a farm-size dimension.