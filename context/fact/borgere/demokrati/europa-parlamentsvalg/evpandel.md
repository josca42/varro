table: fact.evpandel
description: Partiernes stemmeandel (Europa-Parlamentsvalg) efter valgresultat, område og tid
measure: indhold (unit Pct.)
columns:
- valres: values [0=I alt, 5891=A. Socialdemokratiet, 5893=B. Radikale Venstre, 5895=C. Det Konservative Folkeparti, 5897=F. SF - Socialistisk Folkeparti, 5907=I. Liberal Alliance, 431970=J. Junibevægelsen, 1962293=M. Moderaterne, 431971=N. Folkebevægelsen mod EU, 5899=O. Dansk Folkeparti, 5903=V. Venstre, Danmarks Liberale Parti, 1968075=Æ. Danmarksdemokraterne - Inger Støjberg, 5905=Ø. Enhedslisten - De Rød/Grønne, 1487618=Å. Alternativet]
- omrade: join dim.nuts on omrade=kode; levels [3]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 3 only (99 kommuner), EXCEPT omrade='0' = hele landet (I alt), which is not in dim.nuts. To include the national total, use a LEFT JOIN or query WHERE omrade='0' separately.
- valres='0' (I alt) is the national total (100%). Do not sum party percentages — they already sum to ~100. Pick one valres value per query.
- Values are vote-share percentages (Pct.). Summing indhold across parties or across omrade is meaningless.
- For national-level party vote shares use WHERE omrade='0'. For regional breakdown join dim.nuts and filter WHERE omrade != '0'.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade='0' (national total).