table: fact.bil14
description: Bestanden af busser pr. 1. januar efter anvendelse, passagerantal, enhed og tid
measure: indhold (unit -)
columns:
- anvend: values [1000=I alt, 20250=Rutekørsel, 20255=Turistkørsel]
- sidde: values [1=I alt, 8=Under 10, 9=10, 11=11, 12=12, 13=13-19, 14=20-31, 15=32-49, 16=50-59, 17=60-69, 18=70-79, 19=Over 79, 2005=Uoplyst]
- enhed: values [9020=Antal, 9025=Passagerkapacitet]
- tid: date range 1993-01-01 to 2025-01-01

notes:
- enhed is a unit selector: 9020=Antal (number of buses), 9025=Passagerkapacitet (total seat capacity). Always filter to one enhed — they measure different things and must never be summed together.
- sidde is passenger seat-count bands. sidde=1 is the total. For total bus count or capacity, use WHERE sidde='1' AND anvend=1000 AND enhed=9020 (or 9025).
- anvend=1000 is I alt; 20250=Rutekørsel, 20255=Turistkørsel.