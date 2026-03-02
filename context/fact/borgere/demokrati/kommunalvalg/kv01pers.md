table: fact.kv01pers
description: Valgte kandidaters personlige stemmer ved kommunalvalget i 2001 efter kandidater, stemmetype og tid
measure: indhold (unit -)
columns:
- kandidat: values [1=Abderrahman Ben Haddou (D) (Københavns Kommune), 2=Abdi Hassan Noor (A) (Tornved Kommune), 3=Abul Khaer Muhammad Ghulam Sarwar Mulla (A) (Hillerød Kommune), 4=Agnes Eva Nejstgaard (C) (Allerød Kommune), 5=Agnes Rigmor Nielsen (A) (Nordborg Kommune) ... 4643=Aase Nedergaard (A) (Herning Kommune), 4644=Aase Nissen (A) (Nørre Aaby Kommune), 4645=Aase Nyegaard (L) (Augustenborg Kommune), 4646=Aase Steffensen (O) (Lyngby-Tårbæk Kommune), 4647=Aase Wrang (V) (Sundeved Kommune)]
- stemmetype: values [PERS=Personlige stemmer, PERSP=Personlige stemmer i pct. af partiets stemmer i kommunen, PERSS=Personlige stemmer i pct. af samtlige gyldige stemmer i kommunen]
- tid: date range 2001-01-01 to 2001-01-01
notes:
- stemmetype is a measurement-selector — every kandidat row appears 3 times. Always filter: stemmetype='PERS' for absolute vote count, stemmetype='PERSP' for share of party votes in the municipality, stemmetype='PERSS' for share of all valid votes in the municipality. Never sum across stemmetype values.
- kandidat labels encode party letter and municipality (e.g. 'A.C. Hoxcer Nielsen (A) (Varde Kommune)'). Use ColumnValues("kv01pers", "kandidat", fuzzy_match_str="...") to search by name or municipality.
- Each table covers a single election year (one tid value). For cross-election comparison, query multiple kv*pers tables separately.
