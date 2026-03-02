table: fact.bane32
description: Togtrafik på en hverdag efter banestrækning, enhed og tid
measure: indhold (unit Antal)
columns:
- banes: values [1000=København H-Østerport, 1005=Østerport-Helgoland, 1010=Helgoland-Helsingør ( - 2017), 1011=Helgoland-Nivå ( 2018 - ), 1012=Nivå-Snekkersten ( 2018 - ) ... 1225=Esbjerg-Holstebro ( - 2017), 1226=Esbjerg-Varde ( 2018 - ), 1227=Varde-Skjern ( 2018 - ), 1228=Skjern-Holstebro ( 2018 - ), 1230=Struer-Thisted]
- enhed: values [2080=Persontog pr. døgn, 2090=Persontog i spidstime, 2100=Godstog pr. døgn, 2110=Godstog i spidstime]
- tid: date range 1998-01-01 to 2024-01-01

notes:
- enhed contains 4 distinct measurement types — always filter to exactly one. 2080/2090 measure person trains, 2100/2110 measure goods trains; pr. døgn is daily average, i spidstime is peak hour. These are not additive across enhed.
- Several track segments were renamed/split in 2018 — codes like "Helgoland-Helsingør (-2017)" are discontinued and replaced by "Helgoland-Nivå (2018-)" etc. For cross-year comparisons, be aware that pre/post-2018 segment codes do not align for affected stretches.
- Annual data, ~59 active segments per year. No aggregate "all segments" total — sum across banes for network totals (filter to a single enhed value first).
