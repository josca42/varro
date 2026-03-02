table: fact.kv17pers
description: Valgte kandidaters personlige stemmer ved kommunalvalget i 2017 efter kandidater, stemmetype og tid
measure: indhold (unit -)
columns:
- kandidat: values [1=A.C. Hoxcer Nielsen (A) (Varde Kommune), 2=Abdinoor Adam Hassan (A) (Odense Kommune), 3=Abdirashid Abdi (Å) (Odense Kommune), 4=Abdullahi Gutale (A) (Kalundborg Kommune), 5=Ahmed Dhaqane (A) (Rødovre Kommune) ... 2428=Øzgen Yücel (V) (Hillerød Kommune), 2429=Åge Priisholm (O) (Faaborg-Midtfyn Kommune), 2430=Aase Due (A) (Kalundborg Kommune), 2431=Åse Kubel Høeg (V) (Viborg Kommune), 2432=Aase Nyegaard (L) (Sønderborg Kommune)]
- stemmetype: values [PERS=Personlige stemmer, PERSP=Personlige stemmer i pct. af partiets stemmer i kommunen, PERSS=Personlige stemmer i pct. af samtlige gyldige stemmer i kommunen]
- tid: date range 2017-01-01 to 2017-01-01
notes:
- stemmetype is a measurement-selector — every kandidat row appears 3 times. Always filter: stemmetype='PERS' for absolute vote count, stemmetype='PERSP' for share of party votes in the municipality, stemmetype='PERSS' for share of all valid votes in the municipality. Never sum across stemmetype values.
- kandidat labels encode party letter and municipality (e.g. 'A.C. Hoxcer Nielsen (A) (Varde Kommune)'). Use ColumnValues("kv17pers", "kandidat", fuzzy_match_str="...") to search by name or municipality.
- Each table covers a single election year (one tid value). For cross-election comparison, query multiple kv*pers tables separately.
