table: fact.atf1
description: Virksomheder, der søgte finansiering efter branche (DB07), finansieringsaktivitet, population og tid
measure: indhold (unit Pct.)
columns:
- branche07: values [ATF1=Alle brancher, ATF2=Industri, ATF3=Bygge og anlæg, ATF4=Handel og transport mv., ATF5=Information, kommunikation og videnservice, ATF6=Øvrige erhverv]
- finakt: values [SOGT=Søgte finansiering, SOGT_LF=Søgte lånefinansiering, SOGT_EF=Søgte egenkapitalfinansiering, SOGT_AF=Søgte andre former for finansiering]
- popu: values [S1_N=Virksomheder, der ikke er ejet af et andet firma]
- tid: date range 2007-01-01 to 2018-01-01
notes:
- Despite the column name "branche07", this is NOT standard DB07 — codes are ATF1-ATF6 (custom broad sector groups specific to this survey). Cannot join to dim.db.
- popu has only one value (S1_N = selvstændige virksomheder, ikke ejet af andet firma). No need to filter by popu — but be aware it excludes subsidiary companies.
- finakt values are NOT mutually exclusive: SOGT=searched any financing, SOGT_LF=searched loan financing, SOGT_EF=searched equity financing, SOGT_AF=searched other financing. A firm can appear in multiple categories. Don't sum across finakt.
- Data ends 2018 — outdated for current analysis. Use for historical trend analysis only.
