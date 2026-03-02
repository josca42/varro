<fact tables>
<table>
id: recidiv1
description: Personer efter køn, alder, varighed til tilbagefald, oprindelig straf, oprindelig lovovertrædelse og tid
columns: kon, alder1, vartilbage, strafart, over, tid (time), indhold (unit Antal)
tid range: 2007 to 2024
</table>
<table>
id: recidiv2
description: Personer efter køn, alder, oprindelig lovovertrædelse, lovovertrædelse ved første tilbagefald og tid
columns: kon, alder1, over, over1, tid (time), indhold (unit Antal)
tid range: 2007 to 2024
</table>
<table>
id: recidiv3
description: Personer efter køn, alder, oprindelig straf, oprindelig lovovertrædelse, lovovertrædelse ved første tilbagefald, straf ved første tilbagefald og tid
columns: kon, alder1, strafart, over, over1, strafart1, tid (time), indhold (unit Antal)
tid range: 2007 to 2024
</table>
<table>
id: recidiv4
description: Personer efter køn, alder, oprindelig straf, oprindelig lovovertrædelse, lovovertrædelse (ved strengeste straf i opfølgningsperioden), straf (ved strengeste straf i opfølgningsperioden) og tid
columns: kon, alder1, strafart, over, over2, strafart2, tid (time), indhold (unit Antal)
tid range: 2007 to 2024
</table>
<table>
id: recidiv5
description: Personer efter køn, alder, oprindelig straf, oprindelig lovovertrædelse, recidiv hændelser og tid
columns: kon, alder1, strafart, over, rechen, tid (time), indhold (unit Antal)
tid range: 2007 to 2024
</table>
<table>
id: recidiv6
description: Personer efter køn, alder, uddannelse, varighed til tilbagefald og tid
columns: kon, alder1, uddannelse, vartilbage, tid (time), indhold (unit Antal)
tid range: 2008 to 2024
</table>
<table>
id: recidiv7
description: Personer efter køn, alder, uddannelse, lovovertrædelse (ved strengeste straf i opfølgningsperioden) og tid
columns: kon, alder1, uddannelse, over2, tid (time), indhold (unit Antal)
tid range: 2008 to 2024
</table>
<table>
id: recidiv8
description: Personer efter køn, alder, uddannelse, straf (ved strengeste straf i opfølgningsperioden) og tid
columns: kon, alder1, uddannelse, strafart2, tid (time), indhold (unit Antal)
tid range: 2008 to 2024
</table>
<table>
id: recidiv9
description: Personer efter køn, alder, uddannelse, recidiv hændelser og tid
columns: kon, alder1, uddannelse, rechen, tid (time), indhold (unit Antal)
tid range: 2008 to 2024
</table>
<table>
id: recidv10
description: Personer efter køn, alder, tidligere domme, recidiv hændelser, varighed til tilbagefald og tid
columns: konams, alder, tidldom, rechen, vartilbage, tid (time), indhold (unit Antal)
tid range: 2009 to 2024
</table>
<table>
id: recidv11
description: Personer efter køn, alder, tidligere domme, recidiv hændelser, straf ved første tilbagefald og tid
columns: konams, alder, tidldom, rechen, strafart1, tid (time), indhold (unit Antal)
tid range: 2009 to 2024
</table>
<table>
id: recidv12
description: Personer efter køn, alder, tidligere domme, recidiv hændelser, straf (ved strengeste straf i opfølgningsperioden) og tid
columns: konams, alder, tidldom, rechen, strafart2, tid (time), indhold (unit Antal)
tid range: 2009 to 2024
</table>
</fact tables>
notes:
- All tables use rolling 3-year follow-up cohorts as tid (e.g. [2007,2010) = persons released/sentenced in 2007, tracked for 2 years). Never sum across overlapping tid values. Use a single tid period.
- recidiv1-9 use kon/alder1; recidv10-12 use konams/alder (varchar, no 15-19 age group). Different column names for the same concepts — don't mix.
- strafart (original punishment, codes 0-8) appears in recidiv1/3/4/5. strafart1 (first recidivism punishment, codes 0/100-105) in recidiv3/recidv11. strafart2 (strictest in follow-up, codes 0/100-105) in recidiv4/7/8/recidv12. Different coding schemes — 0 means I alt in all, but the sub-codes differ.
- over (original offense, 42 codes with hierarchy) appears in recidiv1-5. Never SUM across all over codes — pick aggregate (1=Straffelov i alt, 30=Færdselslov i alt, 35=Særlov i alt) or leaf level.
- over1/over2 (recidivism offense, 7 codes: 0,2,5,11,24,30,35) are aggregated views. ColumnValues for these shows duplicate ids — metadata quirk; data only has one row per code.
- vartilbage and tidldom: code 0 is always I alt, not "Ingen tilbagefald"/"Ingen tidligere domme". ColumnValues shows id=0 twice for these — ignore the duplicate.
- For time-to-first-recidivism breakdown: recidiv1 (by original straf+offense), recidiv6 (by education), recidv10 (by prior convictions).
- For recidivism-offense analysis: recidiv2 (original→first recidivism offense), recidiv4/recidiv7 (by strictest sentence in follow-up).
- For recidivism event counts (1/2/3/4-9/10+): recidiv5 (by original straf+offense), recidiv9 (by education), recidv10/11/12 (by prior convictions).
- recidiv6-9 (education breakdown) start from 2008; recidv10-12 (prior convictions) start from 2009.
