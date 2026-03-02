table: fact.arkiv03
description: Aktivitet og personale på Rigsarkivet (Statens Arkiver) efter nøgletal og tid
measure: indhold (unit -)
columns:
- aktp: values [ITBES=Besøg på hjemmesiden (antal), SAML=Samlingernes størrelse (hyldemeter), MODT=Modtagne arkivalier (hyldemeter), ITSML=Digitale samlingers størrelse (gigabyte), ITTIL=Tilvækst af digitale arkivalier (gigabyte), GAEST=Gæster på læsesale (antal), HENV=Skriftlige henvendelser (antal), FAST=Fastansatte medarbejdere (årsværk), FRI=Frivillige medarbejdere (årsværk), TILSK=Medarbejdere i tilskudsordninger (årsværk)]
- tid: date range 2011-01-01 to 2024-01-01

notes:
- aktp is the measurement selector — one row per aktp per tid. Never sum across aktp values. Always filter to one aktp at a time.
- This table covers Rigsarkivet as a whole (no per-archive breakdown). Use arkiv01 if you need data by individual archive location.
- arkiv03 has additional digital metrics not in arkiv01: ITBES (website visits), ITSML (digital collections in GB), ITTIL (annual digital accessions in GB). For digital statistics, arkiv03 is the only option.
- Series starts 2011, four years later than arkiv01 (2007).