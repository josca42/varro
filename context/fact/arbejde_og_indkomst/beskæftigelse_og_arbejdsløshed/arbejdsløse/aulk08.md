table: fact.aulk08
description: Langtidsledige forsikringsaktive efter a-kasse, enhed, alder og tid
measure: indhold (unit -)
columns:
- akasse: values [TOT=I alt, 48=Akademikernes (fra 1. juli 2013 inkl. ingeniører), 46=Din Faglige A-kasse (fra 1. januar 2025 inkl. Fødevareforbundet (NNF), 05=Børne- og Ungdomspædagoger (BUPL-A), 06=Din Sundhedsfaglige A-kasse (DSA) ... 01=Akademikere (AAK) (- juni 2013), 16=Ingeniører (IAK) (- juni 2013), 17=IT-faget og Merkonomer (PROSA) (-juni 2010), 35=Stats- og Teleansatte (STA) (-juni 2010), 38=Træ-Industri-Byg (TIB) ( - dec. 2010)]
- maengde4: values [1=Langtidsledige (antal), 3=Langtidsledige per 1.000 forsikringsaktive]
- alder1: values [TOT=Alder i alt, 1629=16-29 år, 3049=30-49 år, 5099=50 år og derover]
- tid: date range 2009-01-01 to 2025-05-01

notes:
- maengde4 is a measurement selector: 1=antal, 3=rate per 1000. Always filter to one maengde4.
- alder1 uses compact 3-band grouping (16-29/30-49/50+) — coarser than other tables' alder column.
- Companion to aulk07 (same data but with kon instead of alder). No kon breakdown here.