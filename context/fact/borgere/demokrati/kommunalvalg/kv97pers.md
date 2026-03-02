table: fact.kv97pers
description: Valgte kandidaters personlige stemmer ved kommunalvalget i 1997 efter kandidater, stemmetype og tid
measure: indhold (unit -)
columns:
- kandidat: values [1=Abderrahman Ben Haddou (D) (Københavns Kommune), 2=Agnes Eva Nejstgaard (C) (Allerød Kommune), 3=Agnes Munkhøj Nielsen (F) (Ålborg Kommune), 4=Agnes Østergård Clausen (V) (Helle Kommune), 5=Agnethe Jepsen (Z) (Hirtshals Kommune) ... 4681=Aase Noltensmejer (A) (Fuglebjerg Kommune), 4682=Aase Nyegaard (L) (Augustenborg Kommune), 4683=Aase Pedersen (V) (Hedensted Kommune), 4684=Åse Stampe Jensen (C) (Hanstholm Kommune), 4685=Aase Steffensen (O) (Lyngby-Tårbæk Kommune)]
- stemmetype: values [PERS=Personlige stemmer, PERSP=Personlige stemmer i pct. af partiets stemmer i kommunen, PERSS=Personlige stemmer i pct. af samtlige gyldige stemmer i kommunen]
- tid: date range 1997-01-01 to 1997-01-01
notes:
- stemmetype is a measurement-selector — every kandidat row appears 3 times. Always filter: stemmetype='PERS' for absolute vote count, stemmetype='PERSP' for share of party votes in the municipality, stemmetype='PERSS' for share of all valid votes in the municipality. Never sum across stemmetype values.
- kandidat labels encode party letter and municipality (e.g. 'A.C. Hoxcer Nielsen (A) (Varde Kommune)'). Use ColumnValues("kv97pers", "kandidat", fuzzy_match_str="...") to search by name or municipality.
- Each table covers a single election year (one tid value). For cross-election comparison, query multiple kv*pers tables separately.
