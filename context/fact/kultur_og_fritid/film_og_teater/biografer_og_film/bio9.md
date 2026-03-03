table: fact.bio9
description: Biografer efter område, nøgletal, biografstørrelse og tid
measure: indhold (unit -)
columns:
- omrade: values [0=Hele landet, 84=Region Hovedstaden, 85=Region Sjælland, 83=Region Syddanmark, 82=Region Midtjylland ... 41=Byer med 10.000 - 19.999 indbyggere, 42=Byer med 20.000 - 29.999 indbyggere, 43=Byer med 30.000 -  49.999 indbyggere, 44=Byer med 50.000 - 99.999 indbyggere, 45=Byer med 100.000 - 499.999 indbyggere]
- bnogle: values [1=Biografer, 2=Sale, 5=Solgte billetter (1.000), 6=Solgte billetter, danske (1.000), 8=Billetindtægt ekskl. moms (1.000 kr.), 10=Foreviste film, 11=Årets premierefilm, 12=Foreviste danske film, 50=Årets danske premierefilm, 13=Foreviste nordiske film ekskl. danske, 14=Foreviste EU-27 film ekskl. danske, 49=Foreviste EU-28 film ekskl. danske, 15=Foreviste europæiske film ekskl. danske, 16=Foreviste Amerikanske (USA) film, 17=Foreviste øvrige film, 41=Sæder]
- biostor: values [18=Alle biografer, 19=1 sal, 20=2-3 sale, 21=4-5 sale, 22=6-7 sale, 23=8 og flere sale]
- tid: date range 2014-01-01 to 2024-01-01

notes:
- bnogle is a measurement selector with 16 different metrics. Filter to one before aggregating. Never sum across bnogle values.
- biostor has 18=Alle as total; sub-sizes (1 sal, 2-3, 4-5, 6-7, 8+) add up to it.
- omrade mixes four distinct geographic classification schemes — do NOT sum across them:
  - 0 = Hele landet (national total)
  - 81–85 = 5 regioner
  - 1–11 = 11 landsdele (sub-divisions within regions)
  - 100=Kbh+Frb, 461=Odense, 751=Aarhus, 851=Aalborg, 46=Hovedstaden (specific large cities)
  - 40–45 = city-size bands (under 10.000 to 100.000-499.999 inhabitants)
  Pick one scheme per query. ColumnValues("bio9", "omrade") shows all 28 codes with labels.
- Only table with regional breakdown of cinema activity; starts 2014.
- Map: /geo/regioner.parquet (omrade 81–85) or /geo/landsdele.parquet (omrade 1–11) — merge on omrade=dim_kode. Exclude omrade 0, 40–45, and city codes (46, 100, 461, 751, 851).