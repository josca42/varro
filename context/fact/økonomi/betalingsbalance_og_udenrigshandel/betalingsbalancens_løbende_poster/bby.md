table: fact.bby
description: Betalingsbalancen årlig efter poster, indtægt/udgift, land og tid
measure: indhold (unit Mio. kr.)
columns:
- post: values [1=BETALINGSBALANCENS LØBENDE POSTER, 1.A=VARER OG TJENESTER, 1.A.A=VARER, 1.A.A.1.Z=VARER DER KRYDSER DANSK GRÆNSE, 1.A.A.1.Q=VARER DER IKKE KRYDSER DANSK GRÆNSE ... 1.C.0.6=Løbende overførsler, andre overførsler, 2=Kapitaloverførsler mv., NF=Nettofordringserhvervelsen, 3=FINANSIELLE POSTER I ALT, 4.5=FEJL OG UDELADELSER]
- indudbop: values [K=Løbende indtægter, D=Løbende udgifter, N=Nettoindtægter]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [1, 2, 3, 4]
- tid: date range 2005-01-01 to 2024-01-01
dim docs: /dim/lande_uht_bb.md

notes:
- land has the richest geographic breakdown of all tables in this subject: all 4 niveaus present (1=verdensdel, 2=region, 3=underregion, 4=individuelt land — 252 countries matched). Always filter d.niveau to a single level to avoid double-counting hierarchy levels.
- Unmatched land codes (extra aggregates not in dim): W1=alle lande, I9=Eurozone, J9=OECD, P2=?, P7=OPEC, 4F=?, 4S=?. Use these inline (land='W1') without joining the dim.
- Use ColumnValues("lande_uht_bb", "titel", for_table="bby") to see all 252 matched country/region codes — the for_table filter is important here since lande_uht_bb has 237 individual countries at niveau 4 alone.
- post is hierarchical — parent posts are sums of children. Do not sum across levels. This table has the most detailed post hierarchy (bbq/vbbq subset). Filter to one post code.
- indudbop: N = K − D. Filter to one value.
- For a complete country-breakdown of annual net balance: WHERE post='1' AND indudbop='N' AND d.niveau=4