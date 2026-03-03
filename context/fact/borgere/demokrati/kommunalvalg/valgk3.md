table: fact.valgk3
description: Valg til kommunalbestyrelser efter område, parti, stemmer/kandidater/køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- parti: values [A=Socialdemokratiet, B=Radikale Venstre, C=Konservative Folkeparti, DD=Nye Borgerlige, F=Socialistisk Folkeparti, GG=Veganerpartiet, I=Liberal Alliance, KK=Kristendemokraterne, O=Dansk Folkeparti (1997-), S=Slesvigsk Parti, V=Venstre, Ø=Enhedslisten - De Rød-Grønne, Å=Alternativet                                  , EJR=Ikke-reserverede bogstaver i alt]
- stemmer: values [1=Gyldige stemmer, PERSONLIGE=Personlige stemmer (i alt), 4=Opstillede mænd, 5=Opstillede kvinder, 6=Valgte mænd, 7=Valgte kvinder]
- tid: date range 2005-01-01 to 2021-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (98 kommuner). Code '0' = national aggregate not in dim. Always filter to one niveau to avoid double-counting.
- stemmer is a measurement-selector column — every omrade/parti combination appears 6 times (once per stemmer value). Must always filter to one value: 1=valid votes, PERSONLIGE=personal votes, 4=male candidates nominated, 5=female candidates nominated, 6=male elected, 7=female elected. Mixing values silently inflates all sums.
- parti includes EJR = all non-reserved party letters in aggregate. To get total votes across all parties, sum GSA through GSÅ or use valres='GS' from kvres instead.
- Sample query — elected women by party nationally in 2021:
  SELECT f.parti, f.indhold FROM fact.valgk3 f WHERE f.omrade='0' AND f.stemmer='7' AND f.tid='2021-01-01' ORDER BY f.indhold DESC;
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.