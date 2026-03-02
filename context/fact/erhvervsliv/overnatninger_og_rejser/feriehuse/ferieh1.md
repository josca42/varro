table: fact.ferieh1
description: Udlejning af feriehuse på månedsbasis efter gæstens nationalitet, enhed, periode og tid
measure: indhold (unit Antal)
columns:
- nation1: values [TOT=I alt, DAN=Danmark, HOL=Nederlandene, SVE=Sverige, NOR=Norge, TYS=Tyskland, ANDRE=Uoplyst land]
- tal: values [1270=Overnatninger, 1280=Udlejede hus-uger, 1290=Kontrakter, 1300=Disponible husuger]
- periode: values [1=Hele året, 2=År til dato, 1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December]
- tid: date range 2004-01-01 to 2025-01-01

notes:
- tal is a measurement selector: 1270=Overnatninger, 1280=Udlejede hus-uger, 1290=Kontrakter, 1300=Disponible husuger. Always filter to one tal value — all four measures are repeated for every (nation1, periode, tid) combination.
- periode has overloaded codes: 1 = both "Hele året" (full-year total) AND "Januar" (monthly value); 2 = both "År til dato" AND "Februar". Each (nation1, tal, tid) combination has 14 rows, not 12. For unambiguous monthly data use periode >= 3 (March–December). For the annual total, filter periode=1 but expect two rows per combination — the annual total (Hele året) is the larger value (~23M overnights vs ~500K for January).
- tid is always Jan 1 of the reporting year (2004-2025). All monthly data for a given year lives under the same tid.
- nation1=TOT is the national total; do not sum across all nation1 values as that would double-count.