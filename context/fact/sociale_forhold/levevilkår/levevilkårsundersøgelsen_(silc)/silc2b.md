table: fact.silc2b
description: Boligbyrde: Andel personer efter socioøkonomisk status, køn, i hvor høj grad husstanden synes boligudgiften er en byrde og tid
measure: indhold (unit Pct.)
columns:
- socio: values [TOT=I alt, 001=Beskæftigede, B=Børn, 165=Studerende, 11A=Ikke beskæftigede inkl. førtidspensionister, 33A=Folkepensionister og efterlønsmodtagere]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- svaerhed1: values [100=I alt, 115=En tung byrde, 120=Noget af en byrde, 125=Ikke noget problem]
- tid: date range 2004-01-01 to 2024-01-01
notes:
- Housing cost burden by socioeconomic status and gender. Same series as silc1b (2004–2024), percentages only.
- svaerhed1=100 is always indhold=100 (dummy total). Use svaerhed1 IN (115, 120, 125) for the real distribution; they sum to 100%.
- socio: TOT, 001=Beskæftigede, B=Børn, 165=Studerende, 11A=Ikke beskæftigede inkl. førtidspensionister, 33A=Folkepensionister og efterlønsmodtagere.
- koen: TOT, M, K. For overall by socio group: WHERE koen='TOT'.
