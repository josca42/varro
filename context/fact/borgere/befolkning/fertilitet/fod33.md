table: fact.fod33
description: Fertilitetskvotienter efter alder og tid
measure: indhold (unit Pr. 1.000 kvinder)
columns:
- alder: values [TOT1=Samlet fertilitet, 15=15 år, 16=16 år, 17=17 år, 18=18 år ... 47=47 år, 48=48 år, 49=49 år, BRUTTO=Bruttoreproduktionstal, NETTO=Nettoreproduktionstal]
- tid: date range 1973-01-01 to 2024-01-01

notes:
- The alder column mixes three distinct measure types — never aggregate across all alder values:
  - Individual ages 15–49: age-specific fertility rates (pr. 1.000 kvinder in that age group)
  - TOT1: total fertility rate (sum of all age-specific rates = "samlet fertilitet")
  - BRUTTO: gross reproduction rate (expected daughters per woman, ignoring mortality)
  - NETTO: net reproduction rate (BRUTTO adjusted for mortality before reproductive age)
- For total fertility rate, use WHERE alder='TOT1'. For age profile, use individual ages 15–49. For reproduction rates, use BRUTTO or NETTO explicitly.
- Longest series in the subject (back to 1973) but national only — no regional breakdown.