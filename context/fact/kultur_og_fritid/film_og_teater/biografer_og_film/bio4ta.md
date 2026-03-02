table: fact.bio4ta
description: Biograffilm/premierefilm efter biograffilm/billetter, type/målgruppe, filmens danske urpremiere, nationalitet og tid
measure: indhold (unit -)
columns:
- bio: values [5=Solgte billetter (1.000), 24=Film (antal), 25=Billetindtægt (1.000 kr.), 26=Filmleje i pct. af billetindtægten (-2013)]
- typmal: values [27=Spillefilm og dokumentarfilm, alle målgrupper, 47=Spillefilm, alle målgrupper, 28=Spillefilm. voksne, 29=Spillefilm, børn/unge/familie, 48=Dokumentarfilm, alle målgrupper, 30=Dokumentarfilm voksne , 31=Dokumentarfilm, børn/unge/familie, 32=Uoplyst]
- urprim: values [33=Alle film, 2024=2024, 2023=2023, 2022=2022, 2021=2021 ... 19711980=1971-1980, 19611970=1961-1970, 19511960=1951-1960, 1951=Før 1951, 99=Uoplyst]
- nation2: values [0=Alle lande, 5000=Danmark, 4998=Norden ekskl. Danmark, 4997=EU-27 udenfor Danmark, 4994=EU-28 udenfor Danmark ... 5314=Canada, 5390=USA, 5471=Asien, 5502=Australien/New Zealand, 5999=Øvrige og uoplyste]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- bio is a measurement selector. Filter to one: 5=Solgte billetter (1.000), 24=Film (antal), 25=Billetindtægt (1.000 kr.), 26=Filmleje i pct. Note: bio=26 only available up to 2013.
- typmal has a two-level hierarchy — don't mix levels:
  - 27 = all (spillefilm + dokumentar + uoplyst)
  - 47 = all spillefilm (= 28 voksne + 29 børn/unge/familie)
  - 48 = all dokumentarfilm (= 30 voksne + 31 børn/unge/familie)
  - 32 = Uoplyst (not included in 47 or 48, only in 27)
- urprim = year of Danish premiere. 33=Alle film for totals; decade groups available for older films (1951-1960, 1961-1970, etc.).
- nation2 has 0=Alle lande as total. Most detailed country list in this subject. ColumnValues("bio4ta", "nation2") for full list.
- Most granular film stats table: cross-tabulates type, audience, premiere year, and nationality.