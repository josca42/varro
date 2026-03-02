table: fact.fvpandel
description: Partiernes stemmeandel (Folketingsvalg) efter valgresultat, område og tid
measure: indhold (unit Pct.)
columns:
- valres: values [0=I alt, 5891=A. Socialdemokratiet, 5893=B. Radikale Venstre, 5895=C. Det Konservative Folkeparti, 1675319=D. Nye Borgerlige, 1675339=E. Klaus Riskær Pedersen, 5897=F. SF - Socialistisk Folkeparti, 5907=I. Liberal Alliance, 5901=K. Kristendemokraterne, 1962293=M. Moderaterne, 5899=O. Dansk Folkeparti, 1684467=P. Stram Kurs, 1962272=Q. Frie Grønne, Danmarks Nye Venstrefløjsparti, 5903=V. Venstre, Danmarks Liberale Parti, 1968075=Æ. Danmarksdemokraterne - Inger Støjberg, 5905=Ø. Enhedslisten - De Rød-Grønne, 1487618=Å. Alternativet, 9999=Udenfor for partierne]
- omrade: join dim.nuts on omrade=kode; levels [3]
- tid: date range 2007-01-01 to 2022-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts niveau 3 (99 kommuner) for 99 of the 100 distinct omrade values. The unmatched code is omrade=0 (HELE LANDET, national aggregate) — exclude it when joining to dim, or use it for a national total.
- valres=0 ("I alt") is a total row representing 100% of valid votes per municipality. Individual party codes are shares summing to 100%. Summing valres across all values doubles the count (you get 200%). Always filter to either valres=0 for the total, or specific party codes for party breakdowns.
- Party codes are numeric DST IDs. Use ColumnValues("fvpandel", "valres") to see the full list.
- Example: party share in København 2022: WHERE omrade=101 AND tid='2022-01-01' AND valres != '0'
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
