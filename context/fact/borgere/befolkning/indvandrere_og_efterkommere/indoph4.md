table: fact.indoph4
description: Indvandrere 1. januar efter nuværende opholdsgrundlag, oprindelseslandegruppe og tid
measure: indhold (unit Antal)
columns:
- ophgr2: values [0=I alt, 13=Asyl mv., 14=Familiesammenføring til flygtning, 15=Familiesammenføring til dansk/nordisk statsborger, 16=Familiesammenføring til udenlandsk statsborger, 501=Arbejde til EU-borger, 502=Arbejde til ikke-EU-borger, 601=Studier - herunder praktikanter - til EU-borger, 602=Studier - herunder praktikanter - til ikke-EU-borger, 901=Øvrige EU-borgere, 701=Au pair, 52=Ukraine (særlov), 801=Andet, 9998=Permanent opholdstilladelse, 999=Nordiske statsborgere]
- oprlandegrp: values [0=I alt, 361=EU-27 (uden Storbritannien), 364=Europa udenfor EU-27 (uden Storbritannien), 371=Afrika, 372=Nordamerika, 374=Asien, 375=Oceanien, 373=Syd-og Mellemamerika, 591=Statsløse, 5999=Uoplyst]
- tid: date range 2008-01-01 to 2025-01-01

notes:
- All columns are inline-coded, no dim join needed.
- ophgr2 = nuværende opholdsgrundlag (CURRENT permit). Includes 9998=Permanent opholdstilladelse. Use ophgr2=0 for all permits combined.
- oprlandegrp=0 is the total. The continent codes (361/364/371/372/373/374/375/591) are mutually exclusive and cover all immigrants. Sum these 8 regional groups = total indvandrere.
- Note: code 364 ("Europa udenfor EU-27") is in this table but not in dim.lande_psd (dim has 363 instead). No issue here since this table is fully inline.
- Simplest table for permit-type × origin-region cross-tabs.