table: fact.kv09pers
description: Valgte kandidaters personlige stemmer ved kommunalvalget i 2009 efter kandidater, stemmetype og tid
measure: indhold (unit -)
columns:
- kandidat: values [1=Adnan Jedon (A) (Brønderslev Kommune), 2=Agnete Damkjær (B) (Middelfart Kommune), 3=Agnete Dreier (F) (Holbæk Kommune), 4=Agnete Fog (B) (Allerød Kommune), 5=Ahmed Barimal Zemar (F) (Aabenraa Kommune) ... 2464=Øzgen Yücel (V) (Hillerød Kommune), 2465=Aage Rais-Nordentoft (A) (Aarhus Kommune), 2466=Aage Stenz (A) (Randers Kommune), 2467=Åse Kubel Høeg (V) (Viborg Kommune), 2468=Aase Nyegaard (L) (Sønderborg Kommune)]
- stemmetype: values [PERS=Personlige stemmer, PERSP=Personlige stemmer i pct. af partiets stemmer i kommunen, PERSS=Personlige stemmer i pct. af samtlige gyldige stemmer i kommunen]
- tid: date range 2009-01-01 to 2009-01-01
notes:
- stemmetype is a measurement-selector — every kandidat row appears 3 times. Always filter: stemmetype='PERS' for absolute vote count, stemmetype='PERSP' for share of party votes in the municipality, stemmetype='PERSS' for share of all valid votes in the municipality. Never sum across stemmetype values.
- kandidat labels encode party letter and municipality (e.g. 'A.C. Hoxcer Nielsen (A) (Varde Kommune)'). Use ColumnValues("kv09pers", "kandidat", fuzzy_match_str="...") to search by name or municipality.
- Each table covers a single election year (one tid value). For cross-election comparison, query multiple kv*pers tables separately.
