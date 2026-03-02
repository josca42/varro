table: fact.regk64
description: Kommunernes likvide beholdninger (1000 kr.) efter funktion og tid
measure: indhold (unit 1.000 kr.)
columns:
- funktion: values [92200=9.22.00 Likvide aktiver i alt, 92201=9.22.01 Kontante beholdninger, 92205=9.22.05 Indskud i pengeinstitutter m.v., 92207=9.22.07 Investerings- og placeringsforeninger, 92208=9.22.08 Realkreditobligationer, 92209=9.22.09 Kommunekreditobligationer, 92210=9.22.10 Statsobligationer m.v., 92211=9.22.11 Likvide aktiver udstedt i udlandet]
- tid: date range 2007-01-01 to 2025-04-01

notes:
- National aggregate only — no omrade dimension. Quarterly data (latest 2025-04-01).
- funktion=92200 (Likvide aktiver i alt) is the aggregate total = sum of 92201+92205+92207+92208+92209+92210+92211 (verified). Do not sum 92200 with its components.
- 92205 (Indskud i pengeinstitutter) can be negative when municipalities are net borrowers on their bank accounts.
- For a broader balance sheet overview including non-liquid items and liabilities, use regk63.
