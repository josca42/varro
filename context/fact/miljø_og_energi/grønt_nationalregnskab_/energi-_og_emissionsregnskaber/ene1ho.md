table: fact.ene1ho
description: Energiregnskab i specifikke enheder (oversigt) efter tilgang og anvendelse, energitype og tid
measure: indhold (unit -)
columns:
- tilanv: values [ETIL=Tilgang i alt, EIMPORT=Import, EPRODM=Produktion mv, EANV=Anvendelse i alt, EEKSPORT=Eksport, ELAGER=Lagerforøgelser, ESVIND=Ledningstab og svind, ETOT=Brancher og husholdninger]
- energi1: values [EMRO=Råolie (ton), EMHFBK=Halvfabrikata (ton), EMRAFF=Raffinaderigas (ton), EMLPG=LPG (ton), EMLPGTR=LPG_transport (ton) ... EMBIOOIL=Biodiesel, bioethanol og bioolie (ton), EMVMP=Omgivelsesvarme indvundet med varmepumper (TJ), EMEL=El (GWh), EMFJV=Fjernvarme (TJ), EMGVG=Bygas (1000 Nm3)]
- tid: date range 1966-01-01 to 2024-01-01

notes:
- energi1 encodes both the fuel type AND its native unit in the code label (e.g. EMEL=El (GWh), EMFJV=Fjernvarme (TJ), EMRO=Råolie (ton)). indhold values are in these mixed units — do NOT sum across energy types, as the units are incompatible.
- tilanv: ETIL=total supply (EIMPORT+EPRODM), EANV=total use. These are top-level balance rows — the overview counterpart to ene1ht (supply detail) and ene1ha (use detail).
- Use ene2ho/ene2ht/ene2ha (GJ tables) for cross-fuel comparisons. Use ene1* tables when you need native units (e.g. GWh of electricity, ton of oil).