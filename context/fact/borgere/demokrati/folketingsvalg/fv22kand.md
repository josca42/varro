table: fact.fv22kand
description: Opstillede kandidaters personlige stemmer efter opstillede kandidater, valgresultat, parti, område og tid
measure: indhold (unit Antal)
columns:
- opkandidat: values [6343255=A. Anders Andreasen, 3639650=A. Anders Kronborg, 729762=A. Ane Halsboe-Jørgensen, 6469501=A. Anna Thusgård, 867438=A. Anne Paulin ... 5421364=Jayseth Lotus Arrose Simonysano, 233950=Rasmus Paludan, 6082264=Kent Nielsen, 426922=Chresten H. Ibsen, 440653=Kenneth Vestergaard]
- valres: values [1=Valgt, 0=Ikke valgt]
- parti: values [5891=A. Socialdemokratiet, 5893=B. Radikale Venstre, 5895=C. Det Konservative Folkeparti, 1675319=D. Nye Borgerlige, 5897=F. SF - Socialistisk Folkeparti, 5907=I. Liberal Alliance, 5901=K. Kristendemokraterne, 1962293=M. Moderaterne, 5899=O. Dansk Folkeparti, 1962272=Q. Frie Grønne, Danmarks Nye Venstrefløjsparti, 5903=V. Venstre, Danmarks Liberale Parti, 1968075=Æ. Danmarksdemokraterne - Inger Støjberg, 5905=Ø. Enhedslisten - De Rød-Grønne, 1487618=Å. Alternativet, 9999=Udenfor for partierne]
- omrade: values [10=Københavns Storkreds, 11=Københavns Omegns Storkreds, 12=Nordsjællands Storkreds, 13=Bornholms Storkreds, 14=Sjællands Storkreds, 15=Fyns Storkreds, 16=Sydjyllands Storkreds, 17=Østjyllands Storkreds, 18=Vestjyllands Storkreds, 19=Nordjyllands Storkreds]
- tid: date range 2022-01-01 to 2022-01-01

notes:
- 2022 election only. One row per candidate × storkreds × valres. omrade is the 10 storkredse (codes 10–19, same coding as fv22tot/fv22tota). No dim link — the 10 omrade values are exhaustive and inline.
- valres=1 means the candidate was elected; valres=0 means not elected. To get total personal votes for a candidate, SUM(indhold) across omrade — but note a candidate only stands in one storkreds, so there's at most one omrade per candidate.
- opkandidat uses numeric IDs. Filter by parti to browse candidates for a given party.
- 2022 only. For historical aggregate candidate counts (opstillede/valgte by gender), use fvkand (1990–2022).
- Map: context/geo/storkredse.parquet — merge on (omrade - 9)=dim_kode.
