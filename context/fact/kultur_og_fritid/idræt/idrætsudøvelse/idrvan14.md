table: fact.idrvan14
description: Børns idrætsudøvelse efter alder og køn, forældres baggrund og tid
measure: indhold (unit Pct.)
columns:
- alderk: values [100=I alt, D=Drenge, P=Piger, 0709=7-9 år, 1012=10-12 år, 1315=13-15 år]
- forback: values [23=Begge forældre født i Danmark (2016-), 24=Forældre er født i Danmark eller Europa (2016-), 25=Forældre er dansk/europæisk og ikke-europæisk oprindelse (2016-), 26=Begge forældre er født uden for Europa (2016-), 27=Begge forældre arbejder (2016-), 28=En forældre arbejder (2016), 29=Ingen forældre arbejder (2016), 32=Mindst en forældre arbejder ikke (2020-), 30=Mor, far og/eller søskende dyrker sport eller motion (-2020), 33=Begge forældre dyrker sport/motion (2024-), 34=Én forældre dyrker sport/motion (2024-), 31=Ingen andre i familien dyrker sport eller motion]
- tid: date range 2011-01-01 to 2024-01-01

notes:
- forback mixes multiple distinct background dimensions (parental origin, parental employment, family sport habits) into one column. Categories within each sub-question are mutually exclusive, but the column as a whole is NOT a single dimension — do not sum across all forback values.
- Many forback codes have changed or been replaced across survey rounds. Check year annotations: codes 23–26 (forældrenes fødested) available from 2016, code 28 only in 2016 (replaced by 32 in 2020), codes 33–34 only from 2024. Filter tid carefully when comparing codes across years.
- alderk: 100=I alt, D=Drenge, P=Piger, then age bands. Don't sum gender + age rows.
- Survey data — not annual; data points at 2011, 2016, 2020, 2024.