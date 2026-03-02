table: fact.fvkand
description: Opstillede og valgte kandidater efter kandidater, parti og tid
measure: indhold (unit Antal)
columns:
- kandidat: values [MOPST=Opstillede mænd, KOPST=Opstillede kvinder, MVALGT=Valgte mænd, KVALGT=Valgte kvinder]
- parti: values [5891=A. Socialdemokratiet, 5893=B. Radikale Venstre, 5895=C. Det Konservative Folkeparti, 5896=D. Centrum-Demokraterne, 1675319=D. Nye Borgerlige ... 5910=Z. Fremskridtspartiet, 1968075=Æ. Danmarksdemokraterne - Inger Støjberg, 5905=Ø. Enhedslisten - De Rød-Grønne, 1487618=Å. Alternativet, 9999=Udenfor for partierne]
- tid: date range 1990-01-01 to 2022-01-01

notes:
- kandidat has four mutually exclusive values: MOPST/KOPST (opstillede mænd/kvinder) and MVALGT/KVALGT (valgte mænd/kvinder). Summing MOPST+KOPST gives total opstillede; MVALGT+KVALGT gives total valgte. Never sum all four — that doubles the count.
- parti uses numeric DST IDs, not party letters. 9999=candidates running outside parties. Use ColumnValues("fvkand", "parti") to browse the full list.
- National-level only (no omrade). For gender/age breakdown use ligedb1; for personal vote counts use fv22kand (2022 only).
