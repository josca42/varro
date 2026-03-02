table: fact.ene1ha
description: Energiregnskab i specifikke enheder (detaljeret) efter anvendelse, energitype og tid
measure: indhold (unit -)
columns:
- anvend: values [EANV=Anvendelse i alt, EEKSPORT=Eksport, ELAGER=Lagerforøgelser, ESVIND=Ledningstab og svind, ETOT=Brancher og husholdninger ... V96000=96000 Frisører, vaskerier og andre serviceydelser, V960000=960000 Frisører, vaskerier og andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, V97000=97000 Private husholdninger med ansat medhjælp, V970000=970000 Private husholdninger med ansat medhjælp]
- energi1: values [EMRO=Råolie (ton), EMHFBK=Halvfabrikata (ton), EMRAFF=Raffinaderigas (ton), EMLPG=LPG (ton), EMLPGTR=LPG_transport (ton) ... EMBIOOIL=Biodiesel, bioethanol og bioolie (ton), EMVMP=Omgivelsesvarme indvundet med varmepumper (TJ), EMEL=El (GWh), EMFJV=Fjernvarme (TJ), EMGVG=Bygas (1000 Nm3)]
- tid: date range 1966-01-01 to 2024-01-01

notes:
- energi1 encodes fuel type AND native unit (e.g. EMEL=El (GWh), EMFJV=Fjernvarme (TJ)). Do NOT sum across energy types — units are incompatible. Use ene2ha for cross-fuel GJ comparisons.
- anvend mixes macro use categories (EANV, EEKSPORT, ELAGER, ESVIND, ETOT) with sector-level consumption codes (V{NACE}...). Filter to one level.
- This is the use/anvend-side detail. Counterpart: ene1ht (supply side).