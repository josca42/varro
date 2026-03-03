table: fact.arkiv02b
description: Aktivitet og personale på stads- og lokalarkiver efter område, nøgletal og tid
measure: indhold (unit -)
columns:
- blstkom: join dim.nuts on blstkom=kode; levels [2]
- aktp: values [SAML=Samlingernes størrelse (hyldemeter), MODT=Modtagne arkivalier (hyldemeter), GAEST=Gæster på læsesale (antal), HENV=Skriftlige henvendelser (antal), FAST=Fastansatte medarbejdere (årsværk), FRI=Frivillige medarbejdere (årsværk), TILSK=Medarbejdere i tilskudsordninger (årsværk)]
- tid: date range 2016-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- blstkom joins dim.nuts at niveau=2 (landsdele). The table contains codes 0–11 (excluding 4). Use: JOIN dim.nuts d ON f.blstkom = d.kode WHERE d.niveau = 2
- blstkom=0 is a national aggregate total — exclude it when summing across regions to avoid double-counting.
- Bornholm (kode=4, Landsdel Bornholm) is absent from this table — either merged into another landsdel or not separately reported for local archives.
- aktp is the measurement selector — one row per (blstkom, tid) per aktp. Never sum across aktp values. Always filter to one aktp at a time.
- This table covers stads- og lokalarkiver only (municipal/local archives). Use arkiv01 or arkiv03 for Rigsarkivet (national state archives).
- Map: /geo/landsdele.parquet (niveau 2) — merge on blstkom=dim_kode. Exclude blstkom=0.