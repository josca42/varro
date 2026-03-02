table: fact.fisk11
description: Fisk og skaldyr i dam- og havbrug (fysisk balance) efter balanceposter, fiske- og skaldyrsarter og tid
measure: indhold (unit Ton)
columns:
- balpost: values [FS1=Beholdningen (primo), FS2=Vækst i beholdning, FS3=Anden tilgang til beholdning, FS4=Tilgang i alt, FS5=Høst, FS6=Tab i beholdning, FS7=Reduktion i beholdning i alt, FS8=Beholdningen (ultimo)]
- fiskskal: values [TOT=ALLE FISKEARTER, OLD=Ørred og Laks, dambrug, AFS=Andre fisk og skaldyr, AAL=Ål, OLH=Ørred og Laks, havbrug, MUS=Muslinger]
- tid: date range 2010-01-01 to 2024-01-01

notes:
- balpost codes have subtotals: FS4 (tilgang i alt) = FS2 + FS3; FS7 (reduktion i alt) = FS5 + FS6. Do not mix parent and child codes in aggregations.
- fiskskal=TOT equals the sum of all species (OLD+AFS+AAL+OLH+MUS). Don't add TOT to individual species — double counting.
- FS1 (primo) and FS8 (ultimo) are stock levels; FS2–FS7 are flows. Stocks and flows have different semantics — don't sum them.
- This table is aquaculture only (dam- og havbrug). For wild-caught fish use fisk33; for monetary value of aquaculture use fisk22.