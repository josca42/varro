table: fact.kubs01
description: Kulturministeriets udbetalinger efter kulturemne og tid
measure: indhold (unit Mio. kr.)
columns:
- kulturemne: values [0=Alle kulturemner, 8=IDRÆT OG FRITID, 9=Fornøjelses- og temaparker, 10=Idræt, 11=Spil og lotteri ... 31=Statslig administration, 32=Udstyr, 33=Anden/tværgående kultur, 34=Folkeoplysning og folkehøjskoler, 99=Uoplyst]
- tid: date range 2010-01-01 to 2023-01-01

notes:
- Simple two-column table (kulturemne + tid). `kulturemne=0` is "Alle kulturemner" (national total). Filter to a specific code for a single topic.
- `kulturemne` uses numeric codes where the broad category codes are shown in uppercase (8=IDRÆT OG FRITID, 12=KULTURARV etc.) and sub-category codes are lowercase sub-items underneath them. Summing all kulturemne values would double-count since broad categories include their sub-items.
- Longest kubs series from 2010; use this table for trend analysis of total ministry disbursements by cultural topic.