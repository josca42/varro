table: fact.foukul02
description: Årsværk og Personale i den offentlige sektor til Forskning og Udvikling i Kulturen efter fagområde, årsværk og personale, køn og tid
measure: indhold (unit Antal)
columns:
- fagomr: values [1000=Kultur i alt, 1010=byplanlægning, fysisk planlægning, 1020=medier og kommunikation, 1030=historie, 1040=arkæologi, 1050=sprogvidensk., filologi, 1060=litteraturvidenskab, 1070=filosofi, idehistorie, 1080=teologi, 1090=musik, teatervidenskab, 1100=kunst- og arkitekturvidenskab, 1110=film- og medievidenskab, 1120=øvrig humanistisk videnskab]
- aarvaerk: values [40=Arsværk til FoU, 50=Personale til FoU]
- koen: values [0=I alt, 1=Mænd, 2=Kvinder]
- tid: date range 2007-01-01 to 2023-01-01

notes:
- aarvaerk is a measurement-type selector, not a category: 40=Årsværk til FoU (FTE), 50=Personale til FoU (headcount). These are two independent measures. Always filter to one — SUM across both silently doubles the count.
- koen=0 (I alt) is the total of koen=1 (Mænd) + koen=2 (Kvinder). Filter to koen=0 for totals, or filter to koen=1/2 for gender breakdown — never sum all three.
- fagomr=1000 (Kultur i alt) is the aggregate of all sub-fields (1010–1120). Filter to fagomr=1000 for an overall total, or exclude it (WHERE fagomr != 1000) when breaking down by field to avoid double-counting.
- Example — total FTE in culture research 2023: SELECT indhold FROM fact.foukul02 WHERE tid='2023-01-01' AND aarvaerk=40 AND koen=0 AND fagomr=1000