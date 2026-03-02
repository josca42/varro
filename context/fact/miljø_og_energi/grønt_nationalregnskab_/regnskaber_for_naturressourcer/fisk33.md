table: fact.fisk33
description: Fritlevende fisk og skaldyr (fysisk balance) efter balanceposter, fiske- og skaldyrsarter og tid
measure: indhold (unit Ton)
columns:
- balpost: values [FS1=Beholdningen (primo), FS2=Vækst i beholdning, FS3=Anden tilgang til beholdning, FS4=Tilgang i alt, FS51=Fangst, FS6=Tab i beholdning, FS7=Reduktion i beholdning i alt, FS8=Beholdningen (ultimo)]
- fiskskal: values [TOT=ALLE FISKEARTER, TOR=Torsk, TIO=Torskefisk i øvrigt, ROD=Rødspætte, SIL=Sild, MAK=Makrel, IND=Industrifisk]
- tid: date range 2010-01-01 to 2024-01-01

notes:
- balpost codes have subtotals: FS4 (tilgang i alt) = FS2 + FS3; FS7 (reduktion i alt) = FS51 + FS6. Note FS51 here (fangst) vs FS5 in fisk11 (høst) — different code for the harvest/catch item.
- fiskskal=TOT equals sum of all listed species. Don't add TOT to individual species.
- FS1 and FS8 are stock levels (biomass); flows (FS2–FS7) and stocks have different semantics — don't sum them.
- Different species set than fisk11: wild fish (Torsk, Rødspætte, Sild, Makrel, Industrifisk) vs aquaculture (Ørred, Ål, Muslinger). No overlap.
- For aquaculture physical balance use fisk11; for aquaculture economic value use fisk22.