table: fact.idrvan9a
description: Børns idrætsudøvelse efter alder og køn, idrætsgrene og tid
measure: indhold (unit Pct.)
columns:
- alderk: values [100=I alt, D=Drenge, P=Piger, 0709=7-9 år, 1012=10-12 år, 1315=13-15 år]
- idraet: values [10=Svømning, 100=Rulleskøjter, 110=Dans, 120=Badminton, 130=Ridning, 140=Skateboard/waveboard, 150=Basketball, 160=Kampsport, 170=Tennis, 180=Bordtennis, 190=E-sport (2020-), 20=Fodbold, 200=Atletik, 30=Gå- og vandreture, 40=Trampolin, 50=Løbehjul (2016-), 60=Løb, 70=Gymnastik, 80=Håndbold, 90=Styrketræning]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- idraet values are NOT mutually exclusive — children do multiple sports. Values sum to ~299% for alderk=100. Each row = "X% of children practise this sport".
- alderk mixes gender and age: 100=I alt, D=Drenge, P=Piger, then age bands (0709, 1012, 1315). Do not sum gender + age rows together.
- Some sports added mid-series: Løbehjul from 2016, E-sport from 2020 — will have NULL or missing in earlier years.
- Survey data — not annual; data points at 2007, 2011, 2016, 2020, 2024.