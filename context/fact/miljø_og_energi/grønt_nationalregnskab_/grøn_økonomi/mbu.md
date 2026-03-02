table: fact.mbu
description: Industriens miljøbeskyttelsesudgifter efter branche (DB07), miljøformål og tid
measure: indhold (unit Mio. kr.)
columns:
- branche07: values [TOT=TOT Erhverv i alt, B=B Råstofindvinding, CA=CA Føde-, drikke- og tobaksvareindustri, CB=CB Tekstil- og læderindustri, 16000=16000 Træindustri ... 29000=29000 Fremst. af motorkøretøjer og dele hertil, 30000=30000 Fremst. af skibe og andre transportmidler, CM=CM Møbel og anden industri mv., 33000=33000 Reparation og installation af maskiner og udstyr, 35036=35+36 Forsyningsvirksomhed]
- mformaal: values [G_10=A Miljøbeskyttelse i alt, G_11=1.1 Driftsudgifter til miljøbeskyttelse i alt, G_12=1.2 Køb af tjenester til miljøbeskyttelse i alt, G_13=1.3 Forureningsbekæmpende investeringer i alt, G_14=1.4 Forureningsforebyggende investeringer i alt, G_15=A1 Beskyttelse af luftkvalitet og klima, G_20=A2 Spilde- og regnvandshåndtering, G_25=A3 Affaldshåndtering og genindvinding, G_75=B4 Reduceret energi- og varmeforbrug, G_76=02.5 Anden/tværgående aktivitet vedr. miljøbeskyttelse]
- tid: date range 2014-01-01 to 2023-01-01

notes:
- mformaal has two overlapping dimensions in one column — don't sum across all values. G_10 = total miljøbeskyttelse i alt. G_11/G_12/G_13/G_14 are expenditure types (operations, purchased services, end-of-pipe investments, cleaner investments) that sum to G_10. G_15/G_20/G_25/G_75/G_76 are environmental purpose categories that also sum to G_10. Pick one grouping: either expenditure type OR environmental purpose, not both.
- branche07 covers only industry (22 codes): TOT, B (Råstofindvinding), CA/CB/CM (industry aggregates), and 14 specific 5-digit DB07 codes (16000–33000 + 35036). No service sectors. Use ColumnValues("mbu", "branche07") to see all codes.
- No dim table links — all columns are inline coded.