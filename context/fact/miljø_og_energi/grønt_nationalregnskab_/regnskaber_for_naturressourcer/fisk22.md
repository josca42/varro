table: fact.fisk22
description: Fisk og skaldyr i dam- og havbrug (økonomisk balance) efter balanceposter, fiske- og skaldyrsarter og tid
measure: indhold (unit 1.000 kr.)
columns:
- balpost: values [FS1=Beholdningen (primo), FS2=Vækst i beholdning, FS3=Anden tilgang til beholdning, FS4=Tilgang i alt, FS5=Høst, FS6=Tab i beholdning, FS7=Reduktion i beholdning i alt, FS9=Omvurdering, FS8=Beholdningen (ultimo)]
- fiskskal: values [TOT=ALLE FISKEARTER, OLD=Ørred og Laks, dambrug, AFS=Andre fisk og skaldyr, AAL=Ål, OLH=Ørred og Laks, havbrug, MUS=Muslinger]
- tid: date range 2010-01-01 to 2024-01-01

notes:
- Economic counterpart to fisk11 (same species, same time period) but in 1.000 kr. instead of tons.
- balpost hierarchy same as fisk11: FS4 = FS2+FS3, FS7 = FS5+FS6. Extra code FS9 (omvurdering) not present in fisk11.
- fiskskal=TOT equals sum of all species. Don't add TOT to individual species.
- FS1 and FS8 are monetary stock values (carrying value of live inventory); flows have different semantics — don't mix.
- For physical quantities (tons) use fisk11. For wild fish (fritlevende) there is no economic balance table — only fisk33 physical.