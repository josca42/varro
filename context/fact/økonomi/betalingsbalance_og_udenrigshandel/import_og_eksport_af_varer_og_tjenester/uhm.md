table: fact.uhm
description: Udenrigshandel månedlig efter poster, im- og eksport, land, enhed, sæsonkorrigering og tid
measure: indhold (unit -)
columns:
- post: values [1.A=VARER OG TJENESTER, 1.A.A=VARER, 1.A.A.1.Z=VARER DER KRYDSER DANSK GRÆNSE, 1.A.A.1.0-4X2-3=Næringsmidler, drikkevarer, tobak mv., 1.A.A.1.2=Råstoffer, ikke spiselige, undt. brændsel ... 1.A.A.1.QX=Øvrige varer der ikke krydser grænsen, 1.A.B=TJENESTER, 1.A.B.3.1=Søtransport, 1.A.B.10=Andre forretningstjenester, 1.A.B.X=Øvrige tjenester]
- indud: values [1=Import, 2=Eksport]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [2, 4]
- enhed: values [93=Millioner kroner, 100=Procentvis udvikling (måned), 101=Procentvis udvikling (3 måneder), 102=Procentvis udvikling (år)]
- saeson: values [1=Ikke sæsonkorrigeret, 2=Sæsonkorrigeret]
- tid: date range 2010-01-01 to 2025-08-01
dim docs: /dim/lande_uht_bb.md

notes:
- enhed is a measurement selector — every dimension combination is repeated for all four enhed values (93=Mio. kr., 100=pct/måned, 101=pct/3 måneder, 102=pct/år). Always filter to one: `enhed = 93` for level values in mio. kr.
- saeson must also be filtered. Not all combinations have saeson=2 (sæsonkorrigeret), but failing to filter doubles counts where both exist. Use `saeson = 1` for raw data.
- post is hierarchical (dot notation). 1.A = varer + tjenester; 1.A.A = varer; 1.A.B = tjenester. Parent rows include the total for all children — summing all post values massively double-counts. Filter to a single post code.
- land joins dim.lande_uht_bb but only 10 of 11 codes match. W1 (Verden — world total) is not in the dim table. Use `land = 'W1'` directly for the total. In uhm only 8 niveau-4 countries and 2 niveau-2 groups (B6=EU-27, D6=Extra EU-27) are present — it's a limited country set.
- ColumnValues("lande_uht_bb", "titel", for_table="uhm") shows the 10 matchable codes. Note that W1 won't appear there — reference it directly.
- Typical query: filter `enhed = 93`, `saeson = 1`, pick a single `post`, pick a `land` or join dim with `d.niveau = 4`. Forgetting enhed or saeson silently multiplies the sum.