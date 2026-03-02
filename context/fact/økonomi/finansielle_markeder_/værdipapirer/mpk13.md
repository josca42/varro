table: fact.mpk13
description: Aktieindeks ultimo efter type og tid
measure: indhold (unit Indeks)
columns:
- type: values [10=Aktier i alt (OMXC ultimo december 1995 = 100), 57=OMXC 20 Cap (28. november 2011 = 400), 60=OMXC 20 (3. juli 1989 = 100), 75=MidCap+ (30. december 2002 = 100), 80=SmallCap+  (30. december 2002 = 100), 85=OMXC 25 (19. dec 2016 = 1000), 13=Energi, 15=Materialer, 20=Industri, 25=Forbrugsgoder, 30=Forbrugertjenester, 35=Sundhedspleje, 40=Finans, 45=IT, 50=Telekommunikation, 55=Forsyning, 93=Essentielle forbrugsvarer, 90=Ikke-essentielle forbrugsvarer, 96=Ejendomme]
- tid: date range 1996-01-01 to 2025-09-01

notes:
- indhold is an index value (Indeks), not Mio. kr. — never sum across type codes. Each type has its own base date and base value (e.g. type=60 OMXC20 base 100 at 3 July 1989, type=85 OMXC25 base 1000 at 19 Dec 2016).
- type codes fall into two groups: broad market indices (10, 57, 60, 75, 80, 85) and sector indices (13=Energi, 15=Materialer, 20=Industri, 25=Forbrugsgoder, 30=Forbrugertjenester, 35=Sundhedspleje, 40=Finans, 45=IT, 50=Telekommunikation, 55=Forsyning, 93=Essentielle forbrugsvarer, 90=Ikke-essentielle forbrugsvarer, 96=Ejendomme). These are not hierarchically related — do not aggregate.
- For the most commonly cited Danish stock market benchmark: type=60 (OMXC20, longest series from 1996) or type=85 (OMXC25, from Jan 2017). type=57 (OMXC20Cap) applies a 20% cap per constituent.
- Simple table with no measurement selectors — just filter tid and type.