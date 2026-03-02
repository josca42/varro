table: fact.ene2ho
description: Energiregnskab i GJ (oversigt) efter tilgang og anvendelse, energitype og tid
measure: indhold (unit GJ (gigajoule))
columns:
- tilanv: values [ETIL=Tilgang i alt, EIMPORT=Import, EPRODM=Produktion mv, EANV=Anvendelse i alt, EEKSPORT=Eksport, ELAGER=Lagerforøgelser, ESVIND=Ledningstab og svind, ETOT=Brancher og husholdninger]
- energi1: values [ETOT=I ALT, EROOL=RÅOLIE OG HALVFABRIKATA, ERO=Råolie, EHFBK=Halvfabrikata, EOIL=OLIEPRODUKTER ... EVMP=Omgivelsesvarme indvundet med varmepumper, EKONV=KONVERTEREDE ENERGIARTER, EEL=El, EFJV=Fjernvarme, EGVG=Bygas]
- tid: date range 1966-01-01 to 2024-01-01

notes:
- tilanv is a supply/use selector. ETIL=total supply (=EIMPORT+EPRODM). EANV=total use (=ETOT+EEKSPORT+ELAGER+ESVIND). Rows for all values exist in the same table — filter tilanv to a single code to avoid summing across the balance.
- energi1 has ETOT (grand total) plus sub-codes by fuel type. Only select ETOT or specific fuels, not both.
- indhold is in GJ for all energy types — the unified unit version. ene1ho is the equivalent with native units (ton, TJ, GWh etc per energy type).
- For cross-fuel totals (e.g. total import), use energi1='ETOT'. For fuel breakdowns, pick specific codes and exclude aggregate codes.