table: fact.vej22
description: Motorkøretøjer pr. døgn efter vejstrækning og tid
measure: indhold (unit Antal)
columns:
- vejstr: values [1000=E45 Sydjyske Motorvej, ved Frøslev (Landegrænsen), 1005=E45 Sønderjyske Motorvej, nordvest for Skovby, 1010=E45 Sydjyske Motorvej, vest for Haderslev, 1020=E20 E45 Sydjyske Motorvej, nord for Kolding, 1025=E20 Esbjergmotorvejen, øst for Lunderskov ... 2490=211 Frederikssundsvej, ved Ballerup (1988 - 2016), 2500=211 Frederikssundsvej, sydøst for Frederikssund, 2510=E47 E55 Kongevejen i Helsingør (1988 - 2022), 2515=E47 E55 Kongevejen, ved Helsingør, 2520=E47 E55 Flynderborgvej i Helsingør (1988 - 2016)]
- tid: date range 1988-01-01 to 2024-01-01

notes:
- vejstr has 197 road segments with inline codes — long descriptive names like "E45 Sydjyske Motorvej, ved Frøslev". Use ColumnValues("vej22", "vejstr") to browse. Note that some codes include year ranges in the name (e.g. "1988 - 2016"), indicating the segment was renamed or discontinued.
- No overcounting risk: only two columns (vejstr, tid). Each row is a distinct road segment × year combination. Annual data from 1988.