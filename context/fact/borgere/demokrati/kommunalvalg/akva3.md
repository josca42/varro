table: fact.akva3
description: Valg til regionsråd efter område, parti, stemmer/kandidater/køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- parti: values [A=Socialdemokratiet, B=Radikale Venstre, C=Konservative Folkeparti, DD=Nye Borgerlige, F=Socialistisk Folkeparti, GG=Veganerpartiet, I=Liberal Alliance, KK=Kristendemokraterne, O=Dansk Folkeparti (1997-), S=Slesvigsk Parti, V=Venstre, Ø=Enhedslisten - De Rød-Grønne, Å=Alternativet                                  , EJR=Ikke-reserverede bogstaver i alt]
- stemmer: values [1=Gyldige stemmer, PERSONLIGE=Personlige stemmer (i alt), 4=Opstillede mænd, 5=Opstillede kvinder, 6=Valgte mænd, 7=Valgte kvinder]
- tid: date range 2005-01-01 to 2021-01-01
dim docs: /dim/nuts.md

notes:
- Same structure as valgk3 but for regionsråd elections. omrade only at niveau 1 (5 regioner) + '0' national aggregate — no kommune-level breakdown.
- stemmer is a measurement-selector: always filter to one value (1=valid votes, PERSONLIGE=personal votes, 4/5=candidates by gender, 6/7=elected by gender). Every omrade/parti row repeats 6 times, so forgetting to filter inflates all sums 6x.
- Use ColumnValues("nuts", "titel", for_table="akva3") to confirm the 5 regions available.
- Map: context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.