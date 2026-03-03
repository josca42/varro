table: fact.kvres
description: Valg til kommunalbestyrelser efter område, valgresultat og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- valres: values [V=VÆLGERE, AS=AFGIVNE STEMMER, GS=GYLDIGE STEMMER I ALT, GSA=A. Socialdemokratiet, GSB=B. Radikale Venstre ... PS=PERSONLIGE STEMMER I ALT, GB=GYLDIGE BREVSTEMMER I ALT, US=UGYLDIGE STEMMER I ALT, BS=Blanke stemmer, AGS=Andre ugyldige stemmer]
- tid: date range 2005-01-01 to 2021-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (98 kommuner). Code '0' = national aggregate, not in dim. Filter WHERE d.niveau = 1 or d.niveau = 3 depending on desired granularity; mixing levels double-counts.
- valres has 22 distinct values: V (voters), AS (ballots cast), GS (total valid), PS (personal votes), GB (postal votes), US (invalid), BS (blank), AGS (other invalid), plus party-level codes GSA/GSB/GSC/… for each party. To get party vote shares, use GSA, GSB, etc. — GS is the total valid votes denominator.
- To get voter turnout from this table: indhold WHERE valres='AS' / indhold WHERE valres='V'. For the national-level rate already computed, use kvpct instead.
- Sample query — valid votes for Socialdemokratiet by region in 2021:
  SELECT d.titel, f.indhold FROM fact.kvres f JOIN dim.nuts d ON f.omrade=d.kode WHERE f.valres='GSA' AND f.tid='2021-01-01' AND d.niveau=1;
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.