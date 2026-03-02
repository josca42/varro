table: fact.aulk07
description: Langtidsledige forsikringsaktive efter a-kasse, enhed, køn og tid
measure: indhold (unit -)
columns:
- akasse: values [TOT=I alt, 48=Akademikernes (fra 1. juli 2013 inkl. ingeniører), 46=Din Faglige A-kasse (fra 1. januar 2025 inkl. Fødevareforbundet (NNF), 05=Børne- og Ungdomspædagoger (BUPL-A), 06=Din Sundhedsfaglige A-kasse (DSA) ... 01=Akademikere (AAK) (- juni 2013), 16=Ingeniører (IAK) (- juni 2013), 17=IT-faget og Merkonomer (PROSA) (-juni 2010), 35=Stats- og Teleansatte (STA) (-juni 2010), 38=Træ-Industri-Byg (TIB) ( - dec. 2010)]
- maengde4: values [1=Langtidsledige (antal), 3=Langtidsledige per 1.000 forsikringsaktive]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2009-01-01 to 2025-05-01

notes:
- maengde4 is a measurement selector: 1=antal, 3=rate per 1000 forsikringsaktive. Every combination appears twice. Always filter to one maengde4.
- Covers langtidsledige forsikringsaktive (long-term insured unemployed) by a-kasse. Companion to aulk08 (same data but by alder instead of kon).
- Several historic a-kasser are included with end dates (merged/dissolved). Their codes are valid for their active period only.