table: fact.ais1
description: Anløbsaktivitet i danske havne (eksperimentel statistik) efter landsdel, sæsonkorrigering, enhed og tid
measure: indhold (unit -)
columns:
- landdel: values [0=Hele landet]
- saeson: values [10=Sæsonkorrigeret, 11=Ikke sæsonkorrigeret]
- tal: values [12=Skibsanløb]
- tid: date range 2017-01-01 to 2025-10-01

notes:
- saeson is a measurement selector: 10=Sæsonkorrigeret, 11=Ikke sæsonkorrigeret. Always filter to one — summing both doubles the count.
- landdel only has one value (0=Hele landet) — no regional breakdown. tal only has one value (12=Skibsanløb). These columns add no filtering flexibility; just include them in WHERE to be safe.
- This is experimental (AIS-based) statistics with the most current data (through Oct 2025, monthly). Use for recent trends. For longer historical series or harbor-level detail, use skib23 (from 1997) or skib101 (from 2007).