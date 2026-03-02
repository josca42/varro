<fact tables>
<table>
id: uoe1
description: Udgifter til uddannelse efter uddannelsesniveau, udgiftstype, ejerforhold og tid
columns: uddniv, udtype, ejer, tid (time), indhold (unit Mio. kr.)
tid range: 2016-01-01 to 2023-01-01
</table>
<table>
id: uoe2
description: Udgifter til uddannelse efter uddannelsesniveau, finansieringskilde, modsektor og tid
columns: uddniv, finanskilde, modsektor, tid (time), indhold (unit Mio. kr.)
tid range: 2016-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- uoe1 and uoe2 are two perspectives on the same underlying Danish education expenditure data (both sum to the same total). Read the question carefully to pick the right one:
  - uoe1 = expenditure by type and institutional owner: use when asked how money is spent (lønudgifter, investeringer, SU, FoU) or which type of institution (offentlig/privat) spends it.
  - uoe2 = financing flows by source and receiving sector: use when asked who funds education (staten, kommuner, husholdninger, virksomheder, internationale) or which sector receives the funding.
- Both tables cover 2016–2023 (annual) and break down by uddannelsesniveau (grundskoler, ungdomsuddannelser, korte/mellemlange+lange videregående).
- Both tables have sparse dimension matrices — not all combinations of category codes exist. Check the fact doc notes before constructing GROUP BY queries.
- All dimension columns in both tables include aggregate total rows (TOT1, TOT, TOT4 in uoe1; TOT1, TOT3, TOT2 in uoe2). Always filter explicitly to avoid summing totals together with leaf values.