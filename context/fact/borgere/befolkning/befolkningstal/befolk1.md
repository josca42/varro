table: fact.befolk1
description: Befolkningen 1. januar efter køn, alder, civilstand og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 95=95 år, 96=96 år, 97=97 år, 98=98 år, 99-=99 år og derover]
- civilstand: values [TOT=I alt, U=Ugift, G=Gift/separeret, E=Enke/enkemand, F=Fraskilt]
- tid: date range 1971-01-01 to 2025-01-01

notes:
- Annual snapshot (1 January). No geographic breakdown — national totals only.
- alder tops out at 99- (99 og derover), not individual years to 125 as in folk1a. Use folk1a for fine single-year age detail.
- Has civilstand (unlike befolk2). Filter all non-target dims: kon='TOT', alder='TOT', civilstand='TOT'.
- Long historical series back to 1971 with civilstand. For pre-1971 data use befolk2 (no civilstand, back to 1901).