table: fact.arkiv01
description: Aktivitet og personale på Rigsarkivet (Statens Arkiver) efter arkiver, nøgletal og tid
measure: indhold (unit -)
columns:
- arkiv: values [TOT=Rigsarkivet i alt (før: Statens Arkiver), DDA=Rigsarkivet Odense DDA (før: Dansk Data Arkiv), ERH=Rigsarkivet Aarhus (før: Erhvervsarkivet), LFYN=Rigsarkivet Odense  (før: Landsarkivet for Fyn), LNJ=Rigsarkivet Viborg (før: Landsarkivet for Nørrejylland), LSJ=Landsarkivet for Sjælland, LSOJ=Rigsarkivet Aabenraa (før: Landsarkivet for Sønderjylland), RIGS=Rigsarkivet København (før: Rigsarkivet)]
- aktp: values [SAML=Samlingernes størrelse (hyldemeter), MODT=Modtagne arkivalier (hyldemeter), GAEST=Gæster på læsesale (antal), HENV=Skriftlige henvendelser (antal), FAST=Fastansatte medarbejdere (årsværk), FRI=Frivillige medarbejdere (årsværk), TILSK=Medarbejdere i tilskudsordninger (årsværk)]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- aktp is the measurement selector — each (arkiv, tid) combination has one row per aktp. Never sum across aktp values; they measure completely different things (shelf metres, visitors, FTE staff, etc). Always filter to one aktp at a time.
- arkiv TOT is the national aggregate and equals the sum of the sub-archives. Exclude TOT when you want to sum across archives yourself.
- The set of sub-archives shrank over time: in 2007–2013 there were 7 codes (DDA, ERH, LFYN, LNJ, LSJ, LSOJ, RIGS); by 2024 only 4 remain (LFYN, LNJ, LSOJ, RIGS) as several were merged into Rigsarkivet. Time series for a specific archive code will have gaps or end mid-series. Use TOT for a continuous national series.
- arkiv03 covers the same institution but adds digital metrics (website visits, digital collections GB) absent from arkiv01, and has no archive-level breakdown.