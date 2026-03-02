table: fact.bbq
description: Betalingsbalancen kvartalsvis efter poster, indtægt/udgift, land og tid
measure: indhold (unit Mio. kr.)
columns:
- post: values [1=BETALINGSBALANCENS LØBENDE POSTER, 1.A=VARER OG TJENESTER, 1.A.A=VARER, 1.A.A.1.Z=VARER DER KRYDSER DANSK GRÆNSE, 1.A.A.1.Q=VARER DER IKKE KRYDSER DANSK GRÆNSE ... 1.C.0.6=Løbende overførsler, andre overførsler, 2=Kapitaloverførsler mv., NF=Nettofordringserhvervelsen, 3=FINANSIELLE POSTER I ALT, 4.5=FEJL OG UDELADELSER]
- indudbop: values [K=Løbende indtægter, D=Løbende udgifter, N=Nettoindtægter]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [2, 4]
- tid: date range 2005-01-01 to 2025-04-01
dim docs: /dim/lande_uht_bb.md

notes:
- land joins lande_uht_bb at niveau 2 (2 regions: B6=EU-27, D6=Extra EU-27) and niveau 4 (21 individual countries). Filter WHERE d.niveau = 4 for country breakdown or d.niveau = 2 for regional totals. Avoid mixing levels to prevent double-counting.
- Unmatched land codes (not in dim): W1=alle lande i alt, I9=Eurozone, J9=OECD, P7=OPEC. These are extra aggregates present in the fact table. Use them directly as inline filters (e.g. land='W1') rather than joining the dim.
- post is hierarchical — '1' equals sum of '1.A' (varer og tjenester) + '1.B' (indkomst) + '1.C' (løbende overførsler). Never sum across hierarchy levels. The tree goes 5–6 levels deep. Filter to one post code for a coherent measure.
- indudbop: N = K − D. Filter to one value. For net current account balance use indudbop='N'.
- For total Denmark quarterly net balance: WHERE post='1' AND indudbop='N' AND land='W1'