table: fact.idrvan1a
description: Voksnes idrætsudøvelse efter køn og alder, idrætsgrene og tid
measure: indhold (unit Pct.)
columns:
- konalder: values [100=I alt, 1=Mand, 2=Kvinde, 1619=16-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover]
- idraet: values [10=Vandreture, 100=Tennis, 110=Golf, 120=Ridning, 130=Svømning, 140=Landevejscykling, 150=Atletik, 20=Løb, 30=Styrketræning, 40=Spinning, 50=Gymnastik, 60=Fodbold, 70=Badminton, 80=Håndbold, 90=Basketball]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- idraet values are NOT mutually exclusive — one person can practise multiple sports. Values sum to ~192% across all sports for konalder=100. Never sum across idraet categories; read each row as "X% of adults practise this sport".
- konalder mixes gender and age into one column: 100=I alt, 1=Mand, 2=Kvinde, then age bands (1619, 2029, …, 7099). Do not sum gender + age values together — they overlap (a 20-year-old man is in both konalder=1 and konalder=2029).
- Survey data — data points every 3-4 years (2007, 2011, 2016, 2020, 2024). tid is not annual.