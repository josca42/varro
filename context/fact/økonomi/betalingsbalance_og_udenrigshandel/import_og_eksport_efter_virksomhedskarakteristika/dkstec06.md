table: fact.dkstec06
description: Udenrigshandel med tjenester (virksomhedskarakteristika efter økonomiske enheder) efter im- og eksport, branche, poster og tid
measure: indhold (unit Mio. kr.)
columns:
- indud: values [IMP=Import, EXP=Eksport]
- branche: join dim.db on branche=kode::text [approx]
- post: values [0=TJENESTER I ALT, 1=FORARBEJDNINGSTJENESTER, 2=REPARATIONSTJENESTER, 3=TRANSPORT, 3.1=Søtransport, 3.2=Lufttransport, 3.3=Anden transport (end sø- og luft), 3.4=Post- og kurertjenester, 4=REJSER, 5=BYGGE- OG ANLÆGSTJENESTER, 6=FORSIKRINGSTJENESTER, 7=FINANSIELLE TJENESTER, 8=ROYALTIES OG LICENSER, 9=TELEKOMMUNIKATIONS-, COMPUTER- OG INFORMATIONSTJENESTER, 10=ANDRE FORRETNINGSTJENESTER, 10.1=Forsknings- og udviklingstjenester, 10.2=Professionelle og administrative tjenester, 10.3=Tekniske-, handelsrelaterede og øvrige forretningstjenester, 11=AUDIOVISUELLE TJENESTER SAMT TJENESTER IFM. UDDANNELSE, SUNDHED, KULTUR OG REKREATION, 12=OFFENTLIGE TJENESTER]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- Always filter indud to either 'IMP' or 'EXP'. Both directions are separate rows.
- branche contains only letter codes — do not join to dim.db. Inline values: '_T' = total, '_U' = uoplyst, '_O' = other. Use ColumnValues("dkstec06", "branche") to see the full list.
- post is hierarchical. '0' = TJENESTER I ALT (total). '3' = TRANSPORT aggregates '3.1' (Søtransport) + '3.2' (Lufttransport) + '3.3' (Anden transport) + '3.4' (Post- og kurertjenester). '10' = ANDRE FORRETNINGSTJENESTER aggregates '10.1' + '10.2' + '10.3'. Do not sum parent and child codes together. Filter to '0' for a grand total, or pick individual sub-codes for breakdown.
- This is the only table in the subject with a time series (2019–2023, annual). Use it for trends in services trade by type. The other services tables (stec01, stec02) have only 2023.