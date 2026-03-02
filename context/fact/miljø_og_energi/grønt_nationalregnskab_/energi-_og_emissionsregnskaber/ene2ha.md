table: fact.ene2ha
description: Energiregnskab i GJ (detaljeret) efter anvendelse, energitype og tid
measure: indhold (unit GJ (gigajoule))
columns:
- anvend: values [EANV=Anvendelse i alt, EEKSPORT=Eksport, ELAGER=Lagerforøgelser, ESVIND=Ledningstab og svind, ETOT=Brancher og husholdninger ... V96000=96000 Frisører, vaskerier og andre serviceydelser, V960000=960000 Frisører, vaskerier og andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, V97000=97000 Private husholdninger med ansat medhjælp, V970000=970000 Private husholdninger med ansat medhjælp]
- energi1: values [ETOT=I ALT, EROOL=RÅOLIE OG HALVFABRIKATA, ERO=Råolie, EHFBK=Halvfabrikata, EOIL=OLIEPRODUKTER ... EVMP=Omgivelsesvarme indvundet med varmepumper, EKONV=KONVERTEREDE ENERGIARTER, EEL=El, EFJV=Fjernvarme, EGVG=Bygas]
- tid: date range 1966-01-01 to 2024-01-01

notes:
- anvend mixes use-side macro categories (EANV, EEKSPORT, ELAGER, ESVIND, ETOT) with sector-level consumption codes (VA, VC, V{NACE}...). EANV=total of all; ETOT=sectors+households. Multiple hierarchy levels coexist — filter to one.
- energi1 is in GJ. ETOT=total; sub-codes are fuel components. Filter to one level.
- Counterpart to ene2ht (supply side). For sector energy consumption with fuel detail, this table is the right choice over ene3h (which only has GJ, no supply/use split).