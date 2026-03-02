table: fact.kv2bib2
description: Brug af bibliotekernes digitale tjenester efter tjeneste, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- tjen: values [40190=eReolen.dk, 40200=Filmstriben.dk, 40210=Litteratursiden.dk, 40220=Bibliotek.dk, 40230=Dit lokale biblioteks hjemmeside, 40240=Biblioteket-appen, 40250=Andre tjenester]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- Survey data (% of population using each digital library service). Only 2024, no geographic breakdown.
- tjen values are NOT mutually exclusive — each percentage is independent (a person can use multiple digital services). Never sum across tjen.
- kon: 10=Køn i alt, 1=Mænd, 2=Kvinder (numeric codes — different from ibib/fstrib tables which use M/K/TOT).
- alder covers 16+ only (16-24 through 75+).
- 40190=eReolen.dk is the dominant e-book platform; 40200=Filmstriben.dk is the streaming film service (see fstrib tables for usage counts).
