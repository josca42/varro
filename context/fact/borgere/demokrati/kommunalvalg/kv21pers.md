table: fact.kv21pers
description: Valgte kandidaters personlige stemmer ved kommunalvalget i 2021 efter kandidater, stemmetype og tid
measure: indhold (unit -)
columns:
- kandidat: values [1=A.C. Hoxcer Nielsen (A) (Varde Kommune), 2=Abdinoor Adam Hassan (A) (Odense Kommune), 3=Ahmed Huseen Dhaqane (A) (Rødovre Kommune), 4=Akhlaq Ahmad (A) (Albertslund Kommune), 5=Aksel Rosager Johansen (Ø) (Viborg Kommune) ... 2432=Øjvind Vilsholm (Ø) (Furesø Kommune), 2433=Özcan Kizilkaya (A) (Ballerup Kommune), 2434=Øzdes Durukan (F) (Høje-Taastrup Kommune), 2435=Øzgen Yücel (V) (Hillerød Kommune), 2436=Aase Due (A) (Kalundborg Kommune)]
- stemmetype: values [PERS=Personlige stemmer, PERSP=Personlige stemmer i pct. af partiets stemmer i kommunen, PERSS=Personlige stemmer i pct. af samtlige gyldige stemmer i kommunen]
- tid: date range 2021-01-01 to 2021-01-01
notes:
- stemmetype is a measurement-selector — every kandidat row appears 3 times. Always filter: stemmetype='PERS' for absolute vote count, stemmetype='PERSP' for share of party votes in the municipality, stemmetype='PERSS' for share of all valid votes in the municipality. Never sum across stemmetype values.
- kandidat labels encode party letter and municipality (e.g. 'A.C. Hoxcer Nielsen (A) (Varde Kommune)'). Use ColumnValues("kv21pers", "kandidat", fuzzy_match_str="...") to search by name or municipality.
- Each table covers a single election year (one tid value). For cross-election comparison, query multiple kv*pers tables separately.
