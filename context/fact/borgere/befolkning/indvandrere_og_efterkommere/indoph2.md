table: fact.indoph2
description: Indvandrere 1. januar efter første opholdsgrundlag, oprindelseslandegruppe og tid
measure: indhold (unit Antal)
columns:
- ophgr1: values [0=I alt, 13=Asyl mv., 14=Familiesammenføring til flygtning, 15=Familiesammenføring til dansk/nordisk statsborger, 16=Familiesammenføring til udenlandsk statsborger, 501=Arbejde til EU-borger, 502=Arbejde til ikke-EU-borger, 601=Studier - herunder praktikanter - til EU-borger, 602=Studier - herunder praktikanter - til ikke-EU-borger, 901=Øvrige EU-borgere, 701=Au pair, 52=Ukraine (særlov), 801=Andet, 999=Nordiske statsborgere]
- oprlandegrp: join dim.lande_psd on oprlandegrp=kode [approx]; levels [2, 3]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/lande_psd.md

notes:
- oprlandegrp code 364 ("Europa udenfor EU-27 (uden Storbritannien)") is in the fact table but missing from dim.lande_psd (dim has 363 "Andre europæiske lande" instead). A JOIN on dim.lande_psd will silently drop all code-364 rows. Treat oprlandegrp as inline-coded or use indoph4 which has the same continent groups but fully inline.
- oprlandegrp=0 is the total ("I alt"). Other codes are niveau=2 continent groups (361=EU-27, 371=Afrika, 372=Nordamerika, 373=Syd/Mellam-Amerika, 374=Asien, 375=Oceanien, 591=Statsløse, 5999=Uoplyst) plus the problematic 364.
- ophgr1 = første opholdsgrundlag (same as indoph1). Use ophgr1=0 for all permit types.
- For reliable continent-group queries, prefer indoph4 which has the same groups fully documented inline.