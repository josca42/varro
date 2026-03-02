table: fact.glob
description: Fremstillingsvirksomhedernes internationale produktion efter poster, im- og eksport, land og tid
measure: indhold (unit Mio. kr.)
columns:
- post: values [1.A.A.1.Z=Handel med varer der krydser grænsen, 1.A.A.1.Y=Salg af varer i udlandet der ikke krydser grænsen, 1.A.A.1.III=Varer købt eller solgt i udlandet i forb. med forarbejdning i udlandet, 1.A.B.1.Z=Køb af forarbejdningstjeneste i udlandet, 1.A.B.1.2=Varer der krydser grænsen i forbindelse med forarbejdning i udlandet, 1.A.A.2.2=Merchanting, salg af merchantingvarer i udlandet , 1.A.A.2.1=Merchanting, købspris for salg af merchantingvarer i udlandet (negativ eksport), 1.A.B.8=Royalties og licenser, 1.A.B.Z=Anden handel, herunder reparationsarbejde, forarbejdning, etablering af faste anlæg og koncerninterne tjenester]
- indud: values [1=Import, 2=Eksport]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [2, 4]
- tid: date range 2005-01-01 to 2024-01-01
dim docs: /dim/lande_uht_bb.md

notes:
- land has only 5 distinct values: W1 (Verden/verdens total), B6 (EU-27 uden UK), D6 (Extra EU-27), DE (Tyskland), US (USA). W1 is not in dim.lande_uht_bb — it's a special aggregate code meaning "alle lande samlet". Use WHERE land = 'W1' for world totals instead of joining.
- The matched land codes span two hierarchy levels: B6/D6 are niveau 2 (region), DE/US are niveau 4 (land). Don't filter by d.niveau when joining — it would exclude half the rows.
- indud must always be filtered: 1=Import, 2=Eksport. Every row is duplicated across both values. Forgetting this filter doubles all counts.
- post 1.A.A.2.1 (Merchanting, købspris) has negative indhold values by design — it represents a cost deduction. Don't filter out negatives.
- Typical query pattern for Danish manufacturers' total exports by transaction type: WHERE indud = 2 AND land = 'W1' GROUP BY post.