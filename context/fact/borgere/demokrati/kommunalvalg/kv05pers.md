table: fact.kv05pers
description: Valgte kandidaters personlige stemmer ved kommunalvalget i 2005 efter kandidater, stemmetype og tid
measure: indhold (unit -)
columns:
- kandidat: values [1=Abdi Hassan Noor (A) (Holbæk Kommune), 2=Adnan Yossef Moussa Jedon (A) (Brønderslev Kommune), 3=Agnes Birgitte Larsen (B) (Fredensborg Kommune), 4=Agnes Eva Nejstgaard (C) (Allerød Kommune), 5=Agnete Dreier (F) (Holbæk Kommune) ... 2518=Aage Sund Brusgaard (Z) (Morsø Kommune), 2519=Aage Toftegaard (V2) (Jammerbugt Kommune), 2520=Aase Høeg (V) (Viborg Kommune), 2521=Aase Nyegaard (L) (Sønderborg Kommune), 2522=Aase Steffensen (O) (Lyngby-Taarbæk Kommune)]
- stemmetype: values [PERS=Personlige stemmer, PERSP=Personlige stemmer i pct. af partiets stemmer i kommunen, PERSS=Personlige stemmer i pct. af samtlige gyldige stemmer i kommunen]
- tid: date range 2005-01-01 to 2005-01-01
notes:
- stemmetype is a measurement-selector — every kandidat row appears 3 times. Always filter: stemmetype='PERS' for absolute vote count, stemmetype='PERSP' for share of party votes in the municipality, stemmetype='PERSS' for share of all valid votes in the municipality. Never sum across stemmetype values.
- kandidat labels encode party letter and municipality (e.g. 'A.C. Hoxcer Nielsen (A) (Varde Kommune)'). Use ColumnValues("kv05pers", "kandidat", fuzzy_match_str="...") to search by name or municipality.
- Each table covers a single election year (one tid value). For cross-election comparison, query multiple kv*pers tables separately.
