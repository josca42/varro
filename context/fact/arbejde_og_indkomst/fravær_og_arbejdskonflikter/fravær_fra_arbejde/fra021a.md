table: fact.fra021a
description: Fravær efter sektor, køn, fraværsårsag, uddannelse, fraværsindikator og tid
measure: indhold (unit -)
columns:
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1016=Stat (inklusiv sociale kasser og fonde), 1018=Kommuner og regioner i alt, 1020=Regioner, 1025=Kommuner, 1046=Virksomheder og organisationer, 1047=Virksomheder og organisationer - fastlønnede, 1048=Virksomheder og organisationer - timelønnede]
- kon: values [0=I alt, 1=Mænd, 2=Kvinder]
- fravaer: values [1100=Egen sygdom, 1200=Børns sygdom, 1300=Arbejdsulykke, 1400=Barsels- og adoptionsorlov]
- uddannelse: join dim.ddu_udd on uddannelse=kode [approx]
- fravaer1: values [10=Fraværsprocent, 40=Gennemsnitlige antal fraværsdagsværk pr. fuldtidsansat, 50=Gennemsnitlige antal fraværsperioder pr. helårsansat, 60=Gennemsnitlige antal kalenderdage pr. fraværsperiode, 70=Fuldtidsansatte, 80=Helårsansatte, 30=Fraværsperioder (antal), 20=Fraværsdagsværk (antal)]
- tid: date range 2015-01-01 to 2023-01-01
dim docs: /dim/ddu_udd.md
notes:
- uddannelse does NOT join dim.ddu_udd — the H10-H90 codes use a different classification. Treat as inline: use ColumnValues("fra021a", "uddannelse") which returns labels like 'H10 Grundskole', 'H20 Gymnasiale uddannelser', ..., 'H90 Uoplyst mv.'. TOT=I alt.
- fravaer1 is a measurement-type selector with 8 values. Every dimension combination is repeated 8 times. Always filter fravaer1 to one value.
- fravaer is the absence cause (4 values). sektor='1000' and kon='0' are the totals — include or exclude as appropriate.
- This table starts from 2015 (fra020/fra022-fra024 go back to 2013).
